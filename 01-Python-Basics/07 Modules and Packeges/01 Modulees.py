"""
--------------------------------------------------
-------------------- Modules ---------------------
--------------------------------------------------

Modular Programming ==> is a software design technique that emphasizes separating the functionality
of a program into independent, interchangeable modules, such that each contains everything necessary to
execute only one aspect of the desired functionality.


The isinstance() function returns a boolean indicating whether the given object is an instance of the given class.
The choice() method returns a random element of the specified sequence (list, string, array, etc.).

"""
# import sys
# from quotes import * # This way not good
# from quotes import get_quotes as quotes # This way not good
# import quotes as q

# def get_quotes_module():
#     from quotes import get_quotes
#
# def get_quotes_module():
#     from quotes import * # Gives: SyntaxError: import * only allowed at module level

# try:
#     from quotes import get_quotes as quotes
# except:
#     print('Module not found')

# print(quotes())
# print(sys.path)

import quotes
print(quotes.get_quotes())