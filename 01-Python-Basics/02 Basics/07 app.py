my_num = 6
user_guess = input('Enter a number: ')

if not user_guess: # not srt means not True. because empty str is False
    print('You did not enter a Number')
    exit()
if int(user_guess) > 0:
    user_guess = int(user_guess) # Reassignment
    if user_guess == my_num:
        print('You win!')
    elif user_guess + 1 == my_num or user_guess - 1 == my_num:
        print('Too Close')
    else:
        print('You lose!')
else:
    print('Enter a Positive Number!')