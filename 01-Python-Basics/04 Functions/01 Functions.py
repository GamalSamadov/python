"""
--------------------------------------------------
------------------- Functions --------------------
--------------------------------------------------


For more information:
https://academy.hsoub.com/programming/python/%d8%aa%d8%b9%d8%b1%d9%81-%d8%b9%d9%84%d9%89-%d8%a7%d9%84%d8%af%d9%88%d8%a7%d9%84-functions-%d9%81%d9%8a-%d8%a8%d8%a7%d9%8a%d8%ab%d9%88%d9%86-r292/
https://academy.hsoub.com/programming/python/%D9%83%D9%8A%D9%81%D9%8A%D8%A9-%D8%AA%D8%B9%D8%B1%D9%8A%D9%81-%D8%A7%D9%84%D8%AF%D9%88%D8%A7%D9%84-%D9%81%D9%8A-%D8%A8%D8%A7%D9%8A%D8%AB%D9%88%D9%86-3-r752/
"""

def my_function():
    print('Hello World!')

my_function()

def sum():
    print(3)
    print(4)
    return
    print(3*4) # Will not print it


def get_age():
    age = 44
    if age < 0:
        return
    if age > 120:
        return
    print(age)

get_age()

def degree():
    return 40

temprature = degree()
print(temprature)

def temprature_scales():
    return ['Celsius', 'Fahrenheit', 'Kelvin']

scale = temprature_scales()[1]

scales = temprature_scales()[:2]
print(scales)