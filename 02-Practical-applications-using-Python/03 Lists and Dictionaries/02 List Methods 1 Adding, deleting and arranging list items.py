"""

The append() function adds an element to the end of the list.
The extend() function adds an array of items to the end of the list.
The insert() function adds an element to the list at the location specified by the user.
The del keyword removes objects of any kind (list, string, dictionary, etc.).
The remove() function removes the first item in the list whose value is the value specified by the user.
The pop() function removes the element at the user-specified location.
The Sort() function in Python is used to sort the list in place by comparing the list's elements with only the < operator.
"""

# append(), insert()
employees = ['Hasan', 'Hadi', 'Reem', 'Ahmad']
employees.append('yara')
print(employees)

employees.insert(1, 'sara')
print(employees)

old_employees = ['osama', 'Alaa']
employees.append(old_employees)
print(employees)
print(employees[6])
print(employees[6][0])

print('--------------------------------------------------')
# extend()

employees = ['Hasan', 'Hadi', 'Reem', 'Ahmad']
old_employees = ['osama', 'Alaa']

employees.extend(old_employees)
print(employees)

print('--------------------------------------------------')
# remove()
employees.remove('Reem')
print(employees)

try:
    employees.remove('Anas')
except:
    print('ValueError: list.remove(x): x not in list')

employees = ['Hasan', 'Hadi', 'Hasan', 'Ahmad']
employees.remove('Hasan')
print(employees)

print('--------------------------------------------------')
# del statement

del employees[0]
print(employees)

print('--------------------------------------------------')
# sort()

numbers = [8, 7, 6, 4, 3, 9, 8, -5, -9]
numbers.sort()  # reverse=False by default
print(numbers)

numbers.sort(reverse=True)
print(numbers)

employees = ['Yara', 'Sara', 'Hasan', 'Ahmad']
employees.sort()
print(employees)
try:
    spam = [4, 1, 3, 2, 'Alice', 'Bob']
    spam.sort()
    print(spam)
except:
    print("""TypeError: '<' not supported between instances of 'str' and 'int'""")

print('--------------------------------------------------')
# reverse()

employees = ['Yara', 'Sara', 'Hasan', 'Ahmad']
employees.reverse()
print(employees)
employees.sort(reverse=True)
print(employees)