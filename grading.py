import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents():
    a = 13
    base = 5
    nearest_multiple = base * round(a/base)

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
    print(grades)

