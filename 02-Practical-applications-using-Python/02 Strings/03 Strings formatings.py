"""
--------------------------------------------------
--------------- Strings formatings ---------------
--------------------------------------------------



more information format():
https://wiki.hsoub.com/Python/format
"""

name = 'Jamal'
age = 22

print('Hello, my name is: ' + name + ". I am " + str(age) + ' years old.')
print('Hello, my name is: %s. I am %d years old.' % (name, age))

rank = 9.0

print('Hello, my name is: %s. I am %d years old. My rank is: %.2f' % (name, age, rank))

print('----------------------str.format------------------------')

print('My name is: {}. I am {} years old.'.format(name, age))
print('My name is: {:s}. I am {:d} years old. My rank is: {:.3f}'.format(name, age, rank))
print('My name is: {1}. I am {0} years old.'.format(age, name))
print('My name is: {name_key}. I am {age_key} years old.'.format(name_key = name, age_key = age))

print('----------------------f-strings------------------------')
print(f'My name is: {name}. I am {age} years old.')
print(f'My name is: {name}. On the next year my age will be {age+1} years old.')