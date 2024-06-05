# Week 4 - Answer Key

# AVOID PEEKING AHEAD OF TIME!










# Scroll down.
# |
# |
# v




























# Q1
# The .randrange() function of the random libary allows us to specify a range for the random numbers.
# In this case we want to include numbers 1-6, or .randrange(1,7) ...meaning we stop before reaching 7.
import random
roll = random.randrange(1,7)
print("Your dice roll is...", roll)


# Q2
import random
roll = random.randrange(1,21)
if roll == 1: 
    print("CRIT FAIL!", roll)
if roll == 20: 
    print("CRIT SUCCESS!", roll)
if roll > 1 & roll < 20:
    print("Your dice roll is...", roll)

# Q3
import random
animals = ["dogs", "cats", "elephants", "seagulls"]
selection = random.choice(animals)
print("Today you should pet:", selection)

# Q4
poem = "Lizards are sly, like wizards. Beetles are dangerous, like needles."
x = poem.replace("Lizards", "Seagulls")
y = x.replace("Beetles", "Seagulls")
print(y)

# Q5
# We should avoid using shorthand IF statements to prevent confusion and make our code more readable.
if 5 > 2:
    print("Yes") 
else:
    print("No")

# Q6
alice_fave = "seagull"
special_message = "Correct! You clearly know me well!"

user_choice = input("Enter Alice's favorite animal: ")
if user_choice == alice_fave:
    print(special_message)
else:
    print("Sorry, incorrect.")

# Q7
dollars = 47
cents = 20
txt = "The price is {} dollars and {} cents."
print(txt.format(dollars, cents))

# ---BONUS---



# Scroll down.
# |
# |
# v









# Q8

# The password is: seagul100

#Step1 - Assign some variables and multiply them.
v1 = 452
v2 = 207
v3 = 339
v_m = v1 * v2 * v3
#Step2 - Convert the original value to a string, extract a subset of characters, and then convert back to int.
v_s = str(v_m)
v_d = v_s[1:6]
v_i = int(v_d)
#Step3 - Convert the current int value to a binary value.
v_f = format(v_i, 'b')
#Step4 - Create a list of strings (i.e. an array) and append the previous binary value to the list.
v_l = ['se', 'agu', 'l','l']
v_l.append(v_f)
#Step5 - Join all of the list items to a single variable, and then set the password to equal the first 9 characters.
v_c = v_l[0]+v_l[1]+v_l[2]+v_l[3]+v_l[4]
password = v_c[:10]