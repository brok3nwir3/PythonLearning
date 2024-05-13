# Week 24 - Answer Key

# AVOID PEEKING AHEAD OF TIME!










# Scroll down.
# |
# |
# v




























# Q1
q = ['dog', 'cat', 'John', 32]
animal1 , animal2, name1, age1 = q
print(animal1, animal2, name1, age1)

# Q2
h = ['a', 'b', 'c', 5, (1, 3, 7)]
var1 , var2, var3, var4, var5 = h
print(var1 , var2, var3, var4, var5)

# Q3
e = ['apple', 2, 3, 4, 5, 'orange']
fruit1, *numbers, fruit2 = e
print(fruit1, numbers, fruit2)

# Q4
var1 = 1
var2 = 2
var3 = 3
var4 = var1,var2,var3
print(var4)
print(type(var4))

# Q5
def drop_first_last(grades):
    first, *middle, last = grades
    average = sum(middle)/len(middle)
    print(average)

# Q6
student1_grades = [70, 65, 82, 90, 75, 84, 72]
student2_grades = [65, 61, 70, 73, 72, 68, 61]
student3_grades = [80, 91, 93, 85, 87, 79, 73]
student4_grades = [94, 100, 100, 99, 97, 98, 95]
student5_grades = [73, 84, 90, 76, 93, 81, 74]
all_students = [student1_grades,student2_grades,student3_grades, student4_grades, student5_grades]

def drop_first_last(grades):
    first, *middle, last = grades
    average = sum(middle)/len(middle)
    print(average)

for student in all_students:
    drop_first_last(student)

# Q7
student1_grades = [70, 65, 82, 90, 75, 84, 72]
student2_grades = [65, 61, 70, 73, 72, 68, 61]
student3_grades = [80, 91, 93, 85, 87, 79, 73]
student4_grades = [94, 100, 100, 99, 97, 98, 95]
student5_grades = [73, 84, 90, 76, 93, 81, 74]
all_students = [student1_grades,student2_grades,student3_grades, student4_grades, student5_grades]

def drop_first_last(grades):
    first, *middle, last = grades
    average = sum(middle)/len(middle)
    print(average)
    if average < 70:
        student.append('FAIL')
    else:
        student.append('PASS')
    print(student)

for student in all_students:
    drop_first_last(student)

# Q8 ---BONUS---



# Scroll down.
# |
# |
# v



















'''
import os
path = '/etc'
os.chdir(path)

def shadow_parse(target_file):
    for line in target_file:
        uname, password, *fields= line.split(':')
        if not password.startswith('!') and not password.startswith('*'):
            print(uname + ' ' + password)

read_shadow = open('shadow', 'r')
lines = read_shadow.readlines()
shadow_parse(lines)
read_shadow.close()
'''