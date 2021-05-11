# a = 67
base = 5
# nearest_multiple = (base * round(a/base)) + 5
# print(nearest_multiple)
# grades = []
# max_students = 59
# min_students = 0
# i = 0
# while min_students <= len(grades) <= max_students:
#     i += 1
#     grade = input('Enter grades:')
#     if grade == '':
#         break
#     grades.append(grade)
# print(grades)

def round_off():
    grades = []
    max_students = 59
    min_students = 0
    i = 0
    while min_students <= len(grades) <= max_students:
        i += 1
        grade = input('Enter grades:')
        if grade == '':
         break
        grades.append(grade)
    for grade in grades:
        nearest_multiple = (base * round(int(grade)/base)) + 5
        if((nearest_multiple - int(grade) < 3)):
            new_grade = nearest_multiple
            print(new_grade)
        else:
            print(nearest_multiple)

if __name__  == '__main__':
    round_off()





