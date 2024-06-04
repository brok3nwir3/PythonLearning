# Week 2 - Answer Key

# AVOID PEEKING AHEAD OF TIME!










# Scroll down.
# |
# |
# v




























# Q1
w = -3

# Q2
x = 5
y = 9.2
w = -3
total = w+x
print(total)

# Q3
# The data types that are printed are...
# int, flot, and int.

# Q4
# Python code runs from the top down, similar to when you read a book.
# As the code runs, it eventually hits the print statements and retursn the most recent data types for the variables.

# Q5
# If we know f = "monkey" and index 0 = 'm',
# Then we can write out the index for each letter in the string...
# m = 0, o = 1, n = 2, k = 3, e = 4, y = 5
# Therefore, f[2] should return the letter 'n'.

# Q6
# Using the logic from Q5, you might be wondering why we're using f[2:6] instead of f[2:5].
# The reason is because f[x:y] is specifying a range of indices, but the 'y' portion does not include itself.
# For this reason, we have to specify one number ahead (f[2:6] instead of f[2:5]) in order to get the characters we want.
# Note: f[2:6] returns 'nkey', while f[2:5] returns 'nke' 

# Q7
# The code returns True, False, True.
# Let's take a closer look...

# print(bool(4==4.0))
# Even though 4 might be an integer data type and 4.0 might be a float data type,
# the two numbers evaluate to '4' respectively, thus the expression is True.


# a = 5
# b = 5.1
# print(bool(a==b))
# In this case, 5 is not the same as 5.1.
# Remember double equal symbol '==' means "is equal to".
# Therefore, a==b is False.


# print(bool(15))
# This expression is simply the number 15.
# Any number other than 0, will result to a True boolean expression.
# Note: The number 0 is always considered False.