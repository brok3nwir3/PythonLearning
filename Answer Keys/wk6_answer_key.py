# Week 6 - Answer Key

# AVOID PEEKING AHEAD OF TIME!










# Scroll down.
# |
# |
# v




























# Q1
# The starting value of 'n' is 0, and it will increment to 1, 2, and finally 3.

# Q2
# A) The program prints 3 first.
# B) The program prints 7 last.
# Note: With range, you can specify multiple parameters..
# ...In this case range(3,8) means start at 3 and stop iterations at 8.

# Q3
# A) 15
# B) 8
# Note: You can indent the two print statements to see how they iterate within the loop.

# Q4
# Because the 'end' parameter is being used, there won't be any new lines; only spaces.
# The output will result in: 0 1 2 3 4

# Q5
# This program will print an 'emoji' style face: 0_0

# Q6
adj = ["elegant", "formidable", "majestic"]
animals = ["penguin", "zebra", "seagull"]

for word in adj:
    for creature in animals:
        print(creature, "is", word)

# Q7
for x in range(4):
    for y in range(4):
        print("*", end=" ") # Print stars with spaces instead of newlines.
    print()                 # Create a new line on completion of each inner loop run.
