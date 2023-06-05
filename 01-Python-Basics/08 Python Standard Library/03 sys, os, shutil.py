"""
sys:
The platform property returns a string containing the operating system identifier.
The path property returns a list of strings specifying the search path for the units.
The startswith() function is used to find out if the text that called it starts with a given text.
The version property returns a string containing the interpreted version of Python in use.
The getwindowsversion() function returns information about the installed version of Windows.

os:
The getcwd() function returns the current working folder.
The chdir() function is used to change the current working folder.
The listdir() function is used to display the contents of the current working folder.
The scandir() function is used to browse the contents of the current working folder.
The is_file() function returns True if the object that called it was a file.
The mkdir() function is used to create folders.
The makedirs() function is used to create folders in a hierarchical fashion.
The rename() function is used to rename a file or folder.
The rmdir() function is used to delete empty folders.

shutil:
The rmtree() function is used to delete folders.
To copy a file from one location to another you use the copy() function.
The copy2() function is used to copy a file from one location to another.
You can move files and folders with the move() function.
"""

import os
import shutil
import sys

#
#
#
#
# Sys
# Shows ==> win32 on windows, linux on the linux and darwin on the macos
print(sys.platform)

if sys.platform.startswith('win32'):
    print('You\'re Using Windows')
elif sys.platform.startswith('linux'):
    print('Your\'e Using Linux')
elif sys.platform.startswith('darwin'):
    print('Your\'e Using MacOs')

print(sys.version)

if sys.version.startswith('3.10.5'):
    print('Python is up to date.')
else:
    print('Python is old. Please update.')

print(sys.getwindowsversion())
#
#
#
#
# os
#
# get corrent worcing derectory
print(os.getcwd())

# change folder
# os.chdir('01 python basics/08 python standard library/')  # Relative peth
print(os.getcwd())
# os.chdir('../folder1')
print(os.getcwd())
# os.chdir('..')
print(os.getcwd())

# Show files on list
print(os.listdir())

# Show the files by the better way
print(os.scandir())
content = os.scandir()


# print('\n')
# for file in content:
#     if file.is_file():
#         print(file.name)

# Make dir
try:
    os.mkdir('folder3')
except:
    print(
        'FileExistsError: [WinError 183] Cannot create a file when that file already exists: \'folder3\'')


# Make dir in dir
# os.makedirs('folder3/folder6')

# rename
# os.rename('folder01', 'folder01')

# Remove dir
os.chdir('01 Python Basics/08 Python Standard Library')
print(os.getcwd())
print('\n')
os.mkdir('folder5')
os.rmdir('folder5')

os.mkdir('folder5')
os.makedirs('folder5/folder6')
try:
    os.rmdir('folder5')
except OSError:
    shutil.rmtree('folder5')
#
#
#
#
#
#
# Shutil
#
# remove dir while has a dir inner
# os.mkdir('folder01')
# shutil.rmtree('folder01')

# Copy file
shutil.copy('file1.txt', 'folder2/file1.txt')
shutil.copy2('file1.txt', 'folder2/file1.txt')

# Move file
# shutil.move('file2.txt', 'folder2/file2.txt')
# rename using move()
shutil.move('file1.txt',
            'file001.txt')
