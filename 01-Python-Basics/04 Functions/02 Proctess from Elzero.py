# # N1
# # #قم بعمل Function بإسم getPreviousNumbers تقبل منك Parameter واحد وهو الرقم
# # قم بطباعة الرقم وجميع الأرقام التي قبله
# # إذا كان الرقم عبارة عن صفر أو رقم سالب تظهر رسالة للشخص كما في المثال
# # إذا كان الرقم أكبر من 10 قم بجلب الأرقام الزوجية التي قبله فقط
# # إذا كان الرقم يساوي 10 أو أصغر قم بجلب جميع الأرقام التي قبله فقط
# # تأكد أن البيانات التي تعود نوعها Integer
# # لا يجب طباعة الرقم صفر في الرقم النهائي
# # يجب طباعة الرقم نفسه الموجود في ال Function وقبله الأرقام التي قبله
# # يجب طباعة الرقم والأرقام التي قبلها من اليسار لليمين بمعنى الرقم نفسه ثم الأرقام الموجودة قبله
# # getPreviousNumbers(0); # "Negative Numbers & Zero Not Allowed"
# # getPreviousNumbers(-20); # "Negative Numbers & Zero Not Allowed"
# # getPreviousNumbers(10); # 10987654321
# # getPreviousNumbers(17); # 17161412108642
#
# def getPreviousNumbers(number):
#     if number > 0:
#         if number <= 10:
#             while number != 0:
#                 print(number, end='')
#                 number -= 1
#         else:
#             if number % 2 == 0:
#                 while number != 0:
#                     print(number, end='')
#                     number -= 2
#             else:
#                 print(number, end='')
#                 number += 1
#                 while number != 0:
#                     number -= 2
#                     if number != 0:
#                         print(number, end='')
#     else:
#         print('Negative Numbers & Zero Not Allowed')
#
#
# getPreviousNumbers(0)
#
#
# #
# #
# #
# # N2
# def min_number(list):
#     number_list = []
#     for number in list:
#         if str(number).isnumeric():
#             number_list.append(number)
#     number_list.sort()
#     lower = number_list[0]
#     return lower
#
#
# my_list = [115, 20, 10, "A", "!", "@", 13, 1, 5, 2, "X", "C"]
# print(min_number(my_list))
#
#
# #
# #
# #
# #
# #
# # N3
# def get_special_chars_count(list):
#     """
#     :param list:
#     :Prints: Count charakters from bigger to smaller in item of list if the item is string
#     """
#
#     # Finding characters and count of these
#     chars_and_cout = {}
#     for item in list:
#         if type(item) == str:
#             for word in item:
#                 if not word.isnumeric() and not word.isalnum() and not word.isspace():
#                     if word not in chars_and_cout:
#                         chars_and_cout[word] = 1
#                     else:
#                         chars_and_cout[word] += 1
#         else:
#             continue
#
#     # Sorting from bigger to smaller
#     values_list = []
#     for value in chars_and_cout.values():
#         values_list.append(value)
#     values_sorted = []
#     while True:
#         if values_list == []:
#             break
#         else:
#             for value in values_list:
#                 if value is max(values_list):
#                     values_sorted.append(value)
#                     values_list.remove(value)
#
#     # Print
#     for item in values_sorted:
#         for key, value in chars_and_cout.items():
#             if value is item:
#                 print(f"{key} ==> {value}")
#
#
# my_list = ["!!Osa#", "#234!!!!!!!!!!@@", "@@@A", "ES6", "!@#@@@!", '$', 1, 123, [], 1.1]
# get_special_chars_count(my_list)

#
# قم بعرض الأرقام المميزة من داخل List مع تجاهل ال Strings وتحويل ال Float ل Int وال Boolean للمناسب
# المطلوب
# قم بإزالة العناصر المكررة من داخل ال List
# لا تطبع أي String تجده
# إذا وجدت أي Float قم بتحويله ل Integer
# إذا وجدت True إطبع بدلا منه رقم 1 و False بدلا منه رقم 0
# قم بترتيب الأرقام من الأكبر للأصغر
# إذا كان عدد الأرقام عدد فردي قم بطباعتهم كما هم
# إذا كان عدد الأرقام زوجي في السطر الأول قم بطباعة حاصل جمع الرقم الأول مع الرقم الأخير
# في السطر الثاني قم بطباعة حاصل جمع الرقم الثاني مع الرقم قبل الأخير
# في السطر الثالث قم بطباعة حاصل جمع الرقم الثالث مع الرقم قبل قبل الأخير
# وهكذا إلى أن يتبقى رقمين فقط
# آخر رقمين قم بطباعة حاصل ضربهم في بعضهم وليس جمعهم كالباقي
# التحديات
# لا تقم بتغيير نوع البيانات List ابدا لأي نوع آخر
#

# Unique Numbers
def unique_numbers(list):
    # Cnaging False ==> 0, True ==> 1, float ==> int, str ==> Empty
    for i in range(len(list)):
        if type(list[i]) == str:
            list[i] = ''
            continue
        elif type(list[i]) == bool or type(list[i]) == float:
            list[i] = int(list[i])

    # remove str
    while '' in list:
        for string in list:
            if string == '':
                list.remove(string)

    # remove multi items without using set type of date
    set_list = []
    for item in list:
        if item not in set_list:
            set_list.append(item)
    list = set_list

    # Biggeer to smaller
    list.sort(reverse=True)

    # Cheak lengh of list and do the challange
    def cheak_len(list):
        # Odd
        if len(list) % 2 != 0:
            print(list)
        # Even
        else:
            n = -1
            lengh = int(len(list) / 2)
            new_list = []
            for i in range(lengh):
                # print(list[i], i + 1)
                if i == lengh+1:
                    new_list.append(list[i] * list[i - 1])
                else:
                    new_list.append(list[i] + list[n])
                    n -= 1
            list = new_list
    cheak_len(list)


# numbers = [15.60, 2, 2, 2, 4, 5, True, True, 7, "A", 2, False, 2, 8, 9]
numbers = [15.60, 2, 2, 2, 4, 5, True, True, 7, "A", 2, False, 2, 3, 8, 9, 2]

unique_numbers(numbers)
