"""
The copy() function is used to copy files.
The copytree() function is used to copy the entire folder tree

"""

import shutil
from pathlib import Path

# copy and rename files only
pth1 = Path.home() / Path('OneDrive', 'Desktop', 'Curces', 'Hsoub Academy', 'The Code', '02 Practical applications using Python', '05 Perform operations on files', 'New folder', 'file_one.txt')
pth2 = Path.home() / Path('OneDrive', 'Desktop', 'Curces', 'Hsoub Academy', 'The Code', '02 Practical applications using Python', '05 Perform operations on files', 'files', 'file_one_copied.txt')

shutil.copy(pth1, pth2)

# copy and rename folders
pth1 = Path.home() / Path('OneDrive', 'Desktop', 'Curces', 'Hsoub Academy', 'The Code', '02 Practical applications using Python', '05 Perform operations on files', 'New folder')
pth2 = Path.home() / Path('OneDrive', 'Desktop', 'Curces', 'Hsoub Academy', 'The Code', '02 Practical applications using Python', '05 Perform operations on files', 'files', 'New folder_copied')

shutil.copytree(pth1, pth2)