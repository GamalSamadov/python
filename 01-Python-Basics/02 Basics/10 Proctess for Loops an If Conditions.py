## Task N1
'''
A: 100 - 90
B: 89 - 80
C: 79 - 70
D: 69 - 60
E: 59 - 50
F: 49 - 0
'''
# grade = int(input('Enter the grade: '))
# if grade > 100 or grade < 0:
#     print('The grade is out of range!')
#     exit()
# if grade in range(90, 101):
#     print('Your grade is: A')
# elif grade in range(80, 90):
#     print('Your grade is: B')
# elif grade in range(70, 80):
#     print('Your grade is: C')
# elif grade in range(60, 70):
#     print('Your grade is: D')
# elif grade in range(50, 60):
#     print('Your grade is: E')
# else:
#     print('Your grade is: F')

# grade = int(input('Enter the grade: '))
# if grade > 100 or grade < 0:
#     print('The grade is out of range!')
#     exit()
# if 90 <= grade <= 100:
#     print('Your grade is: A')
# elif 80 <= grade <= 89:
#     print('Your grade is: B')
# elif 70 <= grade <= 79:
#     print('Your grade is: C')
# elif 60 <= grade <= 69:
#     print('Your grade is: D')
# elif 50 <= grade <= 59:
#     print('Your grade is: E')
# else:
#     print('Your grade is: F')


# # Task N2
# from datetime import datetime
# now = datetime.now().year
# while True:
#     name = input("Enter your name: ")
#     if name == 'stop':
#         break
#     birth_day = input('Enter your birth day: ')
#     print('Hello', name)
#     print('You are:', now - int(birth_day), 'years old.')


## Task N3
# """
# Print:
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# """
# star = '* '
# for i in range(1, 5):
#     print(star * i)
# for i in range(1, 5):
#     print('* ' * i)


# Task N4
# '''
# Print:
# ***********
# **Python3**
# ***********
# '''
## 1
# lenght = 21
# rng = 4
# if rng == 0:
#     print('Type number bigger then 0')
# else:
#     if rng == 1 or rng == 2:
#         print('Python3'.center(lenght, '*'))
#     if rng >= 3:
#         for i in range(rng):
#             if i == int(rng / 2):
#                 print('Python3'.center(lenght, '*'))
#                 continue
#             else:
#                 print('*' * lenght)
## 2
# for i in range(0, 5):
#     if i == 2:
#         print('* Python *')
#         continue
#     else:
#         print('* ' * 6)



## Task N5
# '''
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# '''
number = 1
for i in range(0, 7):
    for j in range(0, i + 1):
        print(number, end=' ')
        number += 1
    print()


