# Week 20 - Objects, Classes, and Formatting data.

# Q1
# Alice found this strange function online.
# She thinks the return line is too long.
# Help Alice reformat the return line to span multiple lines, rather than one long line.

'''
def thing():
    item1 = 1
    item2 = 2
    item3 = 3
    item4 = 4
    item5 = 5
    item6 = 6
    return print(item1), print(item2), print(item3), print(item4), print(item5), print(item6)

thing()
'''

# Q2
# Bob is a fan of ASCII art, and recently found a cool ASCII fractal.
# Bob wants to be able to call the fractal art using a function.
# Help Bob make a function called fractal(), to print the art he found.
# Bonus: Have the function span the print statement across three lines.

part1="      __/\__ "
part2="      \    /   "
part3="__/\__/    \__/\__"
part4="\                /"
part5="/_              _\ "
part6="  \            /"
part7="__/            \__ "
part8="\                /"
part9="/_  __      __  _\ "
part10="  \/  \    /  \/"
part11="      /_  _\ "
part12="        \/"


# Q3
# Alice is learning about f-strings.
# Help Alice write an f-sting print statement, using the variables below.
# Expected Output: On Monday afternoon, Alice likes to feed the Seagulls.

'''
day = "Monday"
person = "Alice"
animal = "Seagulls"

print(f"")
'''

# Q4
# Alice is doing more practice with f-strings.
# Alice wants to do the celsius to fahrenheit calculation within her print statment.
# Help Alice write an f-sting print statement, using the variables below.
# Expected Output: Today's weather has been apocalypse, with temperatures reaching 100.4 .

'''
weather = ['cloudy', 'windy', 'sunny', 'apocalypse']
temp_c = 38

print(f"")
'''

# Q5
# Lesson item: Python Objects
# Read this article - https://blog.hubspot.com/website/python-object
# Then fill in the blanks...
'''
a) "Python is an ____ programming language."
b) "python breaks down data into individual pieces called ___.
c) "Objects are variables that contain ___ and ___ that can be used to manipulate the data."
d) "An object is like a ___ inside python, with its own set of rules and behaviors."
e) "Objects are essential for interacting with different python environments, such as ___ and ___."
'''

# Q6
# Lesson item: Python Classes
# Read this article - https://blog.hubspot.com/website/python-object
# Then fill in the blanks...
'''
a) "A python class is a collection of python objects, along with ___ and ___ related to those objects."
b) "Classes are like ___ for creating multiple objects with similar characteristics."
c) "python objects are defined by a keyword called ___."
'''

# Q7
# Alice read this article about classess - https://blog.hubspot.com/website/python-object
# She liked the class called 'Person'.
# Now she wants to create 'person2' using the 'Person' class.
# She wants person2 to be named Alice and with an age of 20.
# Help Alice create a person2 object.



# Q8
# Alice wants to add another function to the Person class.
# She thinks there should be a "language" attribute to specify the language a person speaks.
# Help Alice update the class and define Alex's language as Spanish, and Alice's language as English.



# Q9
# Bob saw Alice's update Person class and thinks it needs a new function.
# Instead of having to manually printing out each object attribute, Bob wants to make a function that does this.
# The new class function should be called info().
# Help Bob make the new function.
# Bonus: Have the function use f-strings.
# Expected output for person1...
'''
Name: Alex
Age: 24
Language: Spanish
'''
