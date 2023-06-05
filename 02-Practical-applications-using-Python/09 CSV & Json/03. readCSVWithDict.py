"""
The constructor of the DictReader() class creates an object that acts as a regular file reader, but associates the information on each line with an OrderedDict.
The constructor of the DictWriter() class creates an object that acts as a regular file writer, but associates dictionaries with lines in the CSV file.
The DictWriter.writeheader() method can be used to write headers for fields.

"""

import csv
from pathlib import Path

pth = Path.home() / Path('OneDrive', 'Desktop', 'Curces', 'Hsoub Academy', 'The Code',
                         '02 Practical applications using Python', '09 CSV & Json', 'csvFiles', 'employees_3.csv')

file = open(pth)
dictReader = csv.DictReader(file)

for row in dictReader:
    print(row['Name'], row['Salary'], row['Date'])
