"""--------------------------------------------------
-----------------------List-----------------------
--------------------------------------------------
list ==> iterable object
list ==> mutable and changeble object
list[new index] = 'value' ==> adding a new item
del list_name[index] - delete the item
list.append('new value') ==> adding a new item
list.extend('1', '2') ==> adding many of items to the list
list.insert(index) ==> adding new item to the correct place by index
list.remove('value') ==> remove the item by the value
list.pop(index) ==> remove item by the index
list.sort(reverse=False) ==> sorting the list

"""


devices = ['Smart TV', 'Phone', 'Tablet', 'Laptop', 'Personal Computer']
devices[1] = 'Smart Phone'
print(devices)

del devices[0]  # Delete
print(devices)

devices.append('Smart Watch')  # Adds new item to the end of List
print(devices)
devices.append(['1', '2'])
print(devices)

devices.extend(['1', '2'])  # Adds many of items to the list, if list has this item then dosn't adds
print(devices, 'extend()')

devices.insert(0, 'Yangi birinchi item')  # Adds to the index of list
print(devices)
devices.insert(1, 'Yangi ikkinchi item')
print(devices)

devices.remove('Yangi ikkinchi item')  # removes item
print(devices)

devices.pop(0)  # removes item of this index
print(devices)
devices.pop(-2)
print(devices)
devices.pop(-2)
print(devices)
devices.pop(-1)
print(devices)

devices.sort()  # sorts the list
print(devices)
