# Week 12 - Answer Key

# AVOID PEEKING AHEAD OF TIME!










# Scroll down.
# |
# |
# v




























# Q1
cakes_made = 0

def make_cake():
    global cakes_made
    cakes_made += 1

make_cake()
print(cakes_made)

# Q2
rows = 4
columns = 4
alice_1d = [1]*columns
print(alice_1d)

# Q3
rows = 4
columns = 4
alice_2d = [[1]*columns]*rows
print(alice_2d)

# Q4
rows = 4
columns = 4
alice_2d = [[1]*columns]*rows
alice_2d[0][0] = 2
print(alice_2d)
# 2D arrays made with the naive method may have issues updating individual items.

# Q5
bob_2d = []
rows = 6
columns = 6
for i in range(rows):
    col = []
    for j in range(columns):
        col.append(1)
    bob_2d.append(col)
print(bob_2d)

# Q6
bob_2d = []
rows = 6
columns = 6
for i in range(rows):
    col = []
    for j in range(columns):
        col.append(1)
    bob_2d.append(col)
bob_2d[0][0] = 2
print(bob_2d)
# Yes, the empty list method (with nested for loops to populate the 2D array)...
# aka list comprehension...
# fixed the issue that occurs using the naive method.

# Q7

