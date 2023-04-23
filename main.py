from database import DataBase as Db
from views.login import *

d1 = Db()

d1.clear("Expenses")

d1.push("Expenses", 
        [('User1', 'Lody', 4),
         ('User1', 'Zakupy', 120),
         ('User2', 'Samochod', 90000),
         ])

# for i in d1.pull_rows("Expenses"):
#     print(i)

lg = Login(d1)

lg.login_view("", "")

