'''
--------------------------------------------------
------------- Functional Programming -------------
--------------------------------------------------

Hight-Order Functions ==> are the functions that there arguments are functions too like, map(), filter(), reduce()
map() ==> (function, iterable), does the function for each of items on the iterable object
filter() ==> (function, iterable),

'''
from functools import reduce

# map()
numbers = [1, 2, 3, 4, 5]


def get_squares(number):
    return number ** 2


squares = map(get_squares, numbers)
print(list(squares))

squares_lambda = map(lambda number: number ** 2, numbers)
print(list(squares_lambda))
#
#
# Get F from C
temps = [('Damascus', 29), ('Cairo', 36), ('Baghdad', 44), ('Riyadh', 40), ('Beirut', 34),
         ('Tunis', 30)]  # F = 1.8*C + 32


# V1 Using function
def c_To_f(item):
    return (item[0], (1.8) * item[1] + 32)


f_temp = list(map(c_To_f, temps))
print(f_temp)

# V2 Using lambda function
f_temp_lambda = list(map(lambda item: (item[0], (1.8) * item[1] + 32), temps))
print(f_temp_lambda)

# V3 Imperative programming
f_temps = []
for temp in temps:
    f = (1.8) * temp[1] + 32
    f_temps.append((temp[0], f))
print(f_temps)
#
#
#
#
#
# filter()

languages = [('C', 1972), ('C++', 1985), ('Java', 1995), ('JavaScript', 1995), ('PHP', 1994), ('Python', 1991)]


# Get old languages
def old(item):
    return item[1] < 1990


old_languages = filter(old, languages)
print(list(old_languages))


# Get startswith objects
def find(iterable, text):
    def finder(lang):
        for i in lang:
            if str(i).startswith(text):
                return True
            return False

    return list(filter(finder, iterable))


results = find(languages, 'J')
print(results)

results = find(languages, 'P')
print(results)

results = find(languages, 'Python')
print(results)
#
#
#
#
#
# reduce()

numbers = [1, 2, 3, 4, 5, 6]


def add(x, y):
    return x + y


print(reduce(add, numbers))
print(sum(numbers))

numbers = [31, 51, 94, 11, 40, 83]

max_numbers = reduce(lambda x, y: x if x > y else y, numbers)
print(max_numbers)
print(max(numbers))