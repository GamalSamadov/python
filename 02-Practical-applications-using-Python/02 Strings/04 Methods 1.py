"""
--------------------------------------------------
---------- String methods Handling case ----------
--------------------------------------------------

The upper() function converts the characters in the text string to uppercase.
The lower() function converts the characters in the text string to lowercase.
The islower() function checks if the string characters are lowercase.
The isupper() function checks if the string characters are uppercase.
The title() function is used to convert the first words in a string to uppercase.
The capitalize() function returns a copy of the string with the first character converted to uppercase, and the remaining characters to lowercase.
The swapcase() function reverses the case of the characters in the text string.
You can see the rest of the functions used with strings.

More methods:
https://wiki.hsoub.com/Python/str#.D8.A7.D9.84.D8.AF.D9.88.D8.A7.D9.84_.D8.A7.D9.84.D8.AA.D8.A7.D8.A8.D8.B9.D8.A9_.D9.84.D9.84.D9.83.D8.A7.D8.A6.D9.86_str
"""

# upper()
test = 'Hello world!'
print(test.upper())

print('--------------------------------------------------')

# lower()
print(test.lower())

print('--------------------------------------------------')

test = test.upper()
print(test)

print('--------------------------------------------------')

# print('How are you?')
# feeling = input('Type your mind: ').lower()
# if feeling == 'great':
#     print('I am too feeling great!')
# else:
#     print('Hope you enjoy your day')

print('--------------------------------------------------')

# islower() isupper()
test = 'hello world!'
print(test.islower())

test = 'hello world!'
print(test.isupper())

print('--------------------------------------------------')
# title()
txt = 'Welcome to my 2nd world'
print(txt.title())

print('--------------------------------------------------')
# capitalize()
txt = 'welcome to my 2nd world'
print(txt.capitalize())

print('--------------------------------------------------')
# swapcase()
txt = 'Hello My Name Is HANDI'
print(txt.swapcase())
