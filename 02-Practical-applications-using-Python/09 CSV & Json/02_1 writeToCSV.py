"""
The reader() function is used to read CSV files.
The writer() function is used to write CSV files.
The delimiter property is used to determine the separator between fields.
The lineterminator property is used to specify the line break.

"""

import csv
from pathlib import Path

# # Add multiple lines
header = ['Name', 'Salary', 'Date']
data = [
    ['Ahmad', '1000', '19/06/2021'],
    ['Sara', '800', '16/08/2021'],
    ['Reem', '400', '25/02/2020'],
    ['Yara', '750', '09/07/2020'],
    ['Anas', '1200', '19/06/2019']
]

pth = Path.home() / Path('OneDrive', 'Desktop', 'Curces', 'Hsoub Academy', 'The Code',
                         '02 Practical applications using Python', '09 CSV & Json', 'csvFiles', 'employees_New.csv')

# file = open(pth, 'w', newline='')
# writer = csv.writer(file)
# writer.writerow(header)
# writer.writerows(data)
# file.close()

# Delimeter and lineterminator Keyword
file = open(pth, 'w', newline='')
writer = csv.writer(file, delimiter='\t', lineterminator='\n-------------------------\n')
writer.writerow(header)
writer.writerows(data)
file.close()