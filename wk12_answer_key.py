# Week 12 - Answer Key

# AVOID PEEKING AHEAD OF TIME!










# Scroll down.
# |
# |
# v




























# Q1
def bob_function(reverse_me):
    reverse_me = reverse_me[::-1]
    print(reverse_me)

bob_function("cat")

# Q2
import math
def alice_function(square_me):
    square_me = math.sqrt(square_me)
    print(square_me)

alice_function(9)

# Q3
def bob_function2(float_me):
    float_me = float(float_me)
    print(float_me)

bob_function2("7")

# Q4
start_num = 3.14
while start_num < 4.0:
    start_num = start_num + 0.02
    print (start_num)

# Q5
def q5_func(start, end):
    q5_output = start
    actual_end = end - 1
    for actual_end in range(start, end):
        q5_output += actual_end + 1
        print(q5_output)

q5_func(1,6)

# Q6
def time():
    import datetime
    x = datetime.datetime.now()
    print(x)

time()