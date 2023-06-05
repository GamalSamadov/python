"""
--------------------------------------------------
------------------String -----------------------
--------------------------------------------------
Can type string with (' ') or (" ") or (\""" \""")
String ==> immutable object. Can not change it and dosn't support assignment
len() ==> get lenght of string and list and tuple and more...
capitalize() ==> make first word of string capitale and small others
endswith('value') ==> Gives True if the string ends with the given value or False if dosn't
startswith('value') ==> Gives True if the string srarts with the given value or False if dosn't
find('value') ==> Gines index of given value and does nothing if didn't find the value in string
index('value') ==> Gines index of given value and does ValueError if didn't find the value in string
join() ==> joins list like this: new_str = ', '.join(list)
format() ==> format the string

More string methods:
https://wiki.hsoub.com/Python/str#.D8.A7.D9.84.D8.AF.D9.88.D8.A7.D9.84_.D8.A7.D9.84.D8.AA.D8.A7.D8.A8.D8.B9.D8.A9_.D9.84.D9.84.D9.83.D8.A7.D8.A6.D9.86_str
"""


name = 'Hsoub Academy'
try:
    name[0] = 'i'
except TypeError:
    print('TypeError: \'str\' object does not support item assignment. Because it is immmutable object')

print('Hsoub' in name)
print('H' in name)
print('h' in name)

print(name.capitalize())
print(name.endswith('emy'))  # return True or False
print(name.startswith('emy'))  # return True or False
print(name.find('o'))  # Return index if find
print(name.find('x'))  # Return -1 id dosn't find
print(name.index('A'))  # Return index if found
try:
    print(name.index('x'))
except ValueError:
    print('ValueError: substring not found')  # Return ValueError if not found

names = ['Mohamed', 'Ahmed', 'Tawfeek', 'Suhad']
sep_names = ', '.join(names)  # Joins items of list together
print(sep_names)
print(', '.join(names))

greet = 'Hello {}'
print(greet.format('Ahmad'))