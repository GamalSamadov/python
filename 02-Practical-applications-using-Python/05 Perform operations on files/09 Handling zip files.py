import os
import zipfile
from pathlib import Path
import shutil

pth = Path.home() / Path('OneDrive', 'Desktop', 'Curces', 'Hsoub Academy', 'The Code', '02 Practical applications using Python', '05 Perform operations on files')
# compressZip = zipfile.ZipFile(pth / Path('New folder.zip'))
#
# print(compressZip.namelist())
#
# file_info = compressZip.getinfo('New folder/file_one.txt')
#
# print(file_info.file_size)
# print(file_info.compress_size)

## Extract
# os.chdir(Path.home() / Path('OneDrive', 'Desktop'))
# compressZip.extractall()
# compressZip.extract('New folder/file_one.txt', pth / Path('extractFile'))

# # Compress Files
# newZip = zipfile.ZipFile('new.zip', 'w')
# newZip.write('New folder/file_one.txt')

## compress Folders
# folderZip = zipfile.ZipFile('New Folder Name.zip','w')
# folderZip.write(pth / Path('New folder'))

shutil.make_archive('New Compressed Folder With Shutil', 'zip', pth / Path('New folder')) # compresses only to zip and dar