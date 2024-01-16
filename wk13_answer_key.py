# Week 12 - Answer Key

# AVOID PEEKING AHEAD OF TIME!










# Scroll down.
# |
# |
# v




























# Q1
myit = iter(fruit)
print(next(myit))
print(next(myit))
print(next(myit))

# Q2
myit = iter(animal)
for x in animal:
    print(next(myit))
    #print(x) #Bonus

# Q3
'''
Lists, tuples, dictionaries, and sets are all iterable objects
'''

# Q4
try:
    f = open("game_save_file.txt")
    print("Save file loaded.")
except:
    print("No save file found.")

# Q5
legal_selection = False

while legal_selection == False:
    play_as = input("Will you be 'x' or 'o'?:")
    if play_as != ('x' or 'o'):
        print("Only 'x' or 'o' can be chosen.")
    else:
        legal_selection = True

print("You selection has been made.")

# Q6
age = int(input("What is your human age?:"))

if type(age) is int:
    print("Valid age submitted...")
else:
    raise TypeError("Only integers are allowed")

# Q7
# A)
round_me = 735.99988887
x = round(round_me, 4)
print(x)

# B)
ascii_me = "ÀÎìÇÊ"
print(ascii(ascii_me))

# C)
assortment1 = ('s', 0)
print(all(assortment1))

# D)
assortment2 = (1, 4, 3, 2, 5)
print(sorted(assortment2))