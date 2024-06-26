# Week 9 Test - A test of the content covered in weeks 1-8.

# This test is for your benefit. If you do not know an answer, make your best guess and move to the next question.
# Once all questions have been attempted, check the answer key against your work.
# Use your incorrect answers as a gauge of your knowledge and a guide for future improvement.
# It's okay if you miss some questions. We're here to learn and get better.


# Q1
# What is 'animal' in the following code?
'''
animal = 'zebra'
'''
# A) string
# B) value
# C) method
# D) variable
# E) library


# Q2
# In the following code, what is print an example of?
'''
print("Hello, World!")
'''
# A) library
# B) call
# C) script
# D) variable
# E) function


# Q3
# What type of language is Python?
# A) functional
# B) compiled
# C) procedural
# D) interpreted
# E) front end


# Q4
# T/F: Python is a dynamically typed language.
# A) True
# B) False


# Q5
# What will be returned by the following code?
'''
print(bool(4==4.0))
'''
# A) 4
# B) True
# C) 4.0
# D) False
# E) Type Error


# Q6
# What will be printed by the following code?
'''
y = 9.3
y = "cat"
print(y)
'''
# A) 9.3
# B) "cat"
# C) Assignment Error
# D) False


# Q7 What will be returned by the following code?
'''
f = "seagull"
print(f[3:5])
'''
# A) gul
# B) ag
# C) gu
# D) agu


# Q8
# T/F: Python does NOT feature garbage collection.
# A) True
# B) False


# Q9 What will be returned by the following code?
'''
fruits = ["apple", "banana", "cherry", "kiwi", "grape", "lemon"]
print(fruits[-2])
'''
# A) banana
# B) lemon
# C) grape
# D) kiwi
# E) cherry


# Q10
# What is the programming term for combining two items?
# A) slicing
# B) indicing
# C) concatenating
# D) temping
# E) iterating


# Q11
# What is 'w' in the following code?
'''
w = ["abc", 34, True, 40, "male"] 
'''
# A) list
# B) tuple
# C) set
# D) dictionary


# Q12
# What is 'h' in the following code?
'''
h = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
'''
# A) list
# B) tuple
# C) set
# D) dictionary


# Q13
# How many times will the word "BOOM" be printed?
# And what is the final value of 'count'?
'''
count = 0
while (count < 7):
	count = count + 2
	print("BOOM")
'''
# A) 3, 8
# B) 4, 6
# C) 3, 6
# D) 4, 8


# Q14
# What will the following print statement return?
'''
num1 = 19
num2 = 5
result = num1 % num2
print(result)
'''
# A) 15
# B) 2
# C) 13
# D) 4


# Q15
# What pattern is made by the following code?
'''
for i in range(5):
    for j in range(i):
        print("*", end="")
    print() # new line after each row
'''
# A)
# ****
# ***
# **
# *
# B)
# *
# **
# ***
# ****
# C)
# ****
#  ***
#   **
#    *
# D)
#    *
#   **
#  ***
# ****


# Q16
# What is the starting value for 'n' ?
'''
x = range(4)
for n in x:
  print(n)
'''
# A) 4
# B) 1
# C) 0
# D) NULL


# Q17
# What will the final value of 'n' be?
# What will the final value of 't' be?
'''
r = 20
x = 5
t = 0
for n in range(t, r, x):
    t = t + 2
print(n)
print(t)
'''
# A) 10, 20
# B) 20, 10
# C) 8, 15
# D) 15, 8


# Q18
# What should replace 'XXXXXX' in the following code, to make it work?
'''
XXXXXX my_function():
  print("Hello from a function")
'''
# A) func
# B) def
# C) import
# D) funct


# Q19
# T/F: A while loop is used when the number of iterations is known.
# A) True
# B) False


# Q20
# Which of the following is NOT a built in Python data type?
# A) bool
# B) float
# C) string
# D) int
# E) double


# Q21
# Which choice explains what the .split() method will do in the following code?
'''
txt = "seagulls are known for their great style"
x = txt.split()
print(x) 
'''
# A) Split the string into several strings, using whitespace as the separator.
# B) Split the string into a dictionary, using index as the separator.
# C) Split the string into several strings, using 'x'' as the separator.
# D) Split the string into a list, using whitespace as the separator.
# E) Split the string into a single variable, because no separator is provided.


# Q22
# Which of the following options should be used in the IF statement,
# in order to meaningfully trigger the print statment?
'''
value1 = 38.9
value2 = 32.3
value3 = 39.1
if ...
  print("right in the middle")
'''
# A) value3 > value1 and value2 > value1:
# B) value1 > value2 and value1 < value3: 
# C) value2 > value1 and value1 < value3:
# D) value3 < value2 and value1 < value2:


# BONUS Question:
# Which year was Python released?
# A) 1973
# B) 2002
# C) 1987
# D) 1991