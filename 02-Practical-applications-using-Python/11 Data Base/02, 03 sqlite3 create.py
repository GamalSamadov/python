"""
The official documentation for the sqlite3 package:
https://docs.python.org/3/library/sqlite3.html

The connect() function creates a connection object that represents the database.

sqlitebrowser download link:
https://sqlitebrowser.org/dl/

The execute() function executes the command given to it.
The close() function closes the connection to the database.

The commit() function is used to perform transaction.
The executemany() function is used to execute the specified commands.
"""

import sqlite3
from pathlib import Path
import django

pth = Path.home() / Path('OneDrive', 'Desktop', 'Curces', 'Hsoub Academy', 'The Code', '02 Practical applications using Python', '11 Data Base')
sqLiteConnection = sqlite3.connect(pth / 'DataBase.db')
crsr = sqLiteConnection.cursor()
print('Connected to the data base...')

# SQL command to create a table in the data base
sql_command = '''CREATE TABLE if not exists students (
firstname VARCHAR(20), 
lastname VARCHAR(20),
age INTEGER)'''

crsr.execute(sql_command)

# INSERT data
crsr.execute('INSERT INTO students VALUES ("Hadi", "Hasan", 23);')
crsr.execute('INSERT INTO students VALUES ("Yara", "Anas", 26);')
crsr.execute('INSERT INTO students VALUES ("Sara", "Hasan", 30);')

sqLiteConnection.commit()

# close the connection
sqLiteConnection.close()