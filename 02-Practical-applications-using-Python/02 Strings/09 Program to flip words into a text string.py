"""
Problem solving steps:
1 - Type the algorithms
2 - Flow chart
3 - pseudo code

Algoritm - is steps to solve the problem.

----- flip words into a text string -----

1 - create the string variable
2 - split the words to a list
3 - reverse the list
4 - join the list in a string
"""

def reverse_string_words(string):
    try:
        string = str(string)
    except:
        print('You can only Use string on this function.')
    old_list = string.split(' ')
    old_list.reverse()
    string = ' '.join(old_list)
    return string

print(reverse_string_words('Hey a a'))