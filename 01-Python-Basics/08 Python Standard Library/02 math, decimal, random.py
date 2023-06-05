"""
--------------------------------------------------
------------- Math, Decimal, Random --------------
--------------------------------------------------

Math:
The gcd() function returns the greatest common divisor of the given numbers.
The lcm() function returns the least common multiple of the given numbers.
The floor() function returns the nearest integer less than or equal to the given number.
The ceill() function returns the nearest integer greater than or equal to the given number.
The round() function returns the value of the given number rounded by the number of digits as an rounding after the comma.
The exp() function returns the value of e raised to the power of the given number.
The log() function returns the logarithm of the given number.
The pow() function is used to raise the base x to the y power of the two values passed to it.
The sqrt() function returns the square root of the given number.

Decimal:
The Decimal() function returns an object of class Decimal to represent the value given to it.
The max() function returns the largest element of the given iterator.
The min() function returns the smallest element of the given iterator.

Random:
The random() function is used to generate a random real number from the domain [0.0, 1.0).
The randint() function is used to generate a random integer from the given domain.
The randrange() function is used to create a specified range and choose a random number from it.
The choice() function returns a random element of the sequence (a string, an array, etc.).

More information between Decimal:
https://wiki.hsoub.com/Python/decimal
"""
import random
import decimal
import math

#
#
#
# math
#
# greates common divisor
print(math.gcd(4, 6, 14, 20))
print(math.lcm(4, 6, 14, 20))

# floor, ceil, round
print(math.floor(4.6))
print(math.ceil(4.1))
print(round(4.9))
print(round(4.5))

# return reised to the power
print(math.exp(2.4))

# logarithm of the given number.
print(math.log(1000))
print(math.log(1000, 10))
print(math.log10(1000))

# reised to the power
print(math.pow(2, 2))  # Returns float
print(2**3)  # Returns integer

# square root
print(math.sqrt(144))

print(math.pi)
print(math.e)
#
#
#
# decimal
#
print(1.1+2.2)
print(0.1 + 0.1 + 0.1 == 0.3)
print(0.1 + 0.1 + 0.1 - 0.3)


print(decimal.getcontext())

decimal1 = decimal.Decimal(3)

decimal2 = decimal.Decimal('3.14')

decimal3 = decimal.Decimal(2/4)

print(decimal1)
print(decimal2)
print(decimal3)
print(2/4)
print(decimal1 + decimal2)
print(decimal2 - decimal2)

decimals = [decimal1, decimal2, decimal3]

print()
print(sum(decimals))
print(max(decimals))
print(min(decimals))
#
#
#
#
# Random
print(random.random())  # random float
print(random.random())
print(random.random())
print(random.random())
print(random.random())

print(random.randint(1, 10))  # random integer
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print()

print(random.randrange(10))  # random in range
print(random.randrange(10))
print(random.randrange(10))
print(random.randrange(10))
print(random.randrange(10))
print(random.randrange(10))

names = ['Sara', 'Nada', 'Tawfeek', 'Mohsen', 'Jalal', 'Saeed', 'Zohoor']

print(random.choice(names))  # random item
print(random.choices(names, k=3))  # Random items

print(names)
random.shuffle(names)
print(names)
