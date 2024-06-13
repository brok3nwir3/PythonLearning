# Week 6 - The 'range' function, the 'end' parameter, and loops continued.

# Q1
# Examine the following code.
# What number does 'n' start at?
'''
x = range(4)
for n in x:
  print(n)
'''

# Q2
# Examine the following code.
# A) What number will the program start on?
# B) What number will the program stop on?
'''
for n in range(3,8):
  print(n)
'''

# Q3
# Examine the following code.
# A) What will the final value of 'n' be?
# B) What will the final value of 't' be?
'''
t = 0
for n in range(0, 20, 5):
    t = t + 2
print(n)
print(t)
'''

# Q4
# Examine the following code.
# Type out what you think the output of this program will be.
# Run the program and see if your output matches the actual output.
'''
for i in range(5):
	print(i, end=" ")
'''

# Q5
# Bob made this program, but forgot what it does.
# Can you tell what the program does, just by looking at it?
'''
for i in range(3):
    if i % 2 != 0:
        print("", end="_")
    if i % 2 == 0:
        print("", end="0")
'''

# Q6
# Alice created two short lists of some of her favorite adjectives and animals.
# Help Alice write a nested 'for' loop program that prints each adjective next to each animal,
# for a total of nine print statements.

adj = ["elegant", "formidable", "majestic"]
animals = ["penguin", "zebra", "seagull"]



# Q7
# Use a nested 'for' loop to create the following square pattern:
# * * * *
# * * * *
# * * * *
# * * * *

