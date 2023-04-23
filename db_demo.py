import sqlite3

class DataBase:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("users.db")
        self.c = self.conn.cursor()
    
        
        self.c.execute("""CREATE TABLE IF NOT EXISTS Expenses (u_name TEXT , expense_name TEXT, expense INTEGER)""")

        self.c.execute("""CREATE TABLE IF NOT EXISTS Incomes (u_name TEXT , income_name TEXT, income INTEGER)""")
        self.conn.commit()

    # data jest listą krotek Np. [('User1', 'haslo123', '...', '...')]
    def push(self, data: list) -> None:
        try:
            for i in data:
                ref = "INSERT INTO Users VALUES" + str(i)
                self.c.execute(ref)
        except sqlite3.IntegrityError:
            print('User with that username already exists')
        self.conn.commit()

    def pull_rows(self):
        return self.c.execute("SELECT * FROM Users") # chwilowe rozwiązanie
    
    def query(self, query: str):
        pass

    # czyści wszystkie wiersze
    def clear(self) -> None:
        self.c.execute("DELETE FROM Users")
        self.conn.commit()