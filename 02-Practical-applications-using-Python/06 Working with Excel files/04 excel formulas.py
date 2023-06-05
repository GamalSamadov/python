import openpyxl
from pathlib import Path
import os

print(os.getcwd())
excelfile = openpyxl.load_workbook(Path.home()/Path('OneDrive', 'Desktop', 'Curces', 'Hsoub Academy', 'The Code', '02 Practical applications using Python', '06 Working with Excel files', 'example.xlsx'))
sheet = excelfile['Sheet1']

sheet['B7'] = '=SUM(B1:B6)'
sheet['B7'] = '=average(B1:B6)'
sheet['B7'] = '=COUNTIF(B1:B6, ">750")'

excelfile.save(Path.home()/Path('OneDrive', 'Desktop', 'Curces', 'Hsoub Academy', 'The Code', '02 Practical applications using Python', '06 Working with Excel files', 'example.xlsx'))
