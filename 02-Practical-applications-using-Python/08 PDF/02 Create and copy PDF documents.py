"""
The PDFFileWriter() builder returns an object with which you can create and edit pdf files.
The addblankpage() function is used to create a blank page for a pdf file.
The write() function enables you to write and create a pdf file.
The addPage() function adds a new page to the pdf file.
"""

from PyPDF2 import PdfWriter as w
from pathlib import Path
import PyPDF2

pdf = w()
pth = Path.home() / Path('OneDrive', 'Desktop', 'Curces', 'Hsoub Academy', 'The Code', '02 Practical applications using Python', '08 PDF', 'pdf_file.pdf')
file = open(pth, 'wb')
for i in range(5):
    pdf.add_blank_page(219, 297) # a4 size dimensions
pdf.write(file)

# Copy
pth1 = Path.home() / Path('OneDrive', 'Desktop', 'Curces', 'Hsoub Academy', 'The Code', '02 Practical applications using Python', '08 PDF', 'pdf_test.pdf')
pdfFile = open(pth1, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
for pageNum in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdf.addPage(pageObj)

pdf.write(file)

file.close()