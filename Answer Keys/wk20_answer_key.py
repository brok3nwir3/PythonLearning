# Week 20 - Answer Key

# AVOID PEEKING AHEAD OF TIME!










# Scroll down.
# |
# |
# v




























# Q1
def thing():
    item1 = 1
    item2 = 2
    item3 = 3
    item4 = 4
    item5 = 5
    item6 = 6
    return print(item1), print(item2), \
           print(item3), print(item4), \
           print(item5), print(item6)

thing()

# Q2
def fractal():
    print("\n" + part1 + "\n" + part2 + "\n" + part3 + "\n" + part4 + \
          "\n" + part5 + "\n" + part6 + "\n" + part7 + "\n" + part8 + \
          "\n" + part9 + "\n" + part10 + "\n" + part11 + "\n" + part12)

fractal()

# Q3
print(f"On {day} afternoon, {person} likes to feed the {animal}.")

# Q4
print(f"Today's weather has been {weather[3]}, with temperatures reaching {(((9/5) * temp_c) + 32)} .")

# Q5
'''
a) "Python is an object-oriented programming language."
b) "python breaks down data into individual pieces called objects.
c) "Objects are variables that contain data and functions that can be used to manipulate the data."
d) "An object is like a mini-program inside python, with its own set of rules and behaviors."
e) "Objects are essential for interacting with different python environments, such as libraries and frameworks."
'''

# Q6
'''
a) "A python class is a collection of python objects, along with functions and data related to those objects."
b) "Classes are like templates for creating multiple objects with similar characteristics."
c) "python objects are defined by a keyword called "class"."
'''

# Q7
person2 = Person('Alice', 20)
person2.birthday()

print(person2.name)
print(person2.age)

# Q8
class Person:

    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language

    def birthday(self):
        self.age += 1

person1 = Person('Alex', 24, 'Spanish')
person2 = Person('Alice', 21, 'English')

print(person1.name)
print(person1.age)
print(person1.language)
print(person2.name)
print(person2.age)
print(person1.language)

# Q9
class Person:

    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language

    def birthday(self):
        self.age += 1

    def info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nLanguage: {self.language}")

person1 = Person('Alex', 24, 'Spanish')
person2 = Person('Alice', 21, 'English')
person1.info()