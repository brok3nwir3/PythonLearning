# Week 14 - A short mulitple choice quiz for 2D arrays.

# Q1
# Which of the following would be considered a 1D array in Python?

# A) string
# B) function
# C) list
# D) variable
# E) library

# Q2
# Which of the following best describes a 2D array?

# A) An expanded dictionary.
# B) Imported storage.
# C) Benevolent crustaceans. 
# D) Cascading functions.
# E) A list of lists.

# Q3
# Which of the following would most likely be a use case for a 2D array?

# A) A start-up script.
# B) A random number generator.
# C) A port scanner.
# D) A word guessing game.
# E) A grid of daily temperature spikes.

# Q4
# T/F: The following data could be converted to a 2D array.
'''
Day 1 - 11 12 5 2 
Day 2 - 15 6 10 
Day 3 - 10 8 12 5 
Day 4 - 12 15 8 6 
'''
# A) True
# B) False

# Q5
# What will be returned by the following code?
'''
N = 5
ar = [0]*N
print(ar)
'''
# A) 0
# B) 00000
# C) [0]
# D) NULL
# E) [0, 0, 0, 0, 0]

# Q6
# What will be printed by the following code?
'''
from array import *
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
print(T[1][2])
'''
# A) 12
# B) [15, 6,10], [10, 8, 12, 5]
# C) 2
# D) 10
# E) 6

# Q7
# What will be returned by the following code?
'''
from array import *
T = [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]
T.insert(2, [0, 5, 11, 13, 6])
print(T)
'''
# A) [[11, 12, 5, 2], [0, 5, 11, 13, 6], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]
# B) [[11, 12, 5, 2], [15, 6, 10], [0, 5, 11, 13, 6], [10, 8, 12, 5], [12, 15, 8, 6]]
# C) [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [0, 5, 11, 13, 6], [12, 15, 8, 6]]
# D) 11, 12, 5, 2, 15, 6, 10, 10, 8, 12, 5, 0, 5, 11, 13, 6, 12, 15, 8, 6

# Q8
# Manually initializing and populating a list without using any advanced features or constructs in Python is known as creating a 1D list using...

# A) Slicing
# B) Naive Methods
# C) Concatenating
# D) Casting
# E) Iterating

# Q9
# What will be returned by the following code?
'''
rows, cols = (5, 5)
arr = [[0]*cols]*rows
print(arr)
'''
# A) [0, 0, 0, 0, 0]
# B) 00000
# C) 00000, 00000, 00000, 00000, 00000
# D) NULL
# E) [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]

# Q10
# Which of the following options would be invalid for the given 2D array?
'''
w = 8
h = 5
Matrix = [[0 for x in range(w)] for y in range(h)] 
'''
# A) Matrix[0][0] = 1
# B) Matrix[6][0] = 3
# C) Matrix[0][6] = 3
# D) Matrix[3][3] = 11
# E) Matrix[4][7] = 33