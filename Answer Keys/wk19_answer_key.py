# Week 19 - Answer Key

# AVOID PEEKING AHEAD OF TIME!










# Scroll down.
# |
# |
# v




























# Q1
# PEP stands for Python Enhancement Proposal. 
# A PEP is an official design document providing information to the Python community,
# or describing a new feature for Python or its processes. 
# PEP 8 is especially important since it documents the style guidelines for Python Code.
# Contributing to the Python open-source community requires you to follow these style guidelines.

# Q2
'''
# This is a comment for the code below... 
# blah blah blah blah blah blah blah blah blah 
# blah blah blah blah blah blah
var_f = 17
my_total = 10 + var_f
list_of_numbers = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
    ]
'''

# Q3
def type_check(x):
    if isinstance(x, int) == True:
        print("The data type is integer.")
    else:
        print("Non-integer data type found: ")
        print(type(x))

# Q4
# The object is assigned a memory address.
alice_test = int
print(id(alice_test))
print(alice_test)
# The memory address changes if the object value changes.
alice_test = int(5)
print(id(alice_test))
print(alice_test)


# Q5
# The program returns 2 because there are two lines referencing 'numbers'.
# To increment the reference count to 3, we simply need to add another line that references 'numbers'.
import sys
numbers = [1,2,3]
bob_test1 = numbers
print(sys.getrefcount(numbers))

# Q6
# The three main parts of objects in Python are: Type, Value, and Reference Count.

# Q7
# CPython acts as both an interpreter and a compiler for Python.

# Q8
# The code demonstrates the difference between the plus operator (concatenate)...
# and the comma operator (multiple arguments).
# In other words, using comma makes the print statement treat the items as arguments in a tuple.
# This means the 'x,y' are two distinct elements and will be seperated by a space when printed.

# Q9
# This bit of code sets an index that starts at 1...
# Then the code loops through articles 1-3...
# Each loop iteration prints a formatted version of the article data from JSON.
