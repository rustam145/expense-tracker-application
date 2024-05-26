import psycopg2

class Database:
    def __init__(self, dbname="expense_tracker_db_2", user="postgres", password="7878", host="localhost", port="5432"):
        self.connection = self.create_connection(dbname, user, password, host, port)
        self.cursor = self.connection.cursor()

    def create_connection(self, dbname, user, password, host, port):
        try:
            connection = psycopg2.connect(
                dbname=dbname,
                user=user,
                password=password,
                host=host,
                port=port
            )
            print("Successfully connected to the database")
            return connection
        except psycopg2.Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            print("Query executed successfully")
        except psycopg2.Error as e:
            print(f"The error '{e}' occurred")

    def execute_read_query(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            result = self.cursor.fetchall()
            return result
        except psycopg2.Error as e:
            print(f"The error '{e}' occurred")
            return []

    def close(self):
        self.cursor.close()
        self.connection.close()
