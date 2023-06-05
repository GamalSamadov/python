"""----------------------------------------------
----------------------Tuple---------------------
--------------------------------------------------
tuple ==> iterable object
tuple ==> immutable and not changeble object

more information:
https://wiki.hsoub.com/Python/tuples
"""

tivers = (('Euphrates', 'Tigers'), 'Jordan River', 'Nile')

t = (9)  # this is integer not tuple
print(type(t))

t_2 = (9,) # This is tuple
print(type(t_2))

t_3 = 1, 2, 3, 4, 5, 6, 7, 8, 9  # can type tuple items without ()
print(type(t_3))
print(len(t_3))

print(1 in t_3)
print(2 in t_3)

t = 1, 2, 3, 4
s = 'One', 'Two', 'Three', 'Four'

t = s

print(t)

print(s)


# Changing values of variable each other

a = 3
b = 20

print(a, b)

temp = a

a = b

b = temp

print(a , b)

a = 3
b = 20

print(a, b)

a , b = b, a

print(a , b)
