# Week 23 - Answer Key

# AVOID PEEKING AHEAD OF TIME!










# Scroll down.
# |
# |
# v




























# Q1
'''
In Python, __assignment__ statements do not copy objects, they create __bindings__ between a target and an object.
When we use the __=__ operator, it only creates a new variable that shares the __reference__ of the original object. 
In order to create “real copies” or “clones” of these objects, we can use the __copy__ module in Python.
'''

# Q2
import copy
c = copy.deepcopy(a)
print(id(c))

# Q3
'''
__Parent__ class is the class being inherited from, also called __base__ class.
__Child__ class is the class that inherits from another class, also called __derived__ class.
'''

# Q4
class condo(property):
    pass

x = condo(123, "East Street", "Columbus", "Ohio", 98765)
x.print_property()

# Q5
class condo(property):
    def __init__(self, address_num, street, city, state, zipcode, rent):
        super().__init__(address_num, street, city, state, zipcode)
        self.rent = rent
        

x = condo(123, "East Street", "Columbus", "Ohio", 98765, 1500)
x.print_property()

# Q6
'''
1. Single
2. Multiple
3. Multilevel
4. Hierarchical
5. Hybrid
'''

# Q7
class condo(property):
    def __init__(self, address_num, street, city, state, zipcode, rent, lease_term):
        super().__init__(address_num, street, city, state, zipcode)
        self.rent = rent
        self.__lease_term = lease_term
        

x = condo(123, "East Street", "Columbus", "Ohio", 98765, 1500, 12)
x.print_property()

# Q8
is_greater = lambda x: x > 100 and "greater than 100" or "less than 100"

# Q9
sorted_by_surname = sorted(name_list, key = lambda x: x.split()[1])