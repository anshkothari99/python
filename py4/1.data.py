import sqlite3

# Establishing a connection to the SQLite database
conn = sqlite3.connect('college.db')
c = conn.cursor()

# Creating the institutes table with columns id, college_name, principal, contact
c.execute('''CREATE TABLE institutes (id INTEGER PRIMARY KEY AUTOINCREMENT, college_name CHAR(50), principal CHAR(50), contact CHAR(50))''')

# Inserting 5 entries into the institutes table
data = [('ABC College', 'Dr. John Doe', '1234567890'),
        ('XYZ College', 'Dr. Jane Doe', '0987654321'),
        ('DEF College', 'Dr. Mary Smith', '1112223333'),
        ('GHI College', 'Dr. Bob Johnson', '4445556666'),
        ('JKL College', 'Dr. Susan Lee', '7778889999')]

for entry in data:
    c.execute('''INSERT INTO institutes (college_name, principal, contact) VALUES (?, ?, ?)''', entry)

# Adding a new column called address to the institutes table
c.execute('''ALTER TABLE institutes ADD COLUMN address VARCHAR(255)''')

# Dropping the contact column from the institutes table
#c.execute('''ALTER TABLE institutes DROP COLUMN contact''')

# Modifying the college_name column from char to varchar
c.execute('''ALTER TABLE institutes RENAME TO institutes_old''')
c.execute('''CREATE TABLE institutes (id INTEGER PRIMARY KEY AUTOINCREMENT, college_name VARCHAR(50), principal CHAR(50), contact VARCHAR(50) )''')
c.execute('''INSERT INTO institutes (id, college_name, principal, contact) SELECT id, college_name, principal , contact FROM institutes_old''')
c.execute('''DROP TABLE institutes_old''')

# Updating the contact of Dr. H.H. Shinde to 9028885925
c.execute('''UPDATE institutes SET contact = '9028885925' WHERE principal = 'Dr. H.H. Shinde' ''')

# Deleting the College of Engineering from the institutes table
c.execute('''DELETE FROM institutes WHERE college_name = 'College of Engineering' ''')

# Truncating the institutes table
c.execute('''DELETE FROM institutes''')

# Dropping the institutes table
c.execute('''DROP TABLE institutes''')

# Committing the changes and closing the connection
conn.commit()
conn.close()
