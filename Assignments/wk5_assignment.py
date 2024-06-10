# Week 5 - Loops, the 'end' paramater, and modulo.

# Q1
# a. How many times will the word "Kerblam" be printed?
# b. What is the final value of count?
'''
count = 0
while (count < 5):
	count = count + 2
	print("Kerblam!")
print("The final value of count is:", count)
'''

# Q2
# Alice created a program that prints out great animals.
# Her program also prints a special line for the best animal.
# However, she wants the program to print the special line on the same line as the best animal.
# Can you figure out how to help her?
'''
animals = ["sheep", "golpher", "canary", "seagull", "dog", "squirrel"]
print("A list of great animals...")
for a in animals:
  print(a)
  if a == animals[3]:
    print(" <-- Also, the best animal.")
'''

# Q3
# Bob wants to make an animal guessing game with the following requirements...
# Set a variable equal to your favorite animal (string).
# Make the program take a users input as a guess.
# If the users guess matches your favorite animal, the program exits (loop ends).
# If the guess is wrong, the program will continue running until a correct guess is made.


# Q4
# Modulo...
# Modulo (%) is an arithmetic operation, like subtraction, addition, multiplication, or division.
# Modulo returns the remainder of two numbers that have been divided.
# For example: 10 mod 2 = 0 (no remainder), and 10 mod 3 = 1 (a remainder of 1).
# What are the results of the following modulo problems?

# A)
'''
num1 = 13
num2 = 5
result1 = num1 % num2
print(result1)
'''

# B)
'''
num3 = 20
num4 = 2
result2 = num3 % num4
print(result2)
'''

# C)
'''
num5 = 15
num6 = 30
result3 = num5 % num6
print(result3)
'''

# Q5
# Even-Odd Checker...
# Bob has a list of numbers and needs to quickly determine which numbers in the list are odd.
# Bob noticed that if you use "x mod 2" on any number, it will either return '0' (even) or '1' (odd).
# Help Bob write a program that uses a loop to iterate through his list.
# The program should print "[x] is an even number" or "[x] is an odd number"
# The program should stop, once all numbers have been categorized.
num_list = [10, 2, 3, 17, 60, 95]


# Q6
# Even-Odd Sorter...
# Now that Bobs program is successfully detecting even and odd numbers, he wants to enhance the program further.
# In this spin-off program, Bob wants to create two new lists, one for even numbers and one for odd numbers.
# Bob thinks he can use the .append() function to add items to his two new lists.
# Help Bob write the new program.
num_list = [10, 2, 3, 17, 60, 95]


# Q7
# What's the problem with this code? How would you fix it?
# Note: You can se CTRL+C to close the program, if needed.
'''
i = 1
while i <= 6:
	print(i)
	i -= 1
'''

# Q8
# Bob is wondering... What's the difference between a for loop and a while loop?
# How would you explain the difference to him?



# Homework:

# Read the following articles...
# https://www.w3schools.com/python/python_while_loops.asp
# https://www.w3schools.com/python/python_for_loops.asp
# https://www.freecodecamp.org/news/the-python-modulo-operator-what-does-the-symbol-mean-in-python-solved/
# https://www.geeksforgeeks.org/print-without-newline-python/
# https://www.w3schools.com/python/ref_list_append.asp

# Complete the following exercises...
# Lists, While Loops, and For Loops.
# https://www.w3schools.com/python/exercise.asp

# *** Start Project 1 ***
# See the Projects folder.