from tabulate import tabulate

class Category:
    def __init__(self, db):
        self.db = db

    def create_category(self, name):
        query = "INSERT INTO Categories (name) VALUES (%s)"
        self.db.execute_query(query, (name,))

    def get_categories(self):
        query = "SELECT * FROM Categories"
        categories = self.db.execute_read_query(query)
        print(tabulate(categories, headers=["category_id", "name"], tablefmt="psql"))

    def update_category(self, category_id, name):
        query = "UPDATE Categories SET name = %s WHERE category_id = %s"
        self.db.execute_query(query, (name, category_id))

    def delete_category(self, category_id):
        query = "DELETE FROM Categories WHERE category_id = %s"
        self.db.execute_query(query, (category_id,))

    def search_categories(self, search_term):
        query = "SELECT * FROM Categories WHERE name ILIKE %s"
        categories = self.db.execute_read_query(query, (f"%{search_term}%",))
        print(tabulate(categories, headers=["category_id", "name"], tablefmt="psql"))
