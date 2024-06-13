# Week 3 - Answer Key

# AVOID PEEKING AHEAD OF TIME!










# Scroll down.
# |
# |
# v




























# Q1
fruits = ["apple", "banana", "cherry", "kiwi", "grape", "lemon"]
print(fruits[-2]) # This returns 'grape'
# Elaborated...
print(fruits[-1]) # This returns 'lemon'
print(fruits[-3]) # This returns 'kiwi'

# Q2
# As we saw in Week 2, when we slice an object ([x:y]),
# the 'y' value does not include itself.
# In other words, if y=2... [x:2]... this is like saying, "include everything up to item 2." 
# Another explanation...
# https://stackoverflow.com/questions/509211/how-slicing-in-python-works

# Q3
cool_fruits = ["apple", "banana", "cherry", "kiwi", "grape", "lemon"]
print(cool_fruits[2:6])

# Q4
# The code will print...
# "Bob's favorite dog is poodle and his favorite food is pizza"

# Q5
# It looks like Alice is trying to replace index 0 "brick" with "iron".
# The error she's getting is due to the variable type.
# Variable 'materials' is currently set to a type of tuple, i.e. parenthesis.
# In Python, tuples cannot be assigned additional objects later in the program.
# To get around this error, Alice will need to change the data type for 'materials'
# One option would be to use a list, i.e. square brackets.
materials = ["brick", "concrete", "wood"]
materials[0] = "iron"
print(materials)

# Q6
# In this case, Bob is made a variable and set it to a dictionary type, i.e. curly brackets.
# The error that Bob's encountering is related to the key value he tried using with his dictionary.
# Dictionaries require you to give a specific key, in order to retrieve a value.
# In other words, you can't just ask for value 0 or value 4.
# Instead, you have to do something like the following...
very_cool_names = {"student0":"John", "student1":"Sally", "student2":"Greg"}
print(very_cool_names["student0"])

# Q7
# The strip function removes specific characters from a string.
# In this case we had...
# .strip("orange ")
# This means that all the listed characters... o, r, a, n, g, e, and 'space' will be removed.
# This leaves us with the character 'b'.

# Q8
# Simply set Alice's 'x' variable to '3'.
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(3)
print(a[x])

# Q9
# IF statements require at least two lines...
# One line for the expression to evaluate, in this case... if is b > a...
# Another line (or several lines) with something to do if the expression evaluates to True... In this case print a message.
# The lines after the IF statement must be indented.
a = 33
b = 200
if b > a:
    print("b is greater than a")

# Q10
# Alice needs to replace the question mark characters with the 'and' operator.