"""
--------------------------------------------------
------------ Iterators And Generators ------------
--------------------------------------------------
iter() ==> iterates the given object
next() ==> shows iteration one by one and gives error StopIteration if the itaration done
Generators ==> creates iteration by the easy way
yield ==> creates generator and pauses it and starts from the paused place if it'll be callen second time, while the return ==> stops the function
Function creates the iteration in the memory complately and if the iteration is very big then the function can's make a problem, while the generators creats the iteration one by one.
Generatos can's create a infenity iterations while the function makes a problem
For more information:
https://academy.hsoub.com/questions/15874-%D8%B5%D9%86%D8%A7%D8%B9%D8%A9-%D9%83%D8%A7%D8%A6%D9%86-%D9%82%D8%A7%D8%A8%D9%84-%D9%84%D9%84%D8%AA%D9%83%D8%B1%D8%A7%D8%B1-iterator-%D9%81%D9%8A-%D8%A8%D8%A7%D9%8A%D8%AB%D9%88%D9%86/
"""

x = iter(['a', 'b', 'c'])
print(x)  # <list_iterator object at 0x000001D0816063E0>
print(next(x))  # a
print(next(x))  # b
print(next(x))  # c

print('-' * 50)
print(' Iterators And Generators '.center(50, '-'))
print('-' * 50)


def my_generator():
    i = 0
    print('First value')
    yield i
    i += 1
    print('Second value')
    yield i
    i += 1
    print('Third value')
    yield i


my_gen = my_generator()
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
#
#
#
# Piplining

# V1
def odd_numbers(numbers):
    for num in range(1, numbers, 2):
        yield num

def square(nums):
    for num in nums:
        yield num ** 2


print(sum(square(odd_numbers(10))))

# V2
odd_numbers_v = (num for num in range(1, 10, 2))
square_v = (i ** 2 for i in odd_numbers_v)
print(sum(square_v))

# V3
result = sum(i ** 2 for i in (x for x in range(1, 10, 2)))
print(result)
