# Q1
# Bob learned that he can import a module to generate a random number.
# Bob hates reading documentation though.
# Help him finish his dice rolling program, using the documentation for the random module.
# https://www.w3schools.com/python/module_random.asp
import random
print("Your dice roll is... ")

# Q2
# Now that Bob's dice roller is working, set the range to only include numbers 1-20.
# If the dice roll is a 1, a special "CRIT FAIL!" message should print out.
# If the dice roll is a 20, a special "CRIT SUCCESS!" message should print out.
# If the dic roll is any other number, the normal print statement should be used.

# Q3
# Alice loves petting animals. She learned about a random module that selects a choice from a list.
# Alice needs help building a program to help her choose which animal to pet on a given day.
# Her favorite animals are: dogs, cats, elephants, and seagulls.
# The program should select a random one of Alices favorite animals and tell her which one she should pet today.

# Q5
# Alice was reading some beautiful poetry, but there was a big problem...
# The poem was about lizards and beetles, when it really should've been about seagulls.
# Help Alice write a program to **replace** all instances of the words "lizards" and "beetles."
poem = "Lizards are sly, like wizards. Beetles are dangerous, like needles."

# Q6
# Bob was at work and noticed some crazy person submitted a bunch of code using shorthand if/else statements.
# Help Bob rewrite the code.
print("Yes") if 5 > 2 else print("No") 

# Q7
# Alice created a small program that lets a user enter their favorite animal.
# However, she'd like to turn the program into a guessing game.
# If a user can guess her favorite animal, they'll get a special message.
# Modify her program, to ask a user to guess her favorite animal.
# If the users guess is correct, they should see a special message. 
alice_fave = "seagull"
special_message = "You clearly know me well!"
user_choice = input("Enter your favorite animal:")
print("Your favorite animal is " + user_choice)
