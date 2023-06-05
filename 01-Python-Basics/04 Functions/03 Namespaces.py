"""
--------------------------------------------------
------------------- Namespaces -------------------
--------------------------------------------------

Python ==> is the dynamic system, that is why python can recognize types of data types by typing name of variable
Local namespace ==> is lockal namespace into function means that can't use it out it's aria. local namespaces gonnna create when it will be callen not when it will be created into function
inclosing namespace ==> is a namespace into function that it's into another function
global namespace ==> is a namespace that is global and can use it enywhere on the code
builtin namespace ==> it's a builtin namespaces like: calss, def, for, while, True, False, and more..

python searchs variables using it's namespaces:
01) Searchs into "Inclosing", if didn't find then searchs into
2) "lockal" if didn't find then searchs into
03 "Global" if didn't find then searchs into
04) "bultin"

For more information:
https://wiki.hsoub.com/Python/scopes-and-namespaces
"""


# Local
def add(x, y):
    # This aria is local namespace
    if x < 0:
        return 0
    return x + y


#
#
# inclosing & Global
#
# This aria is Global
x = 100
y = 200


def get_name():
    first_name = ''
    last_name = ''

    def join_first_last():
        # This aria is inclosing
        print(first_name, last_name)

    join_first_last()


#
#
#
x = 100


def add(y):
    z = x + y
    return z


print(add(20))


def my_function():
    input = 'Name'
    name = input('Enter name: ')


try:
    my_function()
except:
    print('TypeError: \'str\' object is not callable')
#
#
#
#
#
x = 100


def print_number():
    x = 200
    print(x)


# GLobal variable "x" is not readable by this function because it has oun local 'x' variable that has it's oun value
print_number()
#
#
#
#
#
x = 100
def print_number_global():
    global x # convert Lockal or including to global
    print(x)


print_number_global()
#
#
#
#
#
#
def outer():
    x = 100
    def inner():
        x = 300
    inner()
    print(x)
outer()

def outer_nonlocal():
    x = 100
    def inner():
        nonlocal x # convert including to global
        x = 300
    inner()
    print(x)
outer_nonlocal()

x = 0
def outer_global():
    x = 100
    def inner():
        global x # convert including to global
        x = 300
    inner()
    print(x, 'local')
outer_global()
print(x, 'global')
