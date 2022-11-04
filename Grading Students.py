#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.

def gradingStudents(grades):
    gradex = []
    for grade in grades:
        if grade < 38:
            gradex.append(grade)
            continue
        for x in range(2):
            if (grade + x+1) % 5 == 0:
                gradex.append(grade + x+1)
                break
            if x == 1:
                gradex.append(grade)

    return (gradex)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
