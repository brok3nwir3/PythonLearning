# Week 3 - Indices continued, slicing, strip() and slice() functions, and intro to IF statements.

# Q1
# When using indices, you can use negative numbers.
# If you use a negative number, you count from -1 (at the end of the string) right to left.
# Like strings, we can specify index values of other objects, like a list (below).
# Uncomment the code below, guess what will be printed, and then run then code.
'''
fruits = ["apple", "banana", "cherry", "kiwi", "grape", "lemon"]
print(fruits[-2])
'''

# Q2
# Selecting specific indices is sometimes referred to as "slicing".
# Any time we include the colon ':' character, we're "slicing" something.
# Recall what we saw in week 2, regarding specifying index ranges.
# Uncomment the code below, guess what will be printed, and then run then code.
'''
fruitie = ("apple", "banana", "cherry", "kiwi", "grape", "lemon")
print(fruitie[0:2])
'''


# Q3
# Uncomment and edit the following print statement, to select "cherry" through "lemon".
'''
cool_fruits = ["apple", "banana", "cherry", "kiwi", "grape", "lemon"]
print(cool_fruits[?])
'''


# Q4
# Print statements sometimes include both strings and variables.
# Uncomment the code below, guess what will be printed, and then run then code.
'''
fave_dog = "poodle"
fave_food = "pizza"
print("Bob's favorite dog is " + fave_dog + " and his favorite food is " + fave_food)
'''


# Q5
# Alice is getting an error her code (below).
# Examine her code and see if you can figure out what she's trying to do.
# See if you can figure out the meaning of the error message.
# Then, help her modify her code to get it working.
'''
materials = ("brick", "concrete", "wood")
materials[0] = "iron"
print(materials)
'''


# Q6
# Bob is getting an error with his code (below).
# Examine his code and see if you can figure out what he's trying to do.
# See if you can figure out the meaning of the error message.
# Then, help him modify his code to get it working.
'''
very_cool_names = {"John", "Sally", "Greg", "Mike"}
print(very_cool_names[0])
'''


# Q7
# Python is full of helpful built-in functions.
# Bob wrote some code to test the strip() function.
# Uncomment the code below, guess what will be printed, and then run then code.
'''
txt = "orange banana"
x = txt.strip("orange ")
print("Of all fruits", x, "is my favorite.")
'''


# Q8
# Alice learned that Python has a slice() function, so she doesn't have to use the normal slice format of [x:y].
# Alice wants to return the first three items in her tuple, but she's getting a syntax error. Help Alice fix her code.
# Check out the example here...
# https://www.w3schools.com/python/ref_func_slice.asp
'''
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(0:3)
print(a[x])
'''


# Q9
# Bob is learning how to use "if" statements, but his code is throwing an error. Help him fix his code.
'''
a = 33
b = 200
if b > a:
print("b is greater than a")
'''

# Q10
# Alice has assigned points to her favorite birds.
# She then created a program to prove seagulls are the best bird.
# However, she needs help fixing her final "if" statement.
# See if you can figure out what to replace the question mark characters with.
# Check online and help Alice finish her code.
'''
eagle = 150
parrot = 300
falcon = 200
seagull = 500
penguin = 350
if seagull > parrot:
   print("A seagull is greater than parrot.")
if falcon > eagle:
   print("A falcon is greater than an eagle.")
if seagull > falcon:
   print("But seagull is even greater than a falcon.")
if seagull > eagle ? seagull > parrot ? seagull > falcon ? seagull > penguin:
   print("Clearly, seagulls are the greatest of all birds.")
'''


# Homework:

# Read the following articles...
# https://www.w3schools.com/python/python_strings_slicing.asp
# https://www.w3schools.com/python/ref_string_strip.asp


# Complete the following exercises...
# Numbers, and Strings...
# https://www.w3schools.com/python/exercise.asp