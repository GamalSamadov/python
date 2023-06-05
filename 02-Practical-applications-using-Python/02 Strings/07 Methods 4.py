"""
--------------------------------------------------
---------------String methods Space---------------
--------------------------------------------------

The center() function returns the characters of the text string shifted toward the center.
The ljust() function returns left-shifted string characters.
The rjust() function returns right-shifted string characters.
The expandtabs() function converts all tabs to whitespace.
"""

print("--------------------------------------------------")
# ljust() rjust() center()

test = 'Hello'
print(test.rjust(10))
print(test.ljust(10))
print(test.center(10))

test = 'Hello'
print(test.rjust(10, "-"))
print(test.ljust(10, "-"))
print(test.center(10, "-"))
print(test.center(11, "-"))

print("--------------------------------------------------")
# expandtabs()
test = 'Hello \tHow are you? \t are you good? \t'
print(test.expandtabs(10))