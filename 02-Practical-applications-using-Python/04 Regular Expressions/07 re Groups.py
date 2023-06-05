# groups

import re

phone = '444-444-4444'

search = re.search(r"(\d{3})-(\d{3}-\d{4})", phone)
print(search.group())
print(search.group(0))
print(search.group(1))
print(search.group(2))

date = '18-07-2022'

search = re.search(r'(\d{2})-(\d{2})-(\d{4})', date)
print(search.group(0))

day = search.group(1)
month = search.group(2)
year = search.group(3)

print(f'The day is: {day}, The month is: {month}, The year is: {year}')

day, month, year = search.groups()
print(f'The day is: {day}, The month is: {month}, The year is: {year}')