
import sqlite3
from pathlib import Path as pth

path = pth.home() / pth('OneDrive', 'Desktop', 'Curces', 'Hsoub Academy',
                        'The Code', '02 Practical applications using Python', '11 Data Base')
sqLiteConnection = sqlite3.connect(path / 'DataBaseEmployees.db')
crsr = sqLiteConnection.cursor()
print('Connected to the data base...')

# Updating
crsr.execute("UPDATE employees SET Salary = 600 WHERE id=6")
print('The data Updated!')


# Deleting
crsr.execute('DELETE FROM employees WHERE id=3')


sqLiteConnection.commit()
sqLiteConnection.close()