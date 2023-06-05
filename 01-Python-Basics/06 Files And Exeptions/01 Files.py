"""
--------------------------------------------------
----------------- File Handling ------------------
--------------------------------------------------


There is no difference between editing the files using apps and editing it using programming languages. Two ways uses Open, Edit, Save tools
The difference in how files are handled.

The App saves a copy from the files. When the editing ends
the app saves the copied file into the original file.

Programming languages deals with files in a sequential manner to edit or only read it.
Edits it by deleting originals values and updates it with the new value or adds new value into the original value.
Reads the files line by line

w ==> write mode
r ==> read mode
a ==> Append value mode
rb ==> read Bite
wb ==> Write Bite

read(word) ==> read the full file bu default or by words
readline(lines) ==> read the file line by line

there is some modules to work with files:
- wave ==> for wave files
- zipfile ==> for zips
- xml.etree.elementTree ==> for xml files
- pyPdf2 ==> for pdf files
- xlwings ==> for xl files
- Pillow ==> for images

for more information:
https://academy.hsoub.com/programming/python/%D8%A7%D9%84%D8%AA%D8%B9%D8%A7%D9%85%D9%84-%D9%85%D8%B9-%D8%A7%D9%84%D9%85%D9%84%D9%81%D8%A7%D8%AA-%D8%A7%D9%84%D9%86%D8%B5%D9%8A%D8%A9-%D9%81%D9%8A-%D8%A8%D8%A7%D9%8A%D8%AB%D9%88%D9%86-r306/

"""

# f = open('C:/Users/gamal/OneDrive/Desktop/Curces/Hsoub Academy/The Code/01 Python Basics/06 Files And Exeptions/file.txt')
# f = open('C:\\Users\\gamal\\OneDrive\\Desktop\\Curces\\Hsoub Academy\\The Code\\01 Python Basics\\06 Files And Exeptions\\file.txt')
f = open('file.txt', 'w')
f.write('Hello from Python\n')
f.write('I love Python')
f.close()

f = open('file.txt', 'r')
print(f.read())
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

f = open('file.txt')
for line in f:
    print(line, end=' ')
f.close()

with open('file.txt', 'r') as f:
    print(f.read())

with open('file.txt', 'w') as f:
    f.write('Hello Hello world!\n')
    f.write('I Am from Python\n')
    f.write('So I Love Python\n')

with open('file.txt', 'r') as f:
    print()
    print(f.read())

with open('file.txt', 'a') as f:
    f.write('Just new text from python')

with open('file2.txt', 'w') as f:
    f.write('')

with open('file.txt', 'r') as f1, open('file2.txt', 'w') as f2:
    f_lines = f1.read()
    f2.write(f_lines)