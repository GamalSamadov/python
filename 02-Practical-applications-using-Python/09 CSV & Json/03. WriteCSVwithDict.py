"""
The constructor of the DictReader() class creates an object that acts as a regular file reader, but associates the information on each line with an OrderedDict.
The constructor of the DictWriter() class creates an object that acts as a regular file writer, but associates dictionaries with lines in the CSV file.
The DictWriter.writeheader() method can be used to write headers for fields.

"""

import csv
from pathlib import Path


pth = Path.home() / Path('OneDrive', 'Desktop', 'Curces', 'Hsoub Academy', 'The Code',
                         '02 Practical applications using Python', '09 CSV & Json', 'csvFiles', 'employees_Test.csv')

file = open(pth, 'w', newline='')
dictWriter = csv.DictWriter(file, ['Name', 'Salary', 'Date'], delimiter=',')
dictWriter.writeheader()
dictWriter.writerow({
    'Name': 'Ahmad',
    'Salary': '850',
    'Date': '07/05/2020'
})
dictWriter.writerow({
    'Salary': '850',
    'Name': 'Ahmad',
    'Date': '07/05/2020'
})

file.close()
