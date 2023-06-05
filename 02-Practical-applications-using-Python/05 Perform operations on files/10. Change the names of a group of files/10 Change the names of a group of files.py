import shutil, os, re
from pathlib import Path

datePuttern = r'^(.*?)((0|1)?\d)-((0|1|2|3)?\d)-((19|20)\d\d)(.*?)$'

pth = Path.home() / Path('OneDrive', 'Desktop', 'Curces', 'Hsoub Academy', 'The Code', '02 Practical applications using Python', '05 Perform operations on files', '10. Change the names of a group of files', 'files')

for filename in os.listdir(pth):
    search = re.search(datePuttern, filename)

    if search == None:
        continue

    beforePart = search.group(1)
    monthPart = search.group(2)
    dayPart = search.group(4)
    yearPart = search.group(6)
    afterPart = search.group(8)

    newFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    print(f"Renaming {filename} to {newFilename}")

    oldName = pth / filename
    newName = pth / newFilename

    shutil.move(oldName, newName)
print('done')