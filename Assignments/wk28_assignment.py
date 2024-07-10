# Week 28 - The .join() function, pickling/unpickling, and the ipaddress module.

# Q1
# Bob was interviewing for a software engineering position at SmallMart. 
# They asked Bob to write a program that identifies the largest number in a list and then prints the number.
# Bob is curious how you would approach this problem.
# Try to solve this problem without using the Internet.
# If you get stuck, then use the Internet.

interview_list = [345, 22, 89, 9, 705, 11, 64, 703]


# Q2
# Bob learned about a helpful function called .join()
# The function allows strings or characters to be joined together.
# All you need to do is make a new empty variable and call the function passing your words/list.
# Help Bob join and print the characters from the following list.

join_list = ['Ice', 'cream', ' is ', 'Bobs ', 'favorite ', "dessert."]


# Q3
# Python has a library called Pickle, which is used to serialize and deserialize data.
# Below is some example code pulled from this article:
# https://machinelearningmastery.com/a-gentle-introduction-to-serialization-for-python/
# Run the code and answer the questions...
# A) What is the extension of the file that's created?
# B) What function is used to serialize the data?
# C) What function is used to deserialize the data?
# D) What is the point of serializing data?
# E) Why is there a warning if you try to view the file created by the code?
'''
import pickle
test_dict = {"Hello": "World!"}
with open("test.pickle", "wb") as outfile:
    pickle.dump(test_dict, outfile)
print("Written object", test_dict)
with open("test.pickle", "rb") as infile:
    test_dict_reconstructed = pickle.load(infile)
print("Reconstructed object", test_dict_reconstructed)
if test_dict == test_dict_reconstructed:
    print("Reconstruction success")
'''

# Q4
# Alice wants to get the sha1sum of her pickle file.
# This will allow her to give receivers a hash to compare the file to, before they open it.
# Help Alice add some code to obtain the hash of her file.
# Expected output...
# {'A': 123, 'B': [1, 2, 3], 'C': {'X': 0, 'Y': 9}}
# 4c687c3fbd47c9665d2c275c253a85d40c98fa8f  my_object.pickle

'''
import pickle
my_object = {'A': 123, 'B': [1, 2, 3], 'C': {'X': 0, 'Y': 9}}
with open('my_object.pickle', 'wb') as f:
    pickle.dump(my_object, f)
with open('my_object.pickle', 'rb') as f:
    loaded_object = pickle.load(f)
print(loaded_object)
'''

# Q5
# Bob is learning about computer networking with Python and the ipaddress module.
# He wrote some code that prints all the IP addresses for a given network.
# Now he wants to add some code to do the following...
# A) Print the count of IP addresses in the given range.
# B) Store the IP addresses in a variable.
# Help Bob update his code.
'''
import ipaddress
net = ipaddress.ip_network('123.45.67.64/27')
for a in net:
    print(a)
'''

# Q6
# Alice found a useful article regarding the 'ipaddress' module:
# https://pyneng.readthedocs.io/en/latest/book/12_useful_modules/ipaddress.html
# Now Alice would like to test some of the things she read from the article.
# Use the article to help Alice perform the following operations...
# A) Determine if the test_address is private
# B) Get the network mask for test_address.
import ipaddress
test_address = ipaddress.ip_interface('1.1.1.1/13')


# Q7
# Bob would now like to use the 'os' module to obtain his internal IP address.
# He knows he could use 'ifconfig,' but he only wants to have the IP address returned in the output, nothing else.
# Help Bob craft a command to return the desired output.
# Example output... 192.168.1.79

import os


# Q8
# Bob is happy with the code that returns his IP address.
# Bob now wants to have the returned IP address stored as a variable.
# Help Bob store the command output to a variable.
# Note: If your variable is storing the value '0', you're on the right track... Check the Internet for help!

import os


# Q9
# Alice wants to parse the result of a ping with Python instead of using some Bash commands.
# Her code currently returns one character of output at a time.
# Help Alice write update her code to recreate the strings, one word per line.
# BONUS: Print a 'packet received' message if the packet was received, and a failure message otherwise.
'''
import os 
test_ping = os.popen("ping -c 1 8.8.8.8 ").read()

for a in test_ping:
    print(a)
'''