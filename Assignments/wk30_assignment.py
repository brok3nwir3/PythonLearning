# Week 30 - Naming styles, testing methods, testing frameworks, and miscellaneous topics.

# Q1
# Bob normally names Python objects using "Snake Case," i.e. my_var, or my_array.
# Snake case is a "naming style" that uses all lower case letters and replaces the space character with an underscore.
# Bob recently read some code that used other naming styles.
# Help Bob identify the names of the following cases...
# A) MyVar, or MyArray
# B) myVar, or myArray
# C) Now determine which format the Python PEP8 style guide suggest be used?


# Q2
# Alice is learning about type hints, and found the following article useful:
# https://www.geeksforgeeks.org/type-hints-in-python/
# She copied the code (below) from the article, which uses type hints.
# Alice wants to compare the default error output to error output from "mypy".
# Install mypy using: pip install mypy
# Then run the program once using: python3 wk30_assignment.py
# And a second time using: mypy wk30_assignment.py
# What differences do you notice with the output?

'''
def factorial(i: int) -> int: # This format means the function receives and returns an int.
    if i<0:
        return None
    if i == 0:
        return 1
    return i * factorial(i-1)
 
print(factorial(4)) # Passing an integer.
print(factorial("4")) # Passing a string.
print(factorial(5.01)) # Passing a float.
'''

# Q3
# Bob wrote some code and now he wants to practice using "breakpoints" in VS Code.
# He learned that you can add a breakpoint in a bunch of different ways, but he likes selecting a line and hitting F9.
# He wants to set breakpoints in his code at both print statements and one within the while loop.
# Help Bob add the breakpoints and then run the Python file with the Python debugger (in the play drop-down).
# Note: The Python debugger may take a moment to load.
# Once the code starts, a small menu will appear at the top of VS Code.
# Use the menu to slowly continue through all breakpoints, using the arrow icon in the menu.
# As you continue, note the changing value of the "w" variable in the top left of the debugger.

'''
print("Spot: 1")

w = 0
while w < 5:
    w += 1

print("Spot: 2")
'''

# Q4
# Alice learned about the "assert" keyword in Python, which helps with debugging.
# Help Alice add an assert statement to her code, to check whether "r" is of type int.
# Also, add a custom assertion error message to explain what is being checked by the assertion.
# This article might be helpful... https://www.w3schools.com/python/ref_keyword_assert.asp

j = 5
r = j / 2.5


# Q5
# Bob heard about a coding technique called "Peer Programming."
# Search the Internet and help Bob answer the following questions...
# A) Which software development techniques are related to peer programming?
# B) What are the names of the two roles in peer programming?
# C) What are the benefits of peer programming?
# D) What are the drawbacks of peer programming?


# Q6
# Alice wants to try a code testing framework she heard about, called "pytest."
# She installed pytest with: pip install pytest
# Then copied the example code here: https://docs.pytest.org/en/stable/
# Lastly, she tested the code using: pytest wk30_assignment.py
# Try it yourself and see what you think.


# Q7
# Bob heard about a module called 'numpy,' which is used to efficiently make arrays and other objects.
# Help Bob make a 2D array using numpy.
# Also add a print statement that prints the object at index [0,2].
# Bob thinks this documentation will be helpful: https://www.w3schools.com/python/numpy/numpy_intro.asp


# Q8
# Bob was given a homework assignment on Python function arguments.
# Bob found an article that might be helpful: https://www.geeksforgeeks.org/args-kwargs-python/
# Help Bob answer the questions below.
# A) What is the difference between args and kwargs?
# B) What does the '*' or '**' represent for a functions parameter?
# C) Which part/s of this code is a "key?": myFun(dog1='Poodle', dog2='Retriever', dog3='Beagle')
# D) How would we write the first line of a function that takes one argument and multiple key word arguments?
