from db_demo import DataBase as db

d1 = db()

d1.clear()

d1.push([('User1', 'Haslo1', 'Wydatek1', 'Przychod1'),
         ('User2', 'Haslo2', 'Wydatek1', 'Przychod1'),
         ('User3', 'Haslo3', 'Wydatek1', 'Przychod1'),
         ('User4', 'Haslo3', 'Wydatek1', 'Przychod1')
         ])

for i in d1.pull_rows():
    print(i)