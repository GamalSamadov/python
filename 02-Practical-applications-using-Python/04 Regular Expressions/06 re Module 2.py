import re

# sub
string = 'Hello my number is 444-444-4444\nMy friend\'s number is: 555-555-5555'

replace = re.sub(r'\d{3}-\d{3}-\d{4}', '000-000-000', string, 1)

print(replace)

print('---------------------------------')

txt = 'I am a student at Hsoub Academy'
replace = re.sub(r'Hsoub\sAcademy', 'Hsoub-Academy', txt)
print(replace)

print('---------------------------------')
# split

search = re.split(r'\s', txt)
print(search)

search = re.split(r'\s', txt, 4)
print(search)

link = 'https://academy.hsoub.com/courses/python-application-development/python-apps/regular-expressions/06-%D8%A7%D8%B3%D8%AA%D8%A8%D8%AF%D8%A7%D9%84-%D9%88%D8%AA%D9%82%D8%B7%D9%8A%D8%B9-%D8%A7%D9%84%D9%86%D8%B5%D9%88%D8%B5-%D8%B9%D8%A8%D8%B1-%D8%AF%D9%88%D8%A7%D9%84-%D8%A7%D9%84%D9%88%D8%AD%D8%AF%D8%A9-re-r3789/'

search = re.sub(r'-', ' ', link)
print(search)

search_two = re.split(r'-', link)
print(search_two)
print(' '.join(search_two ))