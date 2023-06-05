

import sqlite3
from pathlib import Path as pth

path = pth.home() / pth('OneDrive', 'Desktop', 'Curces', 'Hsoub Academy',
                        'The Code', '02 Practical applications using Python', '11 Data Base')
sqLiteConnection = sqlite3.connect(path / 'DataBaseEmployees.db')
crsr = sqLiteConnection.cursor()
print('Connected to the data base...')

crsr.execute(
    'SELECT name, salary, dateOfEmployment FROM employees where salary > 850')
# print(crsr.fetchall())
# print(crsr.fetchone())
# print(crsr.fetchmany(3))

answer = crsr.fetchall()

for i in answer:
    print(i)


# TEST:
# Fetch the students info from db and save it into a exel file


for num in [1,2,3,4,5]:
    print(num)
