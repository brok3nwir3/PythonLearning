# Week 26 - Answer Key

# AVOID PEEKING AHEAD OF TIME!










# Scroll down.
# |
# |
# v




























# Q1
import random

class user: 
    def __init__(self, username, password, email):
        self.username = username
        self.password = random.randrange(99999,999999)
        self.email = email

    def user_temp_email_pw(self):
        print("Temp RNG password check for username -->", self.username, "PW:", self.password)

placeholder = 1
user1 = user(username='john2121', password=placeholder, email='john@gmail.com')
user1.user_temp_email_pw()

# Q2
import random

class user: 
    def __init__(self, username, password, email):
        self.username = username
        self.password = random.randrange(99999,999999)
        self.email = email

    def user_temp_email_pw(self):
        print("Temp RNG password check for username -->", self.username, "PW:", self.password)
    
    def del_pw(self): 
        del self.password

    def set_pw(self, a): 
        self.password = a
        print("New password set w/ setter function:", self.password) 


placeholder = 1
user1 = user(username='john2121', password=placeholder, email='john@gmail.com')
user1.user_pw_check()

user1.del_pw()
website_value = 'Johnny2121!'
user1.set_pw(website_value)

# Q3
# a. This is an example of?... A function being an instance of type object.
# b. This is an example of?... A function being passed to another function.
# c. This is an example of?... A function being stored within a variable.
# d. This is an example of?... A function being created within another function.
# e. This is an example of?... A function being stored within a list.

# Q4
# a) What is a decorator function?... 
# --> Code that allows a user to add new functionality to an existing object without modifying its original structure.
# b) What are decorators usually applied to?... 
# --> Functions
# c) Which function is the decorator in the code below?...
# --> func1()
# d) What is the other name for a decorator?...
# --> Wrapper

# Q5
def double(x):
    x = x**2
    return x

def double_double(y):
    y = double(y)
    y *= y
    return y

test = 10
print(double(test))
print(double_double(test))

# Q6
def double_double(x):
    x = x**2
    def double(x):
        print(x**2)
    double(x)

test = 10
double_double(test)

