"""
--------------------------------------------------
---------------------- Sets ----------------------
--------------------------------------------------
Sets ==> theres items are unique
Sets ==> Iterable but they are not sequance
Sets ==> Mutable but its elements are immutable
Empty sets gives False
The set() function is used to create an empty set, and to convert an iterable object into a set.
The union() function is used to combine elements of groups (equivalent to the parameter I).
The intersection() function returns the common elements between groups (&).
The difference() function returns items that are not shared between the sets (-).
The symmetric_difference() function returns all elements that are not shared between groups.
The add() function adds one element to the collection.
The discard() function deletes a single element from the collection, if it exists.

For more information:
https://wiki.hsoub.com/Python/set_operations
https://academy.hsoub.com/programming/python/%d8%a7%d9%84%d8%aa%d8%b9%d8%a7%d9%85%d9%84-%d9%85%d8%b9-%d8%a7%d9%84%d8%b5%d9%81%d9%88%d9%81%d8%8c-%d8%a7%d9%84%d9%85%d8%ac%d9%85%d9%88%d8%b9%d8%a7%d8%aa-%d9%88%d8%a7%d9%84%d9%82%d9%88%d8%a7%d9%85%d9%8a%d8%b3-%d9%81%d9%8a-%d8%a8%d8%a7%d9%8a%d8%ab%d9%88%d9%86-r226/

"""
#
#
#
#
#
"""Set da ikta bir xil element bo'lmaydi hamda o'zgaruvchi elementlarni set qabul qilmaydi"""

print('-'*50)
print(' Sets '.center(50, '-'))
print('-'*50)

numbers = {1, 2, 3, 4}
fruits = {'apple', 'banana', 'lemon', 'orange'}

empty = {} # Dict
print(type(empty)) # Dict


fruits_list = {'apple', 'banana', 'lemon', 'orange', 'apple'}
fruits_set = set(fruits_list)
print(fruits_set)

empty_set = set()
print(empty_set)
print(type(empty_set))
print(bool(empty_set))

print('apple' in fruits_set)
print('banana' in fruits_set)
print('mango' not in fruits_set)
print(len(fruits_set))

set1 = {'Lemon', 'Orange', 'Grapefruit'}
set2 = {'Apple', 'Banana', 'Pear', 'Orange'}
set3 = {'Watermelon', 'Honeymelon'}

print(set1 | set2 | set3) # Faqat set bilan setni qo'shadi
print(set1.union(set2, set3)) # Set ga boshqa data larni ham qo'shsa bo'ladi

print(set1 & set2) # Ikalasida ham bor bo'lgan elementlarni ko'rsatadi
print(set1.intersection(set2))

print(set1 - set2) # Birinchisida bo'lib ikkinchisida yo'q bo'lganlarn ko'rsatadi
print(set1.difference(set2))

print(set1 ^ set2) # Ikalasida mushtarak bo'lmagan elementlarni ko'rsatadi
print(set1.symmetric_difference(set2))

x = {1,2,3,4,5,6,7,8}

x.add(1)
x.remove(1)
try:
    x.remove(123123)
except KeyError:
    print("KeyError: 123123")
x.discard(2435235)
x.pop()
print(x)
# Set lar emutable!!!

