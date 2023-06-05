"""
The write() function is used to write to the file.
The writelines() function is used to write one or more lines directly into the file.

"""

from pathlib import Path

pth = Path.home() / Path('OneDrive', 'Desktop', 'Curces', 'Hsoub Academy', 'The Code', '02 Practical applications using Python', '05 Perform operations on files', 'New folder', 'file_one.txt')

# myFile = open('file_one.txt', 'w')
myFile = open(pth, 'a')
myFile.write('\n11. Hello, how are you?\n')
myFile.write('12. Hello, how are you?\n')
myFile.write('13. Hello, how are you?\n')

# # writelines
# myList = ['\n14, Hello, how are you?\n', '15, Hello, how are you?\n']
# myFile.writelines(myList)