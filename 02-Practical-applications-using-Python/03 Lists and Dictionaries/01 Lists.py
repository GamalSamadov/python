"""
--------------------------------------------------
--------------------- Lists ----------------------
--------------------------------------------------

The choice() function returns a random element from the iterable list or object.
The shuffle() function shuffles the elements of the list or iterable object.

"""

employees = ['Hasan', 'Hadi', 'Reem', 'Ahmad']

print(employees[0])
print(employees[2])
print(employees[3])
print(employees[-1])
print(employees[-3])
# print(employees[50])

print(employees[1:3])
print(employees[:3])
print(employees[1:])
print(employees[0:4:1])
print(employees[::1])
print(employees[::2])

print(employees)

employees[1] = 'Sara'
print(employees)

employees[-1] = 'Yara'
print(employees)

employees[0:2] = 'Hadi', 'Salwa'
print(employees)

employees[0:2] = ''
print(employees)

print('--------------------------------------------------')
# For loop
employees = ['Hasan', 'Hadi', 'Reem', 'Ahmad']

for i in range(4):
    print(employees[i])

for i in range(len(employees)):
    print(employees[i])

for i in range(len(employees)):
    print(f'Index {i} in employees is: {employees[i]}')

print('--------------------------------------------------')
# enumirate()

for index, item in enumerate(employees, 1):
    print(f'Index {index} in employees is: {item}')

print('--------------------------------------------------')
# in, not in

print('Hadi' in employees)
print('Hadi' not in employees)

# name = input('Enter the name: ')
# if name in employees:
#     print(f'{name}\'s works in our company')
# else:
#     print('Cannot find')
#
print('--------------------------------------------------')
# choise and shuttle
import random
print(random.choice(employees))
print(random.choice(employees))
print(random.choice(employees))

random.shuffle(employees)
print(employees)