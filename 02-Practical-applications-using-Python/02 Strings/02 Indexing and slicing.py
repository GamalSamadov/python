"""

For more information:
String: https://wiki.hsoub.com/Python/str#.D8.A7.D9.82.D8.AA.D8.B7.D8.A7.D8.B9_.D8.A7.D9.84.D8.B3.D9.84.D8.B3.D9.84.D8.A9_.D8.A7.D9.84.D9.86.D8.B5.D9.8A.D8.A9
"""

stringOne = 'This is string one'

# indexing
print(stringOne[0])
print(stringOne[12])
print(stringOne[17])
print(stringOne[-1])
print(stringOne[-2])

print('-' * 50)

# Slicing[start:end:step]
print(stringOne[5:14])
print(stringOne[:14])
print(stringOne[5:])
print(stringOne[:])
print(stringOne[:-4])
print(stringOne[-13:-4])

print('-' * 50)

# Steps
print(stringOne[0:17:1])
print(stringOne[::1])
print(stringOne[::2])
print(stringOne[::-1])