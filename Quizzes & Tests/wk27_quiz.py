# Week 27 Quiz - A review of week 22-26 content.


# Q1
# The following code is an example of?...
'''
def new_username(self, a): 
    self.username = a
    print("New username:", self.username)
'''
# A) Getter
# B) Creator
# C) Deleter
# D) Setter


# Q2
# How would you describe the following code snippet?
'''
some_func(other_func())
'''
# A) A function being defined within another function.
# B) A function being stored within a variable.
# C) A function being passed to another function.
# D) A function being an instance of type object.
# E) A function being stored within a list.


# Q3
# What is the following an example of?
'''
a = [5, 8]
x, y = a
'''
# A) Slicing
# B) Parameterizing
# C) Assignment Exchange
# D) Unpacking
# E) Packing


# Q4
# Which of the following libraries would be helpful for rearranging elements into different configurations?
# A) permutations
# B) os
# C) copy
# D) array
# E) crypt


# Q5
# Which of the following 'user1' objects are invalid?
class user: 
    def __init__(self, attribute1, attribute2, attribute3, attribute4=None):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        self.attribute3 = attribute3
        self.attribute4 = attribute4
    
    def my_print(self):
        print(self.attribute1, self.attribute2, self.attribute3, self.attribute4)

# A) user1 = user(attribute1='abc', attribute2=4567, attribute3='eeeee', attribute4=99)
# B) user1 = user(attribute1='abc', attribute2=4567, attribute3='eeeee')
# C) user1 = user('abc', 4567, 'eeeee')
# D) user1 = user(1, 1, 1, 1)
# E) All of these objects (A-D) are valid.


# Q6
# What will the following code print?
'''
items = ['H', 44, 'Q', 717, 'R']
test = iter(items)
print(next(test), next(test))
'''
# A) H
# B) 44 Q
# C) 0 H
# D) H 44


# Q7 In the following code, var4 is an example of?...
'''
var1 = 1
var2 = 2
var3 = 3
var4 = var1,var2,var3
'''
# A) Packing
# B) Severing
# C) Reallocation
# D) Retrieval
# E) Unpacking


# Q8
# Which library would be required to run the following code?
'''
my2d = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
my2d.insert(0, [123, 456, 789])
'''
# A) permutations
# B) os
# C) copy
# D) array
# E) crypt


# Q9
# The five types of inheritance are...
# A) Aligned, Hierarchical, Single, Multiple, Tiered
# B) Hybrid, Hierarchical, Single, Multiple, Multilevel
# C) Hybrid, Deducted, Single, Reciprocated, Multi-step
# D) Spatial, Hierarchical, Individual, Multiple, Multilevel


# Q10
# Which part of the following lambda is equivalent to an 'else' clause in a normal function?
'''
is_greater = lambda x: x > 100 and "greater than 100" or "less than 100"
'''
# A) x:
# B) and
# C) x >
# D) or
# E) =