# Week 21 Quiz - Answer Key

# AVOID PEEKING AHEAD OF TIME!










# Scroll down.
# |
# |
# v




























# Q1
my_2d = []
rows = 5
columns = 5
for i in range(rows):
    col = []
    for j in range(columns):
        col.append('x')
    my_2d.append(col)
print(my_2d)


# Q2
for row in my_2d:
        print(row)


# Q3
import requests
import json
response = requests.get("https://api.isevenapi.xyz/api/iseven/6/")
py_obj = json.loads(response.text)
json_parsed = py_obj['ad']
print(json_parsed)


# Q4
# D) Type, Value, and Reference Count.


# Q5
x = 1
y = 2
z = x+y
print(z)
print(x,y)


# Q6
print("Really big string... " \
     "spanned to multiple lines...")


# Q7
print(f"There are {5} working days in a week, {52} working weeks in a year, which gives us {5 * 52} working days in a year.") 


# Q8
my_2d = []
rows = 5
columns = 5
for i in range(rows):
    col = []
    for j in range(columns):
        if i % 2 == 0:
            col.append('y')
        else:
            col.append('x')
    my_2d.append(col)
print(my_2d)


# Q9
class Car:

    def __init__(self, make, model):
        self.make = make
        self.model = model

car_1 = Car('Ford', 'F-150')

print(car_1.make)
print(car_1.model)


# Q10
class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

car_1 = Car('Ford', 'F-150', 2014)

print(car_1.make, car_1.model, car_1.year)
