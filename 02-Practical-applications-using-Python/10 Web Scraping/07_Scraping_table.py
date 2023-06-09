import bs4
import requests
import csv
from pathlib import Path

res = requests.get('https://en.wikipedia.org/wiki/List_of_languages_by_number_of_native_speakers')
# print(res.text)

soup = bs4.BeautifulSoup(res.text, 'html.parser')

# select table
table_soup = soup.find_all('table')
filtered_tables = [table for table in table_soup if table.caption is not None]
# print(filtered_tables)

required_table = None

for table in filtered_tables:
    if str(table.caption.text).strip() == 'Top languages by population per Nationalencyklopedin':
        required_table = table
        break

# print(required_table.text)

rows = required_table.find_all('tr')
# print(rows)
headers = [head.text.replace('\n','') for head in rows[0].find_all('th')]
# print(headers)

data = []
for row_data in rows:
    value = row_data.find_all('td')
    value_text = [db.text.strip() for db in value]

    if len(value_text) == 0:
        continue

    data.append(value_text)
    # print(value_text)

# CSV Write
pth = Path.home() / Path('OneDrive', 'Desktop', 'Curces', 'Hsoub Academy', 'The Code', '02 Practical applications using Python', '10 Web Scraping')
file = open(pth / 'wepSctapingTable.csv', 'w', newline='')
writer = csv.writer(file)
writer.writerow(headers)
writer.writerows(data)
file.close()