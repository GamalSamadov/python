"""
--------------------------------------------------
-------------- Errors And Exeptions --------------
--------------------------------------------------

Defrence between Errors and Exeptions:
Error ==> happenes on the compiling time and stopes the compiling, like a Syntax Error or, Out Of Memory Error, RecursionError
Exeption ==> Happenes on the running of code time.
Exeptin ==> is a class and other all exeptions inheritences from the base Exeption class


Exception hierarchy:
https://docs.python.org/3/library/exceptions.html#exception-hierarchy

For more information:
https://wiki.hsoub.com/Python/exceptions
"""

try:
    raise Exception('This is a exeption')
except:
    print('Exept')

try:
    x = 3
    y = 3
    print(x/(x-y))
except:
    print('Did you Divide by Zero?')

print()
try:
    with open('my_file.txt', 'w') as f:
        x = 3
        y = 3

        result = (x+y) / (x-y)

        f.write(f'The result is: {result}')
except FileNotFoundError as error:
    print(error)
except ZeroDivisionError as error:
    print(error)
else:
    print('The resulf was written to the file')
finally:
    print('Code escution was finished')

print('-'*50)
print('-'*50)
print('-'*50)

class TooYoungError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class TooOldError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

def set_age(age):
    try:
        if age < 15:
            raise TooYoungError(f'Sorry, but you are {age} years old. You are too young to sing in')
        elif age > 40:
            raise TooOldError(f'Sorry, but you are {age} years old. You are too old to sing in')
    except TooOldError as error:
        return error
    except TooYoungError as error:
        return error

age = int(input('Enter Your Age: '))
print(set_age(age))