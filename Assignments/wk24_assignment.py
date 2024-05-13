# Week 24 - Packing and unpacking data.

# Q1
# Bob learned that you can easily "unpack" data in Python.
# Unpacking lets you assign a bunch of data from one variable to multiple variables.
# For example...
'''
p = [5, 8]
x, y = p
print(x)
print(y)
'''
# Help Bob unpack the data below into variables with names that make sense for the data.
# Then print the name variables in a single print statement.

q = ['dog', 'cat', 'John', 32]


# Q2
# Bob came across some more interesting data that he'd like to unpack.
# Help Bob unpack the data below into variables, then print the name variables in a single print statement.

h = ['a', 'b', 'c', 5, (1, 3, 7)]


# Q3
# Bob heard that you can use a wildcard (*) when unpacking.
# The wildcard allows you to unpack data in groups.
# Help Bob unpack the data below into the three variables, and then print the variables with a single print statement.

e = ['apple', 2, 3, 4, 5, 'orange']


# Q4
# The opposite of 'unpacking' data is to simply 'pack' data.
# Help Bob pack the following data, then print the new packed data.
# Also, check the data type of the packed data using the built-in type() function.

var1 = 1
var2 = 2
var3 = 3


# Q5
# Alice has a part time job as a teachers assistant.
# The teacher she works with has asked her to determine the class average for each student.
# However, the teacher has asked Alice to drop the first and last grades for each student.
# Alice wants to write a Python function to help her calculate the grades of each student.
# Alice thinks she can use her knowledge of unpacking, sum(), and len() to write the function.
# Help Alice write her function.
'''
student1_grades = [70, 65, 82, 90, 75, 84, 72]

def drop_first_last(grades):
    #...

drop_first_last(student1_grades)
'''

# Q6
# Alice is happy with her function, but needs to run the function for all the students now.
# The grades of all five students are below.
# Help Alice add all of these grades to an array, then write a loop to call her function for each student.

'''
student1_grades = [70, 65, 82, 90, 75, 84, 72]
student2_grades = [65, 61, 70, 73, 72, 68, 61]
student3_grades = [80, 91, 93, 85, 87, 79, 73]
student4_grades = [94, 100, 100, 99, 97, 98, 95]
student5_grades = [73, 84, 90, 76, 93, 81, 74]

def drop_first_last(grades):
    #...

'''

# Q7
# Finally, Alice would like to append either 'FAIL' or 'PASS' to each student grade.
# If a student scored below a 70, they should be marked as FAIL, otherwise PASS.
# Help Alice update her function to include the additional logic.
# Note: This only requires new lines to be added, you won't need to delete any existing code.
'''
student1_grades = [70, 65, 82, 90, 75, 84, 72]
student2_grades = [65, 61, 70, 73, 72, 68, 61]
student3_grades = [80, 91, 93, 85, 87, 79, 73]
student4_grades = [94, 100, 100, 99, 97, 98, 95]
student5_grades = [73, 84, 90, 76, 93, 81, 74]

def drop_first_last(grades):
    #...

'''

# Q8
# ---BONUS---
# Unpacking data becomes especially useful when combined with string processing, such as slicing.
# Consider the following code, which parses the useful information from a line of a file...
'''
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname, homedir, sh)
'''
# Linux environments store passwords within the etc/shadow file with the following format:
# Username:Password:fields...
# Write a program that does the following:
# 1. Switch to the '/etc' directory.
# 2. Write a function that parses the lines of a shadow file and prints username+password for each line.
# 3. Have the function exclude lines that do not contain an encrypted password, i.e. '!' or '*' listed as the password.
# 4. Open the /etc/shadow file and run the unpacking/parsing function against each line.
# Note: You will need to run your program with sudo, i.e. 'sudo python3 shadow_extractor.py'
# This program can be written in less than 20 lines.