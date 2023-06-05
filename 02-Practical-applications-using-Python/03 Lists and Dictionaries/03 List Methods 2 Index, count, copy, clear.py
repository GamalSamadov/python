"""
----------------------------------------------------------------------
-------------  List Methods  Index, count, copy, clear ---------------
----------------------------------------------------------------------

The index() function locates an item within the list.
The count() function determines the number of times an item in the list is repeated.
The copy() function returns a copy of the list.
The clear() function clears all list items.
"""

# index()
employees = ['Hasan', 'Hadi', 'Reem', 'Ahmad', 'Hadi']
print(employees.index('Hadi'))
# print(employees.index('Sara'))

print('--------------------------------------------------')
# Count()
print(employees.count('Hadi'))
print(employees.count('Reem'))

print('--------------------------------------------------')
# copy()
test = employees.copy()
print(employees)
print(test)

print('--------------------------------------------------')
# clear()

test.clear()
print(test)

