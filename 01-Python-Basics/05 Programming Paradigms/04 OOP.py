"""
--------------------------------------------------
---------- Object Orieanted Programming -----------
--------------------------------------------------
Class has ==> Proporties, Methods
Instantiation ==> is creating object from class
__init__ ==> works autumatically on the instantiation time
PascalCase naming type is batter
For more Information:
https://academy.hsoub.com/programming/general/%D8%A7%D9%84%D8%A8%D8%B1%D9%85%D8%AC%D8%A9-%D9%83%D8%A7%D8%A6%D9%86%D9%8A%D8%A9-%D8%A7%D9%84%D8%AA%D9%88%D8%AC%D9%87-r1375/
https://academy.hsoub.com/programming/python/%d9%83%d9%8a%d9%81%d9%8a%d8%a9-%d8%a5%d9%86%d8%b4%d8%a7%d8%a1-%d8%a7%d9%84%d8%a3%d8%b5%d9%86%d8%a7%d9%81-%d9%88%d8%aa%d8%b9%d8%b1%d9%8a%d9%81-%d8%a7%d9%84%d9%83%d8%a7%d8%a6%d9%86%d8%a7%d8%aa-%d9%81%d9%8a-%d8%a8%d8%a7%d9%8a%d8%ab%d9%88%d9%86-3-r754/
"""


class Product:
    def __init__(self, id, name, price, count):  # Constractor
        self.id = id
        self.name = name
        self.price = price
        self.count = count

    def discount(self, ratio):
        self.price = self.price - self.price * ratio

    def info(self):
        return f'Id: {self.id}, Name: {self.name}, Price: {self.price}$, Count: {self.count}'


iphone_13 = Product(id=1, name='Iphone 13', price=999, count=10)

samsung_s21 = Product(id=2, name='Samsung s21', price=985, count=10)

print(iphone_13.info())
iphone_13.discount(0.3)
print(iphone_13.info())


#
#
#
#
#
#
# School

class School:
    def __init__(self, school_name, school_type, director_full_name, teachers_count=0, students_count=0):
        self.school_name = school_name
        self.school_type = school_type
        self.director_full_name = director_full_name
        self.teachers_count = teachers_count
        self.students_count = students_count

    def add_teacher(self, teacher_first_name, teacher_last_name, teacher_year, teacher_gender, teacher_nationality,
                    teacher_materials):
        self.teachers_count += 1
        self.teacher_first_name = teacher_first_name
        self.teacher_last_name = teacher_last_name
        self.teacher_age = teacher_year
        self.teacher_gender = teacher_gender
        self.teacher_nationality = teacher_nationality
        self.teacher_materials = teacher_materials

    def add_student(self, student_first_name, student_last_name, student_year, student_gender, student_nationality):
        self.students_count += 1
        self.student_first_name = student_first_name
        self.student_last_name = student_last_name
        self.student_year = student_year
        self.student_gender = student_gender
        self.student_nationality = student_nationality

    def change_derector(self, new_director_full_name):
        self.director_full_name = new_director_full_name

    def get_info(self):
        return f"\nSchool name: {self.school_name}, \nSchool type: {self.school_type}, \nDetector name: {self.director_full_name}, \nCount of teachers: {self.teachers_count}, \nCount ot students: {self.students_count}"

