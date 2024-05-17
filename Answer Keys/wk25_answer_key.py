# Week 25 - Answer Key

# AVOID PEEKING AHEAD OF TIME!










# Scroll down.
# |
# |
# v




























# Q1
with open('/etc/passwd') as f:
    try:
        while True:
            line = next(f)
            print(line, end='')
    except StopIteration:
        pass

# Q2
def next_iterator(iterable):
    for item in iterable:
        print(next(test))

next_iterator(items)

# Q3
def simpleGeneratorFun(a): 
    yield a * a
    yield a * a * a
    yield a * a * a * a

x = simpleGeneratorFun(2) 
  
print(next(x)) 
print(next(x)) 
print(next(x))

# Q4
# The permutations module starts with the first part of the iterable, then continues to the next.
# In this case the iterable is the string 'dog'.
# The module begins with the letter 'd', giving all permutations starting with 'd',
# then the program calculates (generates) for 'o' and finally 'g'.

# Q5
from itertools import permutations 
import time

print('--- Letter Combo Guessing Game ---')
print('Choose a five letter combination using a, b, c, d, and e.')
print('You cant use the same letter twice.')
print('Add a comma (,) after each letter, but dont include spaces.')
combo = input("Enter you character combo:\n")
combo_converted = tuple(combo.split(','))

legal_chars = ['a','b','c','d','e']

p = permutations(legal_chars)
iteration_count = 0

start = time.time()
for permutation in list(p):
    print(permutation)
    iteration_count += 1
    if permutation == combo_converted:
        end = time.time()
        print('Match found after', iteration_count, 'iterations.','Execution time:', (end-start) * 10**3, 'ms')
        print('The matching combo was:', permutation)
        break

# Q6
# WFzh2qUjSnaAE

# Q7
# New password entry...
# DOG:WFzh2qUjSnaAE
# New dictionary entry...
# dog

# Q8
def hash_type(input):
    alg = ''
    count = 0
    for char in input:
        if count < 2:
            if char == '$':
                count += 1
            alg += char
    if alg == '$1$':
        print('MD5 algorithm detected:', alg)
    elif alg == '$2a$':
        print('Blowfish algorithm detected:', alg)
    elif alg == '$2y$':
        print('Blowfish algorithm detected:', alg)
    elif alg == '$5$':
        print('SHA-256 algorithm detected:', alg)
    elif alg == '$6$':
        print('SHA-512 algorithm detected:', alg)
    elif alg == '$y$':
        print('Yescrypt algorithm detected:', alg)
    else:
        print('Unknown algorithm detected.')

# Q9
# 1) Why is the function 'toString' required?
# The toString() function joins individual characters.
# 2) Why is an 'if' statement required?
# The IF statement is required to actually print a permutation.
# 3) How is each permutation being printed?
# Individual characters are joined with toString() and then once the IF statement evaluates to TRUE, the string is printed.
# 4) Why are two lines matching in the function's for loop?
# The first list calculates forward traversal of the string, the second line calculates reverse traversal of the string.
# 5) Do you see why using a permutation library is better than trying to manually code permutation?
# Permutations are hellish to calculate from scratch.