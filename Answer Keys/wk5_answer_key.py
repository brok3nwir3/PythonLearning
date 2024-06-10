# Week 5 - Answer Key

# AVOID PEEKING AHEAD OF TIME!










# Scroll down.
# |
# |
# v




























# Q1
# a. How many times will the word "Kerblam" be printed? --> 3
# b. What is the final value of count? --> 6

# Q2
# You can use the 'end' command within a print statement to specify how the print statement will end.
# Without specifying an 'end' parameter, print() defaults to a newline (i.e. \n).
# To solve Alice' problem, we tell the print statements to end with nothing, until the bottom of the loop is reached.
# This allows us to append the "special" print statement to the current line, if the best animal matches.
animals = ["sheep", "golpher", "canary", "seagull", "dog", "squirrel"]
print("A list of great animals...")
for a in animals:
	print(a, end ="")
	if a == animals[3]:
		print(" <-- Also, the best animal.")
	else:
		print()
		
# Q3
fave = "dog"
correct = False
while(correct == False):
    guess = input("What is my favorite animal? ")
    if guess == fave:
        print("Congrats! You guess my favorite animal!")
        correct = True
    else:
        print("Nope! Keep guessing!")

# Q4
# A) 3
# B) 0
# C) 15
        
# Q5
# Here we use a 'for' loop because we're dealing with a finite number of objects in 'num_list'.
num_list = [10, 2, 3, 17, 60, 95]
for num in num_list:
    if num % 2 == 0:
        print(num, "is even.")
    else:
        print(num, " is odd.")

# Q6
# First we create two new empty lists.
# Then we reuse the previous code, but we remove the print statements that were inside the loop.
# Next we use the .append() function to add numbers to the appropriate lists.
# Lastly, we print out our two completed lists. 
num_list = [10, 2, 3, 17, 60, 95]
even_list = []
odd_list = []

for num in num_list:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)
        
print("Th even numbers were:", even_list)
print("The odd numbers were:", odd_list)

# Q7
# The program has a logic error and results in an infinite loop.
# There are several ways you could fix the program...
# One way would be to set 6 to -6.
# Another way would be to increment 'i' instead of decrement (i += 1).

# Q8
# When looping through something with an unknown length (or potentially infinite length) we use 'while' loops.
# 'While' loops do not require you to clearly specify the ending condition ahead of time.
# With 'for' loops we specify a specific ending condition, rather than a vague one.
# When we use 'for' loops we know how many iterations the loop will perform.

# Consider the following example loops...
'''
some_condition = False
while(some_condition != True):
    # Do something...

# Versus...

for x in range(6):
    print(x)
'''

# Note: There will be some cases where we could use either a 'while' loop or a 'for' loop interchangeably.
