import sqlite3

connection = sqlite3.connect("record.db")
c = connection.cursor()
# c.execute('''
# CREATE TABLE record(
# Name varchar(255) NOT NULL,
# Last varchar(255)
# );''')


# c.execute('''INSERT INTO record(Name, Last) VALUES('re', 'fe');''')
# c.execute('''INSERT INTO record(Name, Last) VALUES('Mummy', 'fe');''')
# c.execute('''INSERT INTO record(Name, Last) VALUES('rie', 'nice');''')
# connection.commit()

c.execute("SELECT * FROM record WHERE Last LIKE '%f';")
for item in c.fetchall():
    print(item)

connection.commit()