"""
The unlink() function deletes the specified file.
The rmdir() function deletes the specified folder (empty folders only).
The rmtree() function is used to delete the entire folder tree.
The send2trash() function is used to delete files or folders and put them in the trash. To install the package: (pip install Send2Trash)

"""

import os
from pathlib import Path
import shutil
import send2trash

pth1 = Path.home() / Path('OneDrive', 'Desktop', 'Curces', 'Hsoub Academy', 'The Code', '02 Practical applications using Python', '05 Perform operations on files')

## ------ removing the file but gives error if the file not exsists and cannot delete the folders --------
# os.unlink(pth1/ Path('New folder', 'newFileName.txt'))

## ----- removing the empty folder but gives error if the file not exsists ------
# os.rmdir(pth1 / Path('New folder', 'SomeDir'))

## ----- removing the empty and not empty folder but gives error if the file not exsists ------
# shutil.rmtree(pth1 / Path('New folder', 'SomeDir'))

## ----- bast way to remove and send to trash ------

send2trash.send2trash(pth1 / Path('New folder', 'myFile.txt'))
