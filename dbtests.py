from database import DataBase as Db
from views.login import *
from views.register import *

d1 = Db()

d1.clear("Expenses")
d1.clear("Login")

d1.push("Expenses", 
        [('User1', 'Lody', 4),
         ('User1', 'Zakupy', 120),
         ('User2', 'Samochod', 90000),
         ])

d1.push("Login", [("User1", "Haslo123")])

q = "SELECT * FROM Login"
for i in d1.query(q):
    print(i[0], i[1])


reg = Register(d1)
lg = Login(d1, reg)
lg.login_view()



