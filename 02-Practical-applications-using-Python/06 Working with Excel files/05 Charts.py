"""


more abaut charts on the liberory:
https://openpyxl.readthedocs.io/en/stable/charts/introduction.html
"""

import openpyxl
from pathlib import Path

excelfile = openpyxl.load_workbook(Path.home()/Path('OneDrive', 'Desktop', 'Curces', 'Hsoub Academy', 'The Code', '02 Practical applications using Python', '06 Working with Excel files', 'example2.xlsx'))
sheet = excelfile['Sheet1']

# create charts
title = openpyxl.chart.Reference(sheet, min_col=1, max_col=1, min_row=1, max_row=6)
data = openpyxl.chart.Reference(sheet, min_col=2, max_col=2, min_row=1, max_row=6)
chart = openpyxl.chart.PieChart()

chart.title = 'My chart'
chart.add_data(data=data)
chart.set_categories(title)

sheet.add_chart(chart, 'E8')

excelfile.save(Path.home()/Path('OneDrive', 'Desktop', 'Curces', 'Hsoub Academy', 'The Code', '02 Practical applications using Python', '06 Working with Excel files', 'example2.xlsx'))
