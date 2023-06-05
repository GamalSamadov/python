"""
List, dictionaries and set comprehensions
"""

numbers = [22, 48, 3, 11, 99, 37, 90, 74, 55, 67, 20]

## -- Append the item that bigger then 30 to the new list --
my_numbers = [number for number in numbers if number > 30]
# for number in numbers:
#     if number > 30:
#         my_numbers.append(number)
print(my_numbers)

# get squares
squares = [i ** 2 for i in range(10)]
print(squares)

# Change the item that bigger then 100 to 100
percentages = [85, 90, 102, 101, 58, 77, 103, 100, 99]
new_percentages = [i if i <= 100 else 100 for i in percentages]
print(new_percentages)

# Dictionariy comprehensions
numbers = {i: i ** 2 for i in range(10)}
print(numbers)

# Set comprehensions
numbers = [2, 3, 9, 2, 4, 5, 5, 3, 1, 8, 9, 3, 4, 0, 1]
new_numbers = {i for i in numbers}
print(new_numbers)

# comprehensions in comprehensions
matrix = [[i for i in range(5)] for j in range(6)]
print(matrix)
numbers = [2, 5, 3, 1, 4]
result = 1
for number in numbers:
    result = number * result
print(result)
