"""
------------------------------------------------------------------------------
------String methods Adding and deleting characters from the text string------
------------------------------------------------------------------------------
The startswith() function verifies that the string starts with the value specified by the user.
The endswith() function checks if there is a substring at the end of the original string.
The strip() function removes user-defined characters from the end and beginning of a string.
The rstrip() function removes user-defined characters from the end of the string.
The zfill() function adds zeros to the left of the text string.

"""

# startswith() endswith()
test = 'Hello world'
print(test.startswith('H'))
print(test.startswith('h'))
print(test.endswith('d'))

print(test.startswith('w',6))

print('--------------------------------------------------')
# strip() lstrip() rstrip()
test = '     Hello world     '
print(test)
print(test.strip())
print(test.lstrip())
print(test.rstrip())

test = '@@@@Hello world@@@@@@@'
print(test)
print(test.strip('@'))
print(test.lstrip('@'))
print(test.rstrip('@'))

test = '@#@#@#Hello world@#@#@#@#'
print(test)
print(test.strip('@#'))
print(test.lstrip('@#'))
print(test.rstrip('@#'))

print('--------------------------------------------------')
# zfill()
hours = '1'
min = '9'
seconds = '5'
print(f'{hours}:{min}:{seconds}')
print(f'{hours.zfill(2)}:{min.zfill(2)}:{seconds.zfill(2)}')
print(f'{hours.zfill(3)}:{min.zfill(3)}:{seconds.zfill(3)}')

hours = '1'
min = '19'
seconds = '15'
print(f'{hours.zfill(2)}:{min.zfill(2)}:{seconds.zfill(2)}')
print(f'{hours.zfill(3)}:{min.zfill(3)}:{seconds.zfill(3)}')