# Week 22 - More w/ Python classes, lambda review, API review, and the array module.

# Q1
# Bob is stuck on a homework question...
'''
car1 = Car("Honda", "Civic", 2012)
In this line of code, car1 is an example of an ____ and Civic is an example of a ____.
'''
# Help Bob remember the terminology to fill in the blanks on his homework assignment.

# Q2
# Bob wrote the Customer class (below).
# Help Bob write a class *function* called "info" to print following...
# "The selected customer is Albert, and is 52 years old."
# The function should make use of self.name and self.age .
'''
class Customer:
  def __init__(self, name, age):
    self.name = name
    self.age = age
'''

# Q3
# Alice is experimenting with Bob's code (Q1).
# She wants to save Bob's class as a stand-alone file and then import it, similar to a module.
# After importing the file, she wants to add a new customer (c2) named Sally, age 29.
# Finally, Alice wants to call the info function for the new user from her main Python file (here).
# Help Alice do this.



# Q4
# Alice is tired of having to use a bunch of commas to return object attributes...
# For example, print(car1.make, car1.model, car1.year).
# Alice saw some code on this page, which shows a function she could add to her class file...
# https://www.w3schools.com/python/python_classes.asp
# Help Alice write a function to simplify the process of printing car1.
# Expected Output: Honda Civic 2012
'''
class Car:
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year

# The new function should be here.

car1 = Car("Honda", "Civic", 2012)

print(car1)
'''

# Q5
# Bob heard that Python lambda functions are "anonymous."
# Unfortunately Bob fell asleep in class and can't remember what makes lambdas anonymous.
# Search the web and write an explanation note for Bob.


# Q6
# Alice wants to write a lambda function that checks whether a number is even.
# The lambda should be followed by a print statement.
# Example output: If your number returns 0, then it is even, your result is: 1

test_num = 7

# Q7
# Bob has an assignment to comment some API code.
# Help Bob fill in the comment blocks below.
'''
# Blah...
import requests
# Blah...
import json
# Blah...
response = requests.get("https://api.isevenapi.xyz/api/iseven/6/")
# Blah...
py_obj = json.loads(response.text)
# Blah...
json_parsed = py_obj['ad']
print(json_parsed)
'''

# Q8
# Alice learned about the array module, which allows for easy creation and editing of 2D arrays.
# She used the module to make a 2D array (below).
# However, Alice would like to print each row without commas or brackets showing in the output.
# Help Alice update her existing code. Expected output...
'''
11 12 5 2 
15 6 10 
10 8 12 5 
12 15 8 6 
'''

from array import *
my2d = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
for row in my2d:
    print(row)

# Q9
# Alice would like to use the insert function to update her array further.
# Help Alice add the following two rows...
'''
New entry for row 0...
[123, 456, 789]
New entry fow row 5...
[987, 654, 321]
'''
