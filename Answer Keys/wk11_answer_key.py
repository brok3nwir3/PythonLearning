# Week 11 - Answer Key

# AVOID PEEKING AHEAD OF TIME!










# Scroll down.
# |
# |
# v




























#Q1
f = open("wk11_text.txt", "r")
print(f.read())

#Q2
best_animals = []

f = open("wk11_text.txt", "r")
for x in f:
    best_animals.append(x)

print(best_animals)

#Q3
f.close()

#Q4
ea_animals = []

for x in best_animals:
    if "ea" in x:
        ea_animals.append(x)

print(ea_animals)

#Q5
f = open("wk11_text.txt", "w")
for x in ea_animals:
    f.write(x)
f.close()

f = open("wk11_text.txt", "r")
print(f.read())
f.close()