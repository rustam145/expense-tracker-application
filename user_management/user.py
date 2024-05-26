from tabulate import tabulate

class User:
    def __init__(self, db):
        self.db = db

    def create_user(self, username, password, email):
        query = "INSERT INTO Users (username, password, email) VALUES (%s, %s, %s)"
        self.db.execute_query(query, (username, password, email))

    def get_users(self):
        query = "SELECT user_id, username, password, email, balance FROM Users"
        try:
            users = self.db.execute_read_query(query)
            if users:
                colnames = ["user_id", "username", "password", "email", "balance"]
                print(tabulate(users, headers=colnames, tablefmt="psql"))
            else:
                print("No users found")
        except Exception as e:
            print(f"Error fetching data from the database: {e}")

    def update_user(self, user_id, username=None, password=None, email=None):
        if username:
            query = "UPDATE Users SET username = %s WHERE user_id = %s"
            self.db.execute_query(query, (username, user_id))
        if password:
            query = "UPDATE Users SET password = %s WHERE user_id = %s"
            self.db.execute_query(query, (password, user_id))
        if email:
            query = "UPDATE Users SET email = %s WHERE user_id = %s"
            self.db.execute_query(query, (email, user_id))

    def delete_user(self, user_id):
        query = "DELETE FROM Users WHERE user_id = %s"
        self.db.execute_query(query, (user_id,))

    def search_users(self, search_term):
        query = "SELECT * FROM Users WHERE username ILIKE %s OR email ILIKE %s"
        users = self.db.execute_read_query(query, (f"%{search_term}%", f"%{search_term}%"))
        print(tabulate(users, headers=["user_id", "username", "password", "email", "balance"], tablefmt="psql"))
