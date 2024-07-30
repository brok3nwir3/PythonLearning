# Week 30 - Quiz Answer Key

# AVOID PEEKING AHEAD OF TIME!










# Scroll down.
# |
# |
# v




























# Q1
# A) Pascal Case
# B) Camel Case
# C) In general PEP8 recommends snake case for most things. However, there are some exceptions.
# For example, it's recommended to use pascal case when naming classes. When in doubt, aim for readability.
# https://peps.python.org/pep-0008/#naming-conventions

# Q2
# The default python3 error output tells us the line on which there was a function call error.
# It also tells us the error was a TypeError related to using a '<' with a string and an int.
# When we run the program with mypy, we get a much easier to read error, and a total error count.
# Using mypy, we can also see that there was an expected argument type for the function.
# In large programs or ones that perform complex mathematical operations, mypy is a good debugging tool to use.

# Q3
# You can learn more about debugging with breakpoints here:
# https://learn.microsoft.com/en-us/visualstudio/debugger/using-breakpoints?view=vs-2022

# Q4
j = 5
r = j / 2.5
assert type(r) == int, "Error 'r' is not of type int."

# Q5
# A) Agile and/or Extreme Programming (XP).
# B) The driver and the navigator.
# C) Some advantages include... the code automatically becomes peer reviewed, the technique can be helpful for brainstorming,
# it can be a helpful way to teach junior programmers, and it reduces information silos.
# D) Some drawbacks include... reductions in productivity and slower delivery times, some people prefer to work alone,
# people might work or break at different times, and projects might not receive equal engagement from both people.
# Read more here: https://www.techtarget.com/searchsoftwarequality/definition/Pair-programming

# Q6
# 'pytest' can be helpful way to test complicated code, and works similarly to 'mypy'.

# This function increments a number.
def inc(x):
    return x + 1

# This function tests the above function.
# Passing the number 3 would return 4, and not 5.
def test_answer():
    assert inc(3) == 5
    
# Q7
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr[0,2])

# Q8
# A) 'args' takes non-keyword arguments, while 'kwargs' takes keyword arguments.
# B) The '*' or '**' represent wildcard (i.e. an unknown number of arguments) for a functions parameters.
# C) The keys would be dog1, dog2, and dog3.
# D) def myFun(arg1, **kwargs):
