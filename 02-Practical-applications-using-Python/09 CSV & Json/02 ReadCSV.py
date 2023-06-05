"""
The reader() function is used to read CSV files.
The writer() function is used to write CSV files.
The delimiter property is used to determine the separator between fields.
The lineterminator property is used to specify the line break.

"""

import csv
from pathlib import Path

pth = Path.home() / Path('OneDrive', 'Desktop', 'Curces', 'Hsoub Academy', 'The Code',
                         '02 Practical applications using Python', '09 CSV & Json', 'csvFiles', 'employees_1.csv')

file = open(pth)

reader = csv.reader(file)

# data = list(reader)
#
# print(data)
# print(data[1][0])
# print(data[1][1])
# print(data[1][2])

for row in reader:
    print('Row #' + str(reader.line_num) + ' ' + str(row))