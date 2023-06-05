"""
--------------------------------------------------
---------------- OOP Abstraction -----------------
--------------------------------------------------
Abstraction ==> making base abstracted class
Abstract method ==> method that abstracted class doesn't support it but inheritenced classes supports it and if the abstracted class has this this method inheritanced class must to have it

More Information:
https://academy.hsoub.com/programming/python/%D8%A7%D9%84%D9%85%D8%B2%D8%AE%D8%B1%D9%81%D8%A7%D8%AA-decorators-%D9%81%D9%8A-%D8%A8%D8%A7%D9%8A%D8%AB%D9%88%D9%86-r303/
https://wiki.hsoub.com/Python/collections.abc#.D8.A7.D9.84.D8.A3.D8.B5.D9.86.D8.A7.D9.81_.D8.A7.D9.84.D8.A3.D8.B3.D8.A7.D8.B3.D9.8A.D8.A9_.D8.A7.D9.84.D9.85.D8.AC.D8.B1.D9.91.D8.AF.D8.A9_.D9.81.D9.8A_.D8.A7.D9.84.D9.88.D8.AD.D8.AF.D8.A9_collections
"""

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def aria(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def aria(self):
        return self.side ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def aria(self):
        return (self.base * self.height) / 2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def aria(self):
        return 3.14 * self.radius ** 2


square = Square(4)
print(square.aria())


triagle = Triangle(6, 8)
print(triagle.aria())

circle = Circle(5)
print(circle.aria())