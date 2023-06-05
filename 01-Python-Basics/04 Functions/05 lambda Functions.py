"""
--------------------------------------------------
--------------------- Lambda ---------------------
--------------------------------------------------
Alonco Church ==> made Functional Programming
Alan Turing ==> made imperative Programming

Python supports functional programming paradigm
one of the functional programming paradigms is lamda function

Lambda ==> anonymous function but in python we can use variables lika a name for lambda function

Defference between lambda function and function:
- Lambda has not an statements like return, pass, gives 'SyntaxError: invalid syntax'
- lambda is oneline code
- lambda dosn't support Annotations gives error: 'SyntaxError: invalid syntax' like statements
- lambda is immediately invoked function exception (ife) can use it on the fly into hight functions like map(), filter() and more...
- lambda supports posissional arguments ang keyword arguments

For more informations:
https://wiki.hsoub.com/Python/lambda_expressions
"""


def my_function(a):
    return a


print((lambda a: a + 2)(2))

add_two = lambda a: a + 2
print(add_two(2))

add = lambda a, b: a + b
print(add(100, 300))

student_name = lambda first_name, last_name: f"Student's name: {first_name.title()} {last_name.title()}"
print(student_name('Ahmed', 'sayeed'))

## dosn't support statements
# print(lambda a: return a + 1)

a = (lambda a, b: a + b)
b = (lambda a, b=0: a + b)
c = (lambda *args: sum(args))
d = (lambda **kwargs: sum(kwargs.values()))
print(a(a=1, b=2))
print(b(1))
print(c(100, 200, 300))
print(d(a=100, b=200, c=300))
#
#
# Using lambda like key
ids = ['id1', 'id100', 'id2', 'id22', 'id4', 'id40']

# def sotr_key(x):
#     return x[2:]
# ids.sort(key = sotr_key)

ids.sort(key= lambda x: int(x[2:]))
print(ids)