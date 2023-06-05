"""
--------------------------------------------------
--------------- Range and slicing ----------------
--------------------------------------------------
range() ==> returns immutable object
"""

my_slice = range(5)
print(my_slice[3])

try:
    print(my_slice[20])
except IndexError:
    print('IndexError: range object index out of range')

try:
    my_slice[2] = 20
except TypeError:
    print(f"TypeError: 'range' object does not support item assignment")
print(my_slice)


name = 'Hsoup Academy'
hsoup = name[:5]

materials = ['Iron', 'Copper', 'Silver', 'Nickel', 'Gold']
# print(materials[2:5]) # ['Silver', 'Nickel', 'Gold']
print(materials[:4])
print(materials[:])
print(materials[-3:])
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[0:7:2])
print(numbers[7:0:-2])
print(numbers[20:30])  # Dons't return error just empty
print(numbers[:])  # From begin to the end
print(numbers[::-1])  # Reverse
try:
    numbers[0:3] = 600
    print(numbers)
except TypeError:
    print(f'TypeError: can only assign an iterable')
# numbers[0:3] = '600'
# print(numbers)
# numbers[0:3] = '6'
# print(numbers)
# numbers[0:3] = '6000'
# print(numbers)
numbers[0:3] = [100, 100, 100]
print(numbers)

numbers[0:3] = ()
print(numbers)

numbers[0] = []
print(numbers)

numbers[:] = []
print(numbers)
