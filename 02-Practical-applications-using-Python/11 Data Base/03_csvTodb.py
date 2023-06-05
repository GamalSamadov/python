import csv
import sqlite3
from pathlib import Path as pth

path = pth.home() / pth('OneDrive', 'Desktop', 'Curces', 'Hsoub Academy',
                        'The Code', '02 Practical applications using Python', '11 Data Base')
sqLiteConnection = sqlite3.connect(path / 'DataBaseEmployees.db')
crsr = sqLiteConnection.cursor()
print('Connected to the data base...')

# SQL command to create a table in the data base
sql_command = '''CREATE TABLE if not exists employees (
id INTEGER,
Name VARCHAR(20),
Salary INTEGER,
dateOfEmployment TEXT)'''

crsr.execute(sql_command)

# Read csv file
file = open(path / 'employees.csv')
rows = csv.reader(file)

# add data to db
crsr.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", rows)

sqLiteConnection.commit()
sqLiteConnection.close()


a = 'abcd'

for word in a:
    print(word)
