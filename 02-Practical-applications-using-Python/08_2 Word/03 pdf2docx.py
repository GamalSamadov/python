"""
Install pdf2docx package:
pip install pdf2docx

Converter() is used to process the PDF file to be converted into a docx file.
The convert() function converts a PDF file into a docx file.
The link to the article.pdf file used in the lesson.


"""

from pdf2docx import Converter
from pathlib import Path

pth = str(Path.home() / Path('OneDrive', 'Desktop', 'file.pdf'))
pth2 = str(Path.home() / Path('OneDrive', 'Desktop', 'file.docx'))

pdf_file = pth
docx_file = pth2

# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file)      # all pages by default
cv.close()
