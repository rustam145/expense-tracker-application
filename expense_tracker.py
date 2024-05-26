from Database.database import Database
from user_management.user import User
from catagory_management.category import Category
from expense_management.expense import Expense
from balance_management.balance import Balance
from decimal import Decimal

class ExpenseTracker:
    def __init__(self):
        self.db = Database()
        self.user = User(self.db)
        self.category = Category(self.db)
        self.expense = Expense(self.db)
        self.balance = Balance(self.db)

    def show_main_menu(self):
        while True:
            print("\n--- Expense Tracker Main Menu ---")
            print("1. Manage Users")
            print("2. Manage Categories")
            print("3. Manage Expenses")
            print("4. Manage Balance")
            print("5. Show Expense Table")
            print("6. Generate Report")
            print("7. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.show_user_menu()
            elif choice == '2':
                self.show_category_menu()
            elif choice == '3':
                self.show_expense_menu()
            elif choice == '4':
                self.show_balance_menu()
            elif choice == '5':
                self.expense.show_expense_table()
            elif choice == '6':
                self.generate_report_menu()
            elif choice == "7":
                self.db.close()
                print("Goodbye!")
                print("Exiting Expense Tracker...")
                break
            else:
                print("Invalid choice. Please try again.")

    def show_user_menu(self):
        while True:
            print("\n--- User Management ---")
            print("1. Add User")
            print("2. View Users")
            print("3. Update User")
            print("4. Delete User")
            print("5. Search Users")
            print("6. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                username = input("Enter username: ")
                password = input("Enter password: ")
                email = input("Enter email: ")
                self.user.create_user(username, password, email)
            elif choice == '2':
                self.user.get_users()
            elif choice == '3':
                user_id = int(input("Enter user ID to update: "))
                username = input("Enter new username (leave blank to keep current): ")
                password = input("Enter new password (leave blank to keep current): ")
                email = input("Enter new email (leave blank to keep current): ")
                self.user.update_user(user_id, username, password, email)
            elif choice == '4':
                user_id = int(input("Enter user ID to delete: "))
                self.user.delete_user(user_id)
            elif choice == '5':
                search_term = input("Enter search term: ")
                self.user.search_users(search_term)
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

    def show_category_menu(self):
        while True:
            print("\n--- Category Management ---")
            print("1. Add Category")
            print("2. View Categories")
            print("3. Update Category")
            print("4. Delete Category")
            print("5. Search Categories")
            print("6. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter category name: ")
                self.category.create_category(name)
            elif choice == '2':
                self.category.get_categories()
            elif choice == '3':
                category_id = int(input("Enter category ID to update: "))
                name = input("Enter new category name: ")
                self.category.update_category(category_id, name)
            elif choice == '4':
                category_id = int(input("Enter category ID to delete: "))
                self.category.delete_category(category_id)
            elif choice == '5':
                search_term = input("Enter search term: ")
                self.category.search_categories(search_term)
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

    def show_expense_menu(self):
        while True:
            print("\n--- Expense Management ---")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Update Expense")
            print("4. Delete Expense")
            print("5. Filter Expenses")
            print("6. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                user_id = int(input("Enter user ID: "))
                category_id = int(input("Enter category ID: "))
                amount = Decimal(input("Enter amount: "))
                date = input("Enter date (YYYY-MM-DD): ")
                description = input("Enter description: ")
                payment_method = input("Enter payment method: ")
                self.expense.create_expense(user_id, category_id, amount, date, description, payment_method)
            elif choice == '2':
                self.expense.get_expenses()
            elif choice == '3':
                expense_id = int(input("Enter expense ID to update: "))
                user_id = int(input("Enter new user ID (leave blank to keep current): ") or 0)
                category_id = int(input("Enter new category ID (leave blank to keep current): ") or 0)
                amount = input("Enter new amount (leave blank to keep current): ")
                date = input("Enter new date (leave blank to keep current): ")
                description = input("Enter new description (leave blank to keep current): ")
                payment_method = input("Enter new payment method (leave blank to keep current): ")
                self.expense.update_expense(expense_id, user_id if user_id else None, category_id if category_id else None, Decimal(amount) if amount else None, date if date else None, description if description else None, payment_method if payment_method else None)
            elif choice == '4':
                expense_id = int(input("Enter expense ID to delete: "))
                self.expense.delete_expense(expense_id)
            elif choice == '5':
                search_term = input("Enter search term: ")
                self.expense.filter_expenses(search_term)
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

    def generate_report_menu(self):
            
        while True:

            print("\nGenerate Report Menu")
            print("1. By Category")
            print("2. By User")
            print("3. Back to Main Menu")

            report_choice = input("Enter your choice: ")

            if report_choice == "1":
                self.expense.generate_report("category")
            elif report_choice == "2":
                self.expense.generate_report("user")
            elif report_choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")

    def show_balance_menu(self):
        while True:
            print("\n--- Balance Management ---")
            print("1. View Balance")
            print("2. Deposit Balance")
            print("3. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                user_id = int(input("Enter user ID: "))
                balance = self.balance.get_balance(user_id)
                print(f"Current balance for user {user_id}: {balance}")
            elif choice == '2':
                user_id = int(input("Enter user ID: "))
                amount = Decimal(input("Enter amount to deposit: "))
                new_balance = self.balance.deposit(user_id, amount)
                print(f"New balance for user {user_id}: {new_balance}")
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")
