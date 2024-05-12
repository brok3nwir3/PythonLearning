# Week 23 - Shallow vs deep copy, copy module, 

# Q1
# Bob needs help with a homework question regarding copying variables.
# Search online to help Bob fill in the blanks...
'''
In Python, _____ statements do not copy objects, they create _____ between a target and an object.
When we use the _____ operator, it only creates a new variable that shares the ______ of the original object. 
In order to create “real copies” or “clones” of these objects, we can use the _____ module in Python.
'''

# Q2
# Alice learned that when you set a variable equal to another variable,
# a shallow copy is made, i.e. a reference to the original.
# Alice heard that you can use the copy module to create a clone (deep copy) of the original variable.
# Help Alice finish her code to make a clone of her variable 'a'.

a = [100]
b = a

print(id(a))
print(id(b))

'''
Use the copy module here, to make an actual clone of variable 'a'.
import ???
c = copy.deepcopy(???)
print(id(???))
'''

# Q3
# Bob is learning about inheritance and needs to some with his homework.
# Help Bob fill in the blanks...

'''
_____ class is the class being inherited from, also called _____ class.
_____ class is the class that inherits from another class, also called _____ class.
'''

# Q4
# Alice wrote a class for some housing properties.
# However, she'd like to make a new inherited class called 'condos'.
# Help Alice make the new class, using the 'pass' keyword within the new class.
# Once the new class is made, add a new condo property and call the function that's in the original class.

'''
class property():
    def __init__(self, address_num, street, city, state, zipcode):
        self.address_num = address_num
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def print_property(self):
        print(self.address_num, self.street, self.city, self.state, self.zipcode)
'''

# Q5
# Alice decided she wants to update the condo class (Q4).
# Read about the 'The super() Function' in this article Alice found...
# https://www.geeksforgeeks.org/python-super/
# Replace the 'pass' keyword in the condo class, and add the required attributes, plus the 'super' function.
# The updated class should also include a new attribute called 'rent'.
# Help Alice update the condo class and add a new condo entry.
# Finally, add a rent value for the new object, and then call the print_property() function.
# Note: You won't see the value for rent when you call the print_property() function.

'''
class property():
    def __init__(self, address_num, street, city, state, zipcode):
        self.address_num = address_num
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def print_property(self):
        print(self.address_num, self.street, self.city, self.state, self.zipcode)
'''


# Q6
# Bob looked over Alice's shoulder while she was reading... https://www.geeksforgeeks.org/inheritance-in-python/
# He noticed the article she was reading mentioned there are five types of inheritance.
# What are the names of the five types?

'''
1. 
2. 
3. 
4. 
5. 
'''

# Q7
# Bob wants to practice working with Python classes.
# He saw the code Alice was working on, and wants to add a new attribute to the condo class.
# However, the new attribute should be private.
# Help Bob add a private 'lease_term' attribute to the code Alice was working on.
# Lastly, create an object that has all 7 of the arguments required for condo.

'''
class property():
    def __init__(self, address_num, street, city, state, zipcode):
        self.address_num = address_num
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def print_property(self):
        print(self.address_num, self.street, self.city, self.state, self.zipcode)
'''

# Q8
# Alice is practicing with Python lambdas.
# She wants to write a lambda (is_greater) that checks whether a given number is greater than 100.
# Inside the lambda she also wants to include text that will print.
# However, she wants to include the text to be printed within her lambda.
# Alice wrote two test cases below.
# The first test should return: 'less than 100'.
# The second test should return: 'greater than 100'
# Help Alice create the lambda.

'''
is_greater = ???
print(is_greater(20))
print(is_greater(200))
'''

# Q9
# Alice has one more lambda she wants to create.
# Currently her code sorts by first name.
# Alice wants to use a lambda function as a *key* paramter within the sorted() function.
# The lambda within the key parameter will tell the sorted() function which part of the list to select on.
# This will allow her code to sort names by the first character of the last name, instead of the first name.
# Expected Output: ['Marie Curie', 'Grace Hopper', 'Ada Lovelace', 'Emmy Noether']

'''
name_list = ['Grace Hopper', 'Ada Lovelace', 'Emmy Noether', 'Marie Curie']
sorted_by_surname = sorted(name_list)
print(sorted_by_surname)
'''