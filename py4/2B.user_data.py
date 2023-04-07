import sqlite3
conn = sqlite3.connect('people.db')
c = conn.cursor()
c.execute("SELECT * FROM people")
for row in c.fetchall():
    print(row[0], row[1])
conn.close()
