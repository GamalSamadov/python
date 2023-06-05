import random

name = input("What is your name? ")
print("\nGood Luck! " + name+'\n\n')

names = ['hadi', 'yara', 'hasan', 'sara', 'osama']

word = random.choice(names)

print("the name is:")

guesses = ''

turns = 12

while turns > 0:

    failed = 0

    for char in word:

        if char in guesses:
            print(char)

        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You Win")
        print("The name is: ", word)
        break

    guess = input("\nguess a character:")

    guesses += guess

    if guess not in word:
        turns -= 1
        print("\nWrong guess\n")
        print("You have", + turns, 'more guesses\n\n')

        if turns == 0:
            print("You Loose")