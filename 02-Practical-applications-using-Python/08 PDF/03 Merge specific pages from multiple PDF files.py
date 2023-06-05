import PyPDF2, os
from pathlib import Path

pdfFiles = []
pth = Path.home() / Path('OneDrive', 'Desktop', 'Curces', 'Hsoub Academy', 'The Code', '02 Practical applications using Python', '08 PDF', 'article')

for filename in os.listdir(pth):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

pdfFiles.sort(key= str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

for filename in pdfFiles:
    pdfFileObj = open(pth / Path(str(filename)), 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

pdfOutput = open(pth / Path('atricle.pdf'), 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()



