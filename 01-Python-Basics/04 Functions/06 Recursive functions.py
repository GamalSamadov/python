"""
--------------------------------------------------
--------------- Recursed Fonctions ---------------
--------------------------------------------------

"""


# Loop recursion gives RecursionError:
def recursion():
    print('Recursive Function')
    return recursion()


try:
    recursion()
except RecursionError:
    print('RecursionError: maximum recursion depth exceeded while calling a Python object')
#
#
#
print()
print()
print()


#
#
#
def fact(n):  # n = 5, n = 4, n = 3, n = 2, n = 1
    if n <= 1:  # not works, not works, not works, not works, works
        return 1
    else:
        return n * fact(
            n - 1)  # 5 * fact(5-1=4) = 20, (5*4=20) * fact(5-1-1=3) = 60, (5*4*3*2=60) * fact(5-1-1-1=2) = 120, (5*4*3*2*1=60) * fact(5-1-1-1-1=1) = 120 WILL RETURN => 120


print(fact(5))
print()
print()
#
#
#
#
#
# Printing items of list
books = ['Effictive Python', 'Byte of Python', 'Python Essential Reference', 'Think Python', 'Python Cookbook']


def print_books(list):
    if len(list) == 0:
        return
    else:
        print(list[0])
        return print_books(list[1:])


print_books(books)
#
#
#
#
#
#
print()
print()
print()
#
#
#
#


data = [['Effictive Python', 'Byte of Python', 'Python Essential Reference'], 44, 12, 'Python Cookbook',
        ('Books', 'Wepsites')]
#
# Print using for loop is very hard and not effective
for i in data:
    print(i)
print()


#
# Print using Recursive function is very easy
def print_data(data):
    if not data: return # If the list empty pass it
    if (type(data[0]) == list or type(data[0]) == tuple):
        print_data(data[0])
    else:
        print(data[0])
    print_data(data[1:])


print_data(data)
