print('ansh 033')
import sqlite3

conn = sqlite3.connect('people.db')

c = conn.cursor()

c.execute('''CREATE TABLE people (name text, age integer)''')

while True:
    name = input("Enter name (or type 'done' to exit): ")
    if name == 'done':
        break
    age = int(input("Enter age: "))
    c.execute("INSERT INTO people VALUES (?, ?)", (name, age))

conn.commit()
conn.close()
