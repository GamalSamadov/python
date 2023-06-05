"""
enumerate() ==> returns an iterable object of type enumerate. It is used to number repeatable objects.
"""
employees = ['Ahmed Waleed', 'Suzan Muhsen', 'Maha Saleem', 'Jaber Mansoor']

print('Employees: ')
print('-' * 9)
for count, value in enumerate(employees, start=1):
    print(count, value)

print()
print('Employees: ')
print('-' * 9)
index = 0
while index < len(employees):
    print(index + 1, employees[index])
    index += 1


print('-' * 50)
print('-' * 50)
print('-' * 50)
print('-' * 50)



