"""
The move() function is used to move files or folders.
The rename() function is used to rename files or folders.

"""

import shutil
from pathlib import Path
import os

# # move
# pth1 = Path.home() / Path('OneDrive', 'Desktop', 'Curces', 'Hsoub Academy', 'The Code', '02 Practical applications using Python', '05 Perform operations on files', 'New folder', 'test.txt')
# pth2 = Path.home() / Path('OneDrive', 'Desktop', 'Curces', 'Hsoub Academy', 'The Code', '02 Practical applications using Python', '05 Perform operations on files', 'files')
# shutil.move(pth1, pth2)

# # if the moving to folder not exsests the move() func creats the moving file with the name of the not exsested folder
# pth1 = Path.home() / Path('OneDrive', 'Desktop', 'Curces', 'Hsoub Academy', 'The Code', '02 Practical applications using Python', '05 Perform operations on files', 'New folder', 'test.txt')
# pth2 = Path.home() / Path('OneDrive', 'Desktop', 'Curces', 'Hsoub Academy', 'The Code', '02 Practical applications using Python', '05 Perform operations on files', 'SomeFolder')
# shutil.move(pth1, pth2)

# if the file exsests on the two folder the move func gives error (shutil.Error: Destination path "the\path" already exists)
# pth1 = Path.home() / Path('OneDrive', 'Desktop', 'Curces', 'Hsoub Academy', 'The Code', '02 Practical applications using Python', '05 Perform operations on files', 'New folder', 'file.txt')
# pth2 = Path.home() / Path('OneDrive', 'Desktop', 'Curces', 'Hsoub Academy', 'The Code', '02 Practical applications using Python', '05 Perform operations on files', 'files')
# shutil.move(pth1,pth2)

# # renaming using the move func
pth1 = Path.home() / Path('OneDrive', 'Desktop', 'Curces', 'Hsoub Academy', 'The Code', '02 Practical applications using Python', '05 Perform operations on files', 'New folder', 'file.txt')
pth2 = Path.home() / Path('OneDrive', 'Desktop', 'Curces', 'Hsoub Academy', 'The Code', '02 Practical applications using Python', '05 Perform operations on files', 'New folder','newFileName.txt')
# shutil.move(pth1,pth2)
## olso can use the os.rename() to rename
# os.rename(pth1, pth2)