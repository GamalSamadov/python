'''
Type system: Dynamic, Static

Static:
Runs the code during compiling. and the code dosn't work if has any errors on it.
On the stadic system type programmer has to type type of each variables and can't change types of variables
Like the
- C++
# C#
- Java
- GO

Dynamic:
Cheaks to the code on the runtime after the compiling. And the code works and shows the error if it has an error
The system cheaks to the type of variable automaticly and programmer can change type pf variables if he needs
Like the:
- JavaScript
- Python
- Roby
- PhP

There is the duck type system:
If it walks like a dock, and it quacks like a dock then it must be a dock
like python.

Type hinting:
the hint that programmer can type on the function arguments to hint the type of the variable
Annotations ==> the hint that we type on the functions
Annotations dosn't works on the runtime, it works on the compiling time. that is why it dosn't give error
On the visual studio code There is Extention by name: "pyLance" that cheaks to the annotations but it dosn't gives a error
there is a libroary calls: "myPy"
'''


class myLen():
    def __len__(self):
        return 1000


x = myLen()
print(len(x))


# Annotations
def dublicate(value: float) -> float:
    """
    It dublicates the given Float number
    :param value:
    :return:
    """
    return value * 2


print(dublicate(5))
print(dublicate("5")) # 5
