"""
--------------------------------------------------
------ Polymorphism & Operator Overloading -------
--------------------------------------------------
Examples: + operator works with int and str's enought, len() works with data structors enoght

Polymorphism ==> same method does enought thing on the inheritanced class

Magical methods ==> are the buitin methods of classes
dir() ==> shows all methods of object
__add__() ==> is uses + operation on the classes to add the created object from the class to each other and takes self and other atributes
__lt__() ==> is uses the cheak last then < operatot on the classes
__str__() ==> resuld adding objects of class
__getitem__() ==> Allows the indexer [ ] to be used for class objects.

For more information:
https://academy.hsoub.com/programming/python/%D9%83%D9%8A%D9%81%D9%8A%D8%A9-%D8%AA%D8%B7%D8%A8%D9%8A%D9%82-%D8%A7%D9%84%D8%AA%D8%B9%D8%AF%D8%AF%D9%8A%D8%A9-%D8%A7%D9%84%D8%B4%D9%83%D9%84%D9%8A%D8%A9-polymorphism-%D8%B9%D9%84%D9%89-%D8%A7%D9%84%D8%A3%D8%B5%D9%86%D8%A7%D9%81-%D9%81%D9%8A-%D8%A8%D8%A7%D9%8A%D8%AB%D9%88%D9%86-3-r757/
"""

# Exemples
print(3 + 5)
print('Hello' + 'World')

name = 'Hsoub Academy'

numbers = [1, 2, 3, 4, 5, 6]

info = {1: 'Name', 2: 'Age', 3: 'Salary'}

print(len(name))
print(len(numbers))
print(len(info))  # Gives keys


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)  # creates new object from the class Point

    def __str__(self):
        return f"x: {self.x}, y: {self.y}, z: {self.z}"


pt1 = Point(3, 4, -5)
pt2 = Point(-4, 1, 3)

# print(pt1 + pt2) # TypeError: unsupported operand type(s) for +: 'Point' and 'Point'
print(pt1 + pt2)


class Cart:

    def __init__(self, items):
        self.items = items

    def __getitem__(self, item):
        return self.items[item]


order1 = Cart(['Pan', "Pancil", 'Notebook'])
print(order1.items[0])
print(order1[0])
