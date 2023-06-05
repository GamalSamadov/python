"""
--------------------------------------------------
------------ Parametres And Arguments ------------
--------------------------------------------------
Argements ==> Positional, keyword
Positional arguments ==> gets value from tha parametres by there's pozission
Keyword arguments ==> gets value from the key and the key value must be on the end arguments
Paramentres ==> Is mandatory, isn't madnatory
Paramentres ==> 1) The amount of Parametres is known in advance, isn't known
"""


def print_name(name):
    print('Hello', name)


print_name('Jamal')


# def print_info(name, age, weight):
#     print('Name:', name, 'Age:', age, 'Weight:', str(weight) + 'kg')
#
# # Positional
# print_info('Jamal', 22, 1.8)
#
# # Key
# print_info(name='Jamal', age=22, weight=60)
# print_info(age=22, weight=60, name='Jamal') # Arranging items is not required
# print_info('Jamal', age=22, weight=60) # mixing
# # print_info('Jamal', age=22, 60) # SyntaxError: positional argument follows keyword argument
# # print_info('Jamal', 60, age=22) # TypeError: print_info() got multiple values for argument 'age'
# print_info('Jamal', 22, weight=60)
#

def print_info(name, weight, age=40):  # Key arguments must be on the end
    print('Name:', name, 'Age:', age, 'Weight:', str(weight) + 'kg')


print_info(name='Jamal', weight=60)


## -- isn't known amount of parametres --
def print_fruits(*args):  # Name of argument shoud be (*args)
    for fruit in args:
        print('I like the', fruit)


print_fruits('Apple', 'Banana')


def weather(**kwargs):
    print(kwargs)


weather(location='Baghdad', temprature=48, condition='Sunny', wind_speed=3)


### -- Proctess --
def multiple_numbers(number, multiple):
    return f"{number}**{multiple}={number ** multiple}"


# number = int(input('Enter a Number: '))
# multiple = int(input('Enter multi number: '))

number = 1000
multiple = 2

print(multiple_numbers(number, multiple))