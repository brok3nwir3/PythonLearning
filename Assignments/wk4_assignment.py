# Week 4 - If statements continued, random library, replace() and format() functions.

# Q1
# Bob learned that he can import a module to generate a random number.
# He started writing a dice rolling program, that roll a number in range 1-6.
# Bob heard about a .range() function for the random library, but Bob hates reading documentation.
# Help him finish his dice rolling program, using the documentation for the random module.
# https://docs.python.org/3/library/random.html
# Note: Bob is using a comma in his print statement in order to print both a string and the value of 'roll'.
'''
import random
roll = ?
print("Your dice roll is... ", roll)
'''

# Q2
# Now that Bob's dice roller is working, set the range to only include numbers 1-20.
# Also, help Bob add some 'if' statements that print different messages based on the dice roll...
# If the dice roll is a 1, a special "CRIT FAIL!" message should print out.
# If the dice roll is a 20, a special "CRIT SUCCESS!" message should print out.
# If the dice roll is any other number, the normal print statement should be used.



# Q3
# Alice loves petting animals. She learned about a random module that selects a choice from a list.
# Alice needs help building a program to help her choose which animal to pet on a given day.
# Her favorite animals are: dogs, cats, elephants, and seagulls.
# The program should select a random one of Alices favorite animals and tell her which one she should pet today.
# Note: You can check the Internet for examples if you get stuck.



# Q4
# Alice was reading some beautiful poetry, but there was a big problem...
# The poem was about lizards and beetles, when it really should've been about seagulls.
# Help Alice write a program to **replace** all instances of the words "lizards" and "beetles."
'''
poem = "Lizards are sly, like wizards. Beetles are dangerous, like needles."
'''



# Q5
# Bob was at work and noticed some crazy person submitted a bunch of code using shorthand if/else statements.
# Help Bob rewrite the code so it's in a normal format.
'''
print("Yes") if 5 > 2 else print("No") 
'''



# Q6
# Alice created a small program that lets a user enter their favorite animal.
# However, she'd like to turn the program into a guessing game.
# If a user can guess her favorite animal, they'll get a special message.
# Modify her program, to ask a user to guess her favorite animal.
# If the users guess is correct, they should see her special message.
# All other cases should return the message "Sorry, incorrect."
'''
alice_fave = "seagull"
special_message = "Correct! You clearly know me well!"
user_choice = input("Enter your favorite animal: ")
print("Your favorite animal is " + user_choice)
'''


# Q7
# Bob read about the built-in Python function called format().
# Then he wrote a program that formats text and then prints it.
# Help Bob extend his current program to include a variable for 'cents'.
# The print statement should also be changed to include both dollars and cents.
'''
dollars = 49
txt = "The price is {} dollars"
print(txt.format(price))
'''


# ---BONUS---

# Q8
# Someone from cybersecurity told Alice she shouldn't write her passwords in plaintext.
# Alice wrote this program to conceal her password.
# Can you figure out what her password is without using print(password) or print(v_c)?
# Also, can you add descriptive comments for each of the steps she took?

#Step1 - ?
v1 = 452
v2 = 207
v3 = 339
v_m = v1 * v2 * v3
#Step2 - ?
v_s = str(v_m)
v_d = v_s[1:6]
v_i = int(v_d)
#Step3 - ?
v_f = format(v_i, 'b')
#Step4 - ?
v_l = ['se', 'agu', 'l','l']
v_l.append(v_f)
#Step5 - ?
v_c = v_l[0]+v_l[1]+v_l[2]+v_l[3]+v_l[4]
password = v_c[:10]



# Homework:

# Read the following articles...
# https://www.w3schools.com/python/python_conditions.asp
# https://www.w3schools.com/python/module_random.asp
# https://www.w3schools.com/python/ref_string_replace.asp
# https://www.w3schools.com/python/ref_func_format.asp


# Complete the following exercises...
# Operators, and IF/ELSE
# https://www.w3schools.com/python/exercise.asp