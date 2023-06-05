'''
--------------------------------------------------
---------------- OOP Inheritance -----------------
--------------------------------------------------
SuperClass, or Base Class ==> Father class
Subtype, or Derived Class ==> Son Class
Son class inherits, Derives, Extends the father class

a Son Class is a Father Class
For More information:
https://academy.hsoub.com/programming/python/%D9%88%D8%B1%D8%A7%D8%AB%D8%A9-%D8%A7%D9%84%D8%A3%D8%B5%D9%86%D8%A7%D9%81-%D9%81%D9%8A-%D8%A8%D8%A7%D9%8A%D8%AB%D9%88%D9%86-3-r756/
https://wiki.hsoub.com/Python/inhertance
'''


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


class Mobile(Product):
    def __init__(self, id, name, price, count, memory, storage, screen_size):  # Constractor
        super().__init__(id, name, price, count)
        self.memory = memory
        self.storage = storage
        self.screen_size = screen_size

    def spaces(self):
        return f"Memory: {self.memory}, Storage: {self.storage}, Screen Size: {self.screen_size}"


class Laptop(Product):
    def __init__(self, id, name, price, count, disk_space, cpu, ram, screen_size):  # Constractor
        super().__init__(id, name, price, count)
        self.disk_space = disk_space
        self.cpu = cpu
        self.ram = ram
        self.screen_size = screen_size

    def spaces(self):
        return f"Disk Space: {self.disk_space}, CPU: {self.cpu}, Ram: {self.ram}, Screen Size: {self.screen_size}"


class Monitor:
    def __init__(self, id, name, price, count):  # Constractor
        self.id = id
        self.name = name
        self.price = price
        self.count = count


samsung_galaxy_s21 = Mobile(1, 'Samsung S21', 975, 10, 12, 512, 6.1)
print(samsung_galaxy_s21.info())
print(samsung_galaxy_s21.spaces())
macbook_pro_2021 = Laptop(2, "Macbook Pro M1", 1200, 5, 1000, 'M1', 16, 13.0)
print(macbook_pro_2021.info())
print(macbook_pro_2021.spaces())