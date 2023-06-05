import csv
import os
from pathlib import Path

os.makedirs(Path.home() / Path('OneDrive',
            'Desktop', 'CSV Files'), exist_ok=True)

for csvFile in os.listdir(Path.home() / Path('OneDrive', 'Desktop', 'CSV Files')):
    if not csvFile.endswith('.csv'):
        continue

    print('Removing Header From' + csvFile + '...')

    csvrows = []

    csvFileObj = open(Path.home() / Path('OneDrive',
                      'Desktop', 'CSV Files') / csvFile)
    readerObj = csv.reader(csvFileObj)

    for row in readerObj:
        if readerObj.line_num == 1:
            continue
        csvrows.append(row)

    csvFileObj = open(Path.home() / Path('OneDrive', 'Desktop',
                      'CSV Files') / csvFile, 'w', newline='')
    writerObj = csv.writer(csvFileObj)

    for row in csvrows:
        writerObj.writerow(row)

    csvFileObj.close()
