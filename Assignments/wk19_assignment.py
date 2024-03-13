# Week 19 - PEP8, Data type checking, and Python Memory Basics. 

# Q1
# Bob heard about something called PEP8.
# Help Bob figure out what PEP8 stands for and why it's important.



# Q2 
# Bob was reviewing the code in some of his old GitHub repositories.
# He found the code below, which is not PEP8 compliant.
# Bob noticed at least four errors with the code.
# Help Bob rewrite his code to make it PEP8 compliant.
# He thinks this article may be helpful: https://realpython.com/python-pep8/

'''
# This is a comment for the code below... blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah
f = 17
MyTotal = 10 + f
list_of_numbers = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9]
'''

# Q3
# Alice found a new built-in Python function: isinstance()
# The function takes in two arguments.
# The first argument is the data to test.
# The second argument is the the data type to check against.
# Alice wants to use this function to make her own function.
# Her new function will check whether the test data is an integer.
# If the data is not an integer, her code will run the type() function to determine the data type.
# Help Alice create the new function.

'''
# Alice test...
test1 = 'a'
test2 = 5
print(isinstance(test1, int))

new function here...

type_check(test1)
expected output...
"Non-integer type found: 
<class 'str'>"

type_check(test1)
expected output...
This data is an integer.
'''


# Q4
# Alice heard that there's a built-in Python function that returns the memory address of an object.
# Help Alice call the function on the following variables and print their memory addresses.
# Also, help Alice determine what happens in memory if the value of her object changes.

'''
alice_test = 5
print(Add something here...)
print(alice_test)

alice_test += 1
print(Add something here...)
print(alice_test)
'''

# Q5
# Bob learned about module called 'sys' which allows some calls related to the Python Interpreter.
# The module includes a function call 'getrefcount' which returns the number of references an object has.
# Help Bob understand why his current block of code returns '2'. 
# Also, help Bob increment his current reference count to '3'.

'''
import sys
numbers = [1,2,3]
print(sys.getrefcount(numbers))
'''

# Q6
# According to the following article... https://www.honeybadger.io/blog/memory-management-in-python/
# Objects in Python have three main parts.
# CRTL+F "Objects in Python" and determine what those three parts are.


# Q7
# According to the previous article, what acts as "both an interpreter and a compiler" for Python?


# Q8
# Lesson Item: Plus sign vs. Comma.
# Examine the following code.
# Use the Internet to determine the difference between comma and plus sign.

'''
x = 'hello'
y = 'world'
z = x+y
print(z)
print(x,y)
'''

# Q9
# Examine the code in this article, in section "Working with JSON Data"...
# https://www.geeksforgeeks.org/python-api-tutorial-getting-started-with-apis/
# What do the following lines of code achieve?

'''
for index, article in enumerate(articles[:3], start=1):
    print(f"Article {index}:\n{json.dumps(article, sort_keys=True, indent=4)}\n")
'''
