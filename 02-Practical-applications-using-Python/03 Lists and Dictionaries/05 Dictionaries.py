"""
--------------------------------------------------
------------------ Dictionaries ------------------
--------------------------------------------------

The items() function returns a new display of dictionary items as (key, value).
The keys() function returns a new view containing all the dictionary keys.
The values() function is used to display the key values of the dictionary.
"""

hadi = {
    'name' : 'Hadi',
    'salary' : 2000,
    'number' : '+998777555777',
    'skills' : ['HTML', 'CSS', 'Botstrap']
}

print(hadi)
print(hadi['skills'])
print(hadi['number'])

print('----------------------------------')
list = ['Cats', 'Mouses', 'Dogs']
myList = ['Dogs', 'Mouses', 'Cats']
print(list == myList)
print(list[0])
print(myList[0])

print('----------------------------------')
dictionary = {
    'name' : 'Zophie',
    'species' : 'Cat',
    'age' : 8
}
myDictionary = {
    'age' : 8,
    'name' : 'Zophie',
    'species' : 'Cat',
}
print(dictionary == myDictionary)
print(dictionary['age'])
print(myDictionary['age'])

print('----------------------------------')

# birthdays = {
#     'hadi' : 'Apr 1',
#     'sara' : 'Dec 12',
#     'yara' : 'Mar 4'
# }
#
# while True:
#     print('\nEnter name: (blank to quit)... ')
#     name = input()
#     if name == '':
#         break
#     if name in birthdays:
#         print(birthdays[name] + ' is the birthday of ' + name)
#     elif name == 'all':
#         for n, b in birthdays.items():
#             print(f'Name: {n}, Birth day: {b}')
#
#     else:
#         print('I do not have information of ' + name)
#         print('What is their birthday?')
#         bday = input()
#         birthdays[name] = bday
#         print('Birthday database updated.')

print('----------------------------------')

print(hadi.keys())
print(hadi.values())
print(hadi.items())


print('----------------------------------')
# get

yara = {
    'frontEnd' : {
        1 : 'HTML',
        2 : 'CSS',
        3 : 'Botstrap'
    },
    'backEnd' : {
        1 : 'PhP',
        2 : 'Node.js'
    }
}
print(yara)
print(yara['frontEnd'])
print(yara['backEnd'])
print(yara['frontEnd'][2])