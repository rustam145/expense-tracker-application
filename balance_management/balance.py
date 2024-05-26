from decimal import Decimal

class Balance:
    def __init__(self, db):
        self.db = db

    def get_balance(self, user_id):
        query = "SELECT balance FROM Users WHERE user_id = %s"
        balance = self.db.execute_read_query(query, (user_id,))
        return balance[0][0] if balance else Decimal(0.0)
    
    def update_balance(self, user_id, amount):
        current_balance = self.get_balance(user_id)
        new_balance = current_balance + amount
        query = "UPDATE Users SET balance = %s WHERE user_id = %s"
        self.db.execute_query(query, (new_balance, user_id))
        return new_balance

    def deposit(self, user_id, amount):
        self.update_balance(user_id, Decimal(amount))
        print(f"Deposited {amount} to user {user_id}'s balance.")

