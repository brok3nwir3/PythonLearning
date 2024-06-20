# Week 7 - Answer Key

# AVOID PEEKING AHEAD OF TIME!










# Scroll down.
# |
# |
# v




























# Q1
def hello():
    print('Hello World!')

hello()

# Q2
def greetings(name):
    print("Hello ", name, "!")

greetings('Alice')

# Q3
input1 = input("What is your name? ")
input2 = input("What is your favorite animal? ")

def name_animal(name, animal):
    print(name + "'s favorite animal is " + animal + ".")

name_animal(input1, input2)

# Q4
input_num = input("Enter a number: ")

def even_odd_checker(number):
    if int(number) % 2 == 0:
        print(number, "is an even number.")
    else:
        print(number, "is an odd number.")

even_odd_checker(input_num)

# Q5
# To solve this problem, we first write the sum_calc() function using the *return* parameter.
# Next, we paste the even_odd_checker() function from Q4.
# Finally, we call even_odd_checker() passing the result of (sum_calc(x, y))
# ...where x, y can be any two integers... 4 and 5 in this example.
def sum_calc(one, two):
    sum = one + two
    return sum

def even_odd_checker(number):
    if int(number) % 2 == 0:
        print(number, "is an even number.")
    else:
        print(number, "is an odd number.")

even_odd_checker(sum_calc(4, 5))

# Q6
for animal in best_animals:
    print(animal.upper())

# Q7
# Hide and Seek algorithm...
# A) Determine which players are playing.
# B) Determine the hiding locations.
# C) Determine which of the players will be seekers and hiders.
# D) Have the seekers close their eyes and count to 10.
# E) Have the hiders hide while the seekers count to 10.
# F) Have the seekers check each hiding location until all players are found.
# G) The last hider found is the winner.
    
