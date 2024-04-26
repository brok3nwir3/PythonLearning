# Week 22 - Answer Key

# AVOID PEEKING AHEAD OF TIME!










# Scroll down.
# |
# |
# v




























# Q1
'''
car1 = Car("Honda", "Civic", 2012)
In this line of code, car1 is an example of an _object_ and Civic is an example of a _attribute_.
'''

# Q2
class Customer:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def info(self):
    print("The selected customer is " + self.name + ", and is " + str(self.age) + " years old.")

c1 = Customer("Albert", 52)
c1.info()

# Q3
from wk22_class import Customer

c2 = Customer("Sally", 29)
c2.info()

# Q4
class Car:
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year

  def __str__(self):
    return f"{self.make} {self.model} {self.year}"

car1 = Car("Honda", "Civic", 2012)

print(car1)

# Q5
# Python lambda functions are described as "anonymous" because they have no defined name,
# A normal function includes a name. For example: myfunc()

# Q6
test_num = 7
even_check = lambda x: x % 2
print("If your number returns 0, then it is even, your result is:", even_check(test_num))

# Q7
'''
# The requests module allows you to send HTTP requests using Python.
import requests
# Python has a built-in package called json, which can be used to work with JSON data.
import json
# requests.get makes a GET request to a web page.
response = requests.get("https://api.isevenapi.xyz/api/iseven/6/")
# The json.loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary.
py_obj = json.loads(response.text)
# This variable pulls a specific string from the Python dictionary (used above).
json_parsed = py_obj['ad']
print(json_parsed)
'''

# Q8
from array import *
my2d = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
for row in my2d:
    for item in row:
        print(item,end = " ")
    print()

# Q9
from array import *
my2d = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
my2d.insert(0, [123, 456, 789])
my2d.insert(5, [987, 654, 321])
for row in my2d:
    for item in row:
        print(item,end = " ")
    print()
