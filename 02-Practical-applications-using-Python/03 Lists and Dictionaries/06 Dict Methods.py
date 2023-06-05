"""
--------------------------------------------------
-------------- Dictionaries Methods---------------
--------------------------------------------------

The get() function returns the value associated with the key specified by the user.
The setdefault() function returns the value of the specified key.
The update() function is used to add and update dictionary items.
"""

# get
hadi = {
    'name' : 'Hadi',
    # 'salary' : 2000,
    'number' : '+998777555777',
    'skills' : ['HTML', 'CSS', 'Botstrap']
}
# print(hadi['name'] + ' Recieves a salary of ' + str(hadi['salary']))
print(hadi['name'] + ' Recieves a salary of ' + str(hadi.get('salary', 'no salary')))

print('---------------------------------------')
# setdefault()
print(hadi)
print(hadi.setdefault('name', 'Sara'))
print(hadi)
print(hadi.setdefault('salary', 2000))
print(hadi)
if 'language' not in hadi:
    hadi['language'] = 'CSS'
print(hadi)

print('---------------------------------------')
# update()
numbers = {1 : 'one', 2 : 'Three'}
print(numbers)
numbers.update({2 : 'Two'})
print(numbers)
numbers.update({3 : 'Three'})
print(numbers)

print('---------------------------------------')
# clear()
print(hadi)
hadi.clear()
print(hadi)
