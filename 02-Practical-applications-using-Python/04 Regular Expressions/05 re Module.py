"""
--------------------------------------------------
------------------- re Module --------------------
--------------------------------------------------

The search() function searches for the first location where a match occurs with the given regular expression, and returns the corresponding match object.
The findall() function returns all matches with the given regular expression.
The group() function returns the string found in the text and stored in the match object.
who summoned her.
The span() method returns a tube that represents the start and end position of the match object that was found.
"""

import re

txt = 'My name is Jamal'

search = re.search("[A-Z]", txt)
print(search)
print(search.span())
print(search.string)
print(search.re)
print(search.group())
print(dir(search))

test = 'Call me at 444-444-4444 and tmorrow at 555-555-5555'

search = re.search(r'\d{3}-\d{3}-\d{4}', test)
print(search)
print(search.group())

print('-----------------------------------')
# findall

string = 'Hello my number is 444-444-4444\nMy friend\'s number is: 555-555-5555'

search = re.findall(r'\d{3}-\d{3}-\d{4}', string)
print(search)

test_search = re.findall(r'A', string)
print(test_search)

# Practical

phone_number = input('Enter the Phone number: ')

search_phone = re.findall(r'\d{3}-\d{3}-\d{4}', phone_number)

list = []

if search_phone == []:
    print('This phone number is not valid')
else:
    list.append(search_phone)
    print('The phone number is added.')
