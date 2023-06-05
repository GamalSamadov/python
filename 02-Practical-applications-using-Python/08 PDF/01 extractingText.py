"""
Installing the PyPDF2 package:
pip install PyPDF2
PdfFileReader() builder returns an object in which you can read and browse the contents of pdf files.
The numpage property lets you know the number of pages within a pdf file.
The getpage() function returns an object from which we can read the contents of the specified page.
The extracttext() function is used to extract the text from the object that the previous function returns.
Link to the pdf_test.pdf file used in the lesson.
"""

import PyPDF2
from pathlib import Path

pth = Path.home() / Path('OneDrive', 'Desktop', 'Curces', 'Hsoub Academy', 'The Code', '02 Practical applications using Python', '08 PDF', 'pdf_test.pdf')
pdfFileObj = open(pth,'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# pages Numbers
print(pdfReader.numPages)

# read
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())