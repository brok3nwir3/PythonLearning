# Week 2 - Intro to data types, the type() function, indices, and booleans. 

# Q1
# Variables can be set to different data types.
# For example...
x = 5
y = 9.2

# Try creating a new variable called 'w' and set it to -3 (a negative integer value).



# Q2
# Now create a new variable called 'total'.
# Set this new variable to equal w+x.
# Then, write a print statement for 'total'.



# Q3
# Python includes a built-in function called type().
# This function allows us to check the type of a variable.
# Uncomment the following code. What do you think will be printed?
'''
print(type(x))
print(type(y))
print(type(w))
'''



# Q4
# We can also set variables to be strings.
# For example...
x = "dog"
y = "cat"

# You might notice that these variable names (x and y) were already set earlier in our program (above).
# What do you think will happen if we run the print statements from Q3?
# Uncomment the code, and see if you guessed correctly.
'''
print(type(x))
print(type(y))
print(type(w))
'''



# Q5
# Another important concept in programming is 'indices'.
# Numbers and strings can both have indices.
# For example, suppose we have the following string...
f = "monkey"
# Each letter in the string has an index.
# Letter 'm' would have an index of 0 because it is the beginning character in the string.
# Note: In programming, we start counting at 0, instead of 1.
# In index notation, you would specify the letter 'm' with f[0], i.e. the first character in the string 'f'.
# Uncomment the following code, try to guess what will be printed, and then run the program.

# print(f[2])


# Q6
# When using index notation, we can also specify a range of indices to select.
# We do this by setting a starting index and an ending index.
# Uncomment the following code, try to guess what will be printed, and then run the program.

# print(f[2:6])

# Q7
# Another variable type is a Boolean.
# Booleans are either True or False.
# For example...
mybool = True

# The following print statments include various math expressions, which either result in a True or False statement.
# In other words, they are boolean expressions.
# Note 1: The use of '==' means "is equal to", and is different than a single '=' symbol that assigns a value.
# Note 2: The 'bool()' function simply tells Python to evaluate something as a boolean expression.
# Uncomment the following code, try to guess what will be printed, and then run the program.
'''
print(bool(4==4.0))

a = 5
b = 5.1
print(bool(a==b))

print(bool(15))
'''