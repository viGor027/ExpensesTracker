import sqlite3

class DataBase:
    def __init__(self):
        self.conn = sqlite3.connect("users.db")
        self.c = self.conn.cursor()
    
        self.c.execute("""CREATE TABLE IF NOT EXISTS Login (u_name TEXT PRIMARY KEY, u_pwd TEXT)""")

        self.c.execute("""CREATE TABLE IF NOT EXISTS Expenses (u_name TEXT , expense_name TEXT, expense INTEGER)""")

        self.c.execute("""CREATE TABLE IF NOT EXISTS Incomes (u_name TEXT , income_name TEXT, income INTEGER)""")

    # data jest listą krotek Np. [('User1', 'haslo123', '...', '...')]
    def push(self, table: str, data: list):
        try:
            for i in data:
                ref = "INSERT INTO " + table + " VALUES" + str(i)
                self.c.execute(ref)
        except sqlite3.IntegrityError:
            print('User with that username already exists')
        self.conn.commit()

    def pull_rows(self, table: str):
        query = "SELECT * FROM " + table
        return self.c.execute(query) # chwilowe rozwiązanie
    
    def query(self, query: str):
        return self.c.execute(query)
    
    def user_exists(self, user: str):
        user_count = 0
        q1 = "SELECT 1 FROM Login where u_name='" + user + "'"
        for i in self.query(q1):
            user_count += i[0]

        if user_count:
            return True
        else:
            return False

    # czyści wszystkie wiersze podanej tabelu
    def clear(self, table: str):
        query = "DELETE FROM " + table
        self.c.execute(query)
        self.conn.commit()