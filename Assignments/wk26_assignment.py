# Week 26 - Getters, setters, deleters, decorators, and more w/ classes.

# Q1
# Alice is creating a new Python class for manipulating user info on her website.
# She needs to create a 'user' class with properties: username, password, and email address.
# Users receive their temp login password after confirming email address.
# New user objects should be created using a password placeholder variable that has a value of '1'.
# Then, all new accounts get a randomly generated number for their initial account password.
# The random number should be between: 99,999 - 999,999.
# The password should be printed with a 'getter' function called user_temp_email_pw().
# Help Alice make the class, with the required properties, and an 'RNG' password that replaces the placeholder value.
# Also, be sure to create a 'getter' function...
# Sample user_temp_email_pw() function output: "Temp RNG password check for username --> john2121 PW: 338122"
# Alice thinks some of the information in this article might be helpful...
# https://www.geeksforgeeks.org/getter-and-setter-in-python/
'''
import random

class user:
    #...


placeholder = 1
user1 = user(username='john2121', password=placeholder, email='john@gmail.com')
user1.user_temp_email_pw()
'''


# Q2
# Now Alice wants to update the user class to include both a 'setter' and 'deleter' function.
# Once a new user has activated their account, the delete function should remove the temp password value (del_pw()).
# Then the setter function should set the new password equal to what the user entered on the website (set_pw()).
# Help Alice create the two new functions and then call them.
'''
import random

class user: 
    #...



placeholder = 1
user1 = user(username='john2121', password=placeholder, email='john@gmail.com')
user1.print_user()

user1.del_pw()
website_value = 'Johnny2121!'
user1.set_pw(website_value)
'''

# Q3
# Bob is learning about all the ways functions can be used.
# His homework assignment is to read the following article and then answer some questions...
# https://www.geeksforgeeks.org/decorators-in-python/
# Help Bob answer his homework questions.
'''
def hello():
    print("Hello World")

print(isinstance(hello(), object))
'''
# a. This is an example of?...

'''
some_func(other_func())
'''
# b. This is an example of?...

'''
test = my_func()
'''
# c. This is an example of?...

'''
def func1():
    def func2():
'''
# d. This is an example of?...

'''
temp = [1, my_func(), 3]
'''
# e. This is an example of?...

# Q4
# Bob is learning about decorators.
# Examine the code below, from her homework assignment.
# Help Bob answer the following questions:
# a) What is a decorator function?
# b) What are decorators usually applied to?
# c) Which function is the decorator in the code below?
# d) What is the other name for a decorator?
'''
def func1(func):

	def func2():
		print("This is before inner function execution.")

		func()

		print("This is after inner function execution.")
		
	return func2


def func3():
	print("This during the inner function execution.")


test = func1(func3)
test()
'''

# Q5
# Bob needs to write a function that calls another function within itself.
# The original function doubles a number.
# The new function needs to double the doubled number, and be named double_double().
# The new function should also call the original function to do this.
# Help Bob write the function.
'''
def double(x):
    x = x**2
    return x

# New function here.

test = 10
print(double(test)) # This should print 100.
print(double_double(test)) # This should print 10000.
'''

# Q6
# Now Bob needs to create a wrapper function.
# The original function doubles a number.
# The new function should wrap around the original and print the original number doubled twice.
# Help Bob write the function.
'''
# Wrapper function here...
    def double(x):
        print(x**2)

test = 10
double_double(test) # This should print 10000.
'''