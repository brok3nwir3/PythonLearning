### Python Print Loop Programs ###
# Project 2
# Author: Phil van der Linden
# Date: 10/03/2023

# Program 1 Output (Right Triangle):

# *
# **
# ***
# ****


for i in range(5):
    for j in range(i):
        print("*", end="")
    print() # new line after each row


# Program 2 Output (Diamond):

#   *  
#  *** 
# *****
#  *** 
#   *  


n = 3
# Top of the diamond (First three rows).
for i in range(n): #Start at 0, end at 3.
    for j in range(n - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        print('*', end='')
    print()
# Bottom of the diamond (Last two rows).
for i in range(n - 1): #Start at 0, end at 2.
    for j in range(i + 1):
        print(' ', end='')
    for j in range(2*(n - i - 1) - 1):
        print('*', end='')
    print()


# Program 3 Output (Upside-down Pyramid):

# 1010101
#  10101 
#   101  
#    1 


n = 4
for i in range(1, n+1): # Start at 1, end at 5.
    
    for j in range(i-1): # Start at 0, end at 1-1, 2-1, 3-1, 4-1.
        print(' ', end='')
    
    for j in range(2*(n-i)+1): # Start at 0, end at 7, 5, 3, 1.
        if j % 2 == 0:
            print('1', end='')
        else:
            print('0', end='')
    print()


# Some helpful solution references (Q9)...

# How range works: https://www.w3schools.com/python/ref_func_range.asp

# Example solutions here: https://pynative.com/print-pattern-python-examples

# A cool solution to a similar problem:
# https://stackoverflow.com/questions/22287100/how-to-create-patterns-in-python-using-nested-loops