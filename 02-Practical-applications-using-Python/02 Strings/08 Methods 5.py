"""
------------------------------------------------------------
----- String methods Find and replace in a text string -----
------------------------------------------------------------

The find() function searches in the text that called it for the number of the first place in which the same text or character we pass to it was found.
index() performs the same function as find() but throws a ValueError if it doesn't find the substring.
The replace() function replaces the expression chosen by the user - however frequent it is in the text string - with the new value that they specify.

"""
print("--------------------------------------------------")
# find(substring, start(optional), end(optional))
test = 'Hello world'
print(test.find('world'))
print(test.find('o'))
print(test.find('world', 0, 5))

print("--------------------------------------------------")
# index(substring, start(optional), end(optional))
test = 'Hello world'
print(test.index('world'))
print(test.index('o'))
try:
    print(test.index('world', 0, 5)) # ValueError: substring not found
except:
    print("-1")

print("--------------------------------------------------")
# replace(oldValue, newValue, Count(optional))

text = 'one plus one equal two'
print(text.replace('one', '1'))
print(text.replace('one', '1', 1))
