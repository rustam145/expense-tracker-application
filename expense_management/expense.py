from tabulate import tabulate
from decimal import Decimal

class Expense:
    def __init__(self, db):
        self.db = db

    def create_expense(self, user_id, category_id, amount, date, description, payment_method):
        # First, create the expense record
        query = "INSERT INTO Expenses (user_id, category_id, amount, date, description, payment_method) VALUES (%s, %s, %s, %s, %s, %s) RETURNING expense_id"
        self.db.execute_query(query, (user_id, category_id, amount, date, description, payment_method))
        
        # Second, deduct the amount from the user's balance
        query_balance = "SELECT balance FROM Users WHERE user_id = %s"
        current_balance = self.db.execute_read_query(query_balance, (user_id,))[0][0]

        amount = Decimal(amount)  # Convert amount to decimal
        new_balance = current_balance - amount

        query_update_balance = "UPDATE Users SET balance = %s WHERE user_id = %s"
        self.db.execute_query(query_update_balance, (new_balance, user_id))

        print(f"Expense added successfully. New balance for user {user_id}: {new_balance}")

        return new_balance  # Return the updated balance after expense deduction

    def get_expenses(self):
        query = "SELECT * FROM Expenses"
        expenses = self.db.execute_read_query(query)
        print(tabulate(expenses, headers=["expense_id", "user_id", "category_id", "amount", "date", "description", "payment_method"], tablefmt="psql"))

    def update_expense(self, expense_id, user_id=None, category_id=None, amount=None, date=None, description=None, payment_method=None):
        if user_id:
            query = "UPDATE Expenses SET user_id = %s WHERE expense_id = %s"
            self.db.execute_query(query, (user_id, expense_id))
        if category_id:
            query = "UPDATE Expenses SET category_id = %s WHERE expense_id = %s"
            self.db.execute_query(query, (category_id, expense_id))
        if amount:
            query = "UPDATE Expenses SET amount = %s WHERE expense_id = %s"
            self.db.execute_query(query, (amount, expense_id))
        if date:
            query = "UPDATE Expenses SET date = %s WHERE expense_id = %s"
            self.db.execute_query(query, (date, expense_id))
        if description:
            query = "UPDATE Expenses SET description = %s WHERE expense_id = %s"
            self.db.execute_query(query, (description, expense_id))
        if payment_method:
            query = "UPDATE Expenses SET payment_method = %s WHERE expense_id = %s"
            self.db.execute_query(query, (payment_method, expense_id))

    def delete_expense(self, expense_id):
        query = "DELETE FROM Expenses WHERE expense_id = %s"
        self.db.execute_query(query, (expense_id,))

    def filter_expenses(self, search_term):
        query = """
        SELECT * FROM Expenses 
        WHERE CAST(user_id AS TEXT) ILIKE %s 
        OR CAST(category_id AS TEXT) ILIKE %s 
        OR CAST(amount AS TEXT) ILIKE %s 
        OR date::TEXT ILIKE %s 
        OR description ILIKE %s 
        OR payment_method ILIKE %s
        """
        expenses = self.db.execute_read_query(query, (f"%{search_term}%",) * 6)
        print(tabulate(expenses, headers=["expense_id", "user_id", "category_id", "amount", "date", "description", "payment_method"], tablefmt="psql"))

    def show_expense_table(self):
        query = "SELECT * FROM Expenses"
        expenses = self.db.execute_read_query(query)
        if expenses:
            print(tabulate(expenses, headers=["expense_id", "user_id", "category_id", "amount", "date", "description", "payment_method"], tablefmt="psql"))
        else:
            print("No expenses found")

    def generate_report(self, report_type):
        if report_type == "category":
            query = """
            SELECT c.name AS category, SUM(e.amount) AS total_amount
            FROM Expenses e
            JOIN Categories c ON e.category_id = c.category_id
            GROUP BY c.name
            ORDER BY total_amount DESC
            """
        elif report_type == "user":
            query = """
            SELECT u.username AS user_name, SUM(e.amount) AS total_amount
            FROM Expenses e
            JOIN Users u ON e.user_id = u.user_id
            GROUP BY u.username
            ORDER BY total_amount DESC
            """
        else:
            print("Invalid report type")
            return

        report = self.db.execute_read_query(query)
        if report:
            if report_type == "category":
                print("\nExpense Report by Category:")
                print(tabulate(report, headers=["Category", "Total Amount"], tablefmt="psql"))
            elif report_type == "user":
                print("\nExpense Report by User:")
                print(tabulate(report, headers=["User", "Total Amount"], tablefmt="psql"))
        else:
            print("No expenses found for the report")
