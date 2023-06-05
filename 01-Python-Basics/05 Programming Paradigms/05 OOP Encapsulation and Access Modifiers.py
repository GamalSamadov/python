"""
--------------------------------------------------
-------- Encapsulation & Access Modifiers --------
--------------------------------------------------

Concepts of OOP:
- Encapsulation
- Abstraction
- Inheritance
- Polymorphism

Encapsulation ==> means the every object has a special case. Like other object cannot change its case while it doesn't allow. This heppens with functions Getters and setters

Public object ==> other objects can change its and its Inheritance's value
Protected object ==> other object can change value of its Inheritances
Private ==> other object can not change its ind its Inheritances's value

Python Doesn't support encopsulation. But programmers type the name of Protected with one _ on the begin and with Two __ on begin of the Private
on the private __name can change it value using: object._ClassName__name and python dosn't give error Because python doesn't support Encapsulation

"""


class Product:
    def __init__(self, id, name, price, count):  # Constractor
        self.id = id
        self.name = name
        self.__price = price
        self.count = count

    def discount(self, ratio):
        self.__price = self.__price - self.__price * ratio

    def info(self):
        return f'Id: {self.id}, Name: {self.name}, Price: {self.__price}$, Count: {self.count}'

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return str(self.__price) + '$'


iphone_13 = Product(id=1, name='Iphone 13', price=999, count=10)
iphone_13.__price = 0
print(iphone_13.info())
print(iphone_13.__price)
# Name Mangling
iphone_13._Product__price = 0
print(iphone_13.info())
