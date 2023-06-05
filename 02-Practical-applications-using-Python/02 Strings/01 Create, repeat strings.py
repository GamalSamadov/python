"""
Create, concatinate and repeat strings
"""

stringOne = 'This is string one'
stringTwo = "This is string two"

print(stringOne)
print(stringTwo)

stringThree = "This is string \"Three\""
print(stringThree)

stringThree = 'This is string "Three"'
stringThree = 'This is string "Three"'
print(stringThree)

numbers = '1\n2\n3'
print(numbers)

numbers = """1
2
3"""

print(numbers)

# Concatination
print(stringOne + stringTwo)
print(stringOne + " " + stringTwo)

# Repeat
print(stringOne * 5)
