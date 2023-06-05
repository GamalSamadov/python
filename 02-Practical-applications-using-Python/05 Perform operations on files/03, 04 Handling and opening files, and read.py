"""
The open() function is used to open a specified file.
The getcwd() function returns a string containing the current working folder.
The chdir() function changes the current working directory to the passed directory.
The home() function returns a new path object representing the user's home path.

The read() function is used to read the entire file.
The readline() function is used to read a line from a file.
The readlines() function returns a list of all the lines in the file.
The close() function closes the file.
"""

from pathlib import Path
import os

print(os.getcwd())
# os.chdir(r'C:\Users\gamal\OneDrive\Desktop\Curces\Hsoub Academy\The Code\02 Practical applications using Python\05 Perform operations on files\New folder')

print(Path.home())
pth = Path.home() / Path('OneDrive', 'Desktop', 'Curces', 'Hsoub Academy', 'The Code', '02 Practical applications using Python', '05 Perform operations on files', 'New folder', 'file_one.txt')
print(str(pth))

myFile = open(pth, 'r')

# read file
print(myFile)
print(myFile.name)
print(myFile.mode)

# print(myFile.read())
# print(myFile.readline(4))
# print(myFile.readlines())

lines = myFile.readlines()

# print(lines[0:5])

i = 0

for line in lines:
    print(line)
    i+=1
    if i ==5:
        break


myFile.close()