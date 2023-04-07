import sqlite3
conn = sqlite3.connect('people.db')
c = conn.cursor()
c.execute("DELETE FROM people WHERE age=25")
conn.commit()
conn.close()
