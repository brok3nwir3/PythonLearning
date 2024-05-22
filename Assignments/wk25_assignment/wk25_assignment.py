# Week 25 - Iterables, iterators, generators, permutations, execution time, and the crypt library.

# Q1
# Bob is learning about iterators.
# Iterators are small bits of code that iterate over an iterable object.
# For example, the following code demonstrates an iterable object and an iterator...
'''
a = [1, 2, 3, 4]

def iterator_example(iterable):
    for item in iterable:
        print(item)

iterator_example(a)
'''
# Bob figured out that a file with multiple lines can be considered an iterable.
# Bob wrote some iterator code to iterate through the lines of a given file.
# But he's encountering an error at the end of his programs execution.
# Help Bob add a try/except statement to fix his code.
'''
with open('/etc/passwd') as f:
    while True:
        line = next(f)
        print(line, end='')
'''

# Q2
# Bob discovered that Python has a built in iterator function called iter().
# The function can also use next() to manually iterate through and iterator.
# Bob tested the the functions with the following code...
'''
items = [1, 2, 3, 4]
test = iter(items)
print(test)
print(next(test), next(test), next(test), next(test))
'''
# Bob wants to create another function using the built-in iterator functions.
# The manual code above should be turned into a function that can be used against any iterable.
# Help Bob finish his code.
'''
def next_iterator(iterable):
    #...

next_iterator(items)
'''

# Q3
# Bob read about something called a 'generator' in the following article...
# https://www.geeksforgeeks.org/generators-in-python/
# Generators use the 'yield' keyword instead of 'return'.
# He copied the code from the first example in the article.
# He wants his spin-off generator program to yield the first exponents for a number (i.e. a^2, a^3, and a^4).
# Help Bob finish the code.
'''
def simpleGeneratorFun(): 
	yield #...
	yield #...
	yield #...

x = simpleGeneratorFun()

print(next(x))
print(next(x))
print(next(x))
'''

# Q4
# Alice read an article about a Python library with iteration tools, called 'itertools'.
# https://www.geeksforgeeks.org/python-itertools-permutations/
# The itertools library has a 'permutations', which is an example of a type of 'generator'.
# This is because the module generates a variety of output based on a given input.
# Alice wrote a spin-off program, copying the code from the article.
# She noticed something about how the permutations module works.
# Run Alice's code and check the output to see if you figure out what she noticed.
'''
from itertools import permutations 

my_iterable = "dog"
p = permutations(my_iterable) 

for j in list(p): 
    print(j)
'''

# Q5
# Alice used the permutations module to write a simple guessing game.
# Try it out...
'''
from itertools import permutations 

print('--- Letter Combo Guessing Game ---')
print('Choose a five letter combination using a, b, c, d, and e.')
print('You cant use the same letter twice.')
print('Add a comma (,) after each letter, but dont include spaces.')
combo = input("Enter you character combo:\n")
combo_converted = tuple(combo.split(','))

legal_chars = ['a','b','c','d','e']

p = permutations(legal_chars)
iteration_count = 0

for permutation in list(p):
    print(permutation)
    iteration_count += 1
    if permutation == combo_converted:
        print('Match found after', iteration_count, "iterations. The matching combo was:", permutation)
        break
'''
# Alice found some additional code in the following article...
# https://www.geeksforgeeks.org/how-to-check-the-execution-time-of-python-script/
# Alice wants to use the code to update her program and include the total execution time.
# Using the code below as an example, help Alice update her guessing game.
'''
import time

a = 0
start = time.time()     # Start of the calculations.
for i in range(1000):
    a += (i**100)
end = time.time()       # End of the calculations.

print("The time for the test program is :",
      (end-start) * 10**3, "ms") # Multiply the result by 10^3 to give milliseconds (ms).
'''

# Q6
# After learning about permutations, Alice started getting interested in password cracking.
# She learned that the 'crypt' library for Python can be used to hash (or crack hashed) passwords.
# She's used the library to hash a password.
# Run her program and try editing it for different password/salt combinations.
# What's the output for password = dog, salt = WF ?

'''
import crypt
test = crypt.crypt("egg", 'HX') # Password , Salt (2 chars)
print(test)
'''

# Q7
# Alice added her hash to the passwords.txt file.
# She also created a dictionary.txt file with some passwords.
# Read through the code Alice wrote and run the program to see how it works.
# Update the passwords.txt file to include an entry for user 'DOG'.
# ...The password and salt should be the same as from Q6.
# Also, update the dictionary.txt file to include the required password.
# Then change directory to 'wk25_assignment'.
# Run the program and see the result.
'''
import crypt

def testPass(cryptPass):
    salt = cryptPass[0:2]                       # Slice out the first 2 chars (salt value).
    dictFile = open('dictionary.txt', 'r')
    for word in dictFile.readlines():
        word = word.strip('\n')                 # Remove any newline chars.
        cryptWord = crypt.crypt(word,salt)      # Create a hash using the password + salt.
        if cryptWord == cryptPass:
            print("Password found:", word)
            return
    print("Password not found.")
    return

def main():
    passFile = open('passwords.txt')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]                               # Slice out the user (chars before ':').
            cryptPass = line.split(':')[1].strip(' ').strip('\n')   # Set the password after the ':' and remove unwanted chars.
            print("Cracking password for:", user)
            print(cryptPass)
            testPass(cryptPass)

main()
'''

# Q8
# Alice decided to look at the passwords in her local /etc/shadow file.
# She noticed the root password looked different than the default password from the crypt() function.
# Default hash result = HX9LLTdc/jiDE , Local hash = $y$j9T$mRKgw72c.XaWowy1Q1xrC/$nIYDQYi6xfLitgt9vIYSzdgNcK7T6XIsTdZVN8K28PB
# She thinks this is because local Linux password has a different hashing algorithm.
# Alice read the following article and wants to make a function that detects the algorithm used for a given hash...
# https://www.cyberciti.biz/faq/understanding-etcshadow-file/
# Help Alice write a hash_type() function.
'''
hash1 = '$y$j9T$mRKgw72c.XaWowy1Q1xrC/$nIYDQYi6xfLitgt9vIYSzdgNcK7T6XIsTdZVN8K28PB'
hash2 = '$5$j9T$mRKgw72c.XaWowy1Q1xrC/$nIYDQYi6xfLitgt9vIYSzdgNcK7T6XIsTdZVN8K28PB'
hash3 = '$2y$j9T$mRKgw72c.XaWowy1Q1xrC/$nIYDQYi6xfLitgt9vIYSzdgNcK7T6XIsTdZVN8K28PB'
hash4 = 'notahash'

def hash_type(input):
    #...

hash_type(hash1)
hash_type(hash2)
hash_type(hash3)
hash_type(hash4)
'''

# Q9 - BONUS
# Bob saw an article online that had a string permutation algorithm someone made manually.
# https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
# Bob stared at the code for hours and was shocked by how complicated the few lines of code are.
# Read the Python code from the article, then read Bob's version of the code below and test it.
# Next, help Bob add some notes to address the following questions...
# 1) Why is the function 'toString' required?
# 2) Why is an 'if' statement required?
# 3) How is each permutation being printed?
# 4) Why are two lines matching in the function's for loop?
# 5) Do you see why using a permutation library is better than trying to manually code permutation?
'''
def toString(List):
	return ''.join(List)

def permute(input_string, starting_index, ending_index):
	if starting_index == ending_index:
		print(toString(input_string))
	else: 
		for x in range(starting_index, ending_index):
			input_string[starting_index], input_string[x] = input_string[x], input_string[starting_index]
			#print(input_string[starting_index],input_string[x],"test1") # Test print for troubleshooting.
			permute(input_string, starting_index+1, ending_index)
			input_string[starting_index], input_string[x] = input_string[x], input_string[starting_index]
			#print(input_string[starting_index],input_string[x], "test2") # Test print for troubleshooting.

string = "dog"
total_indices = len(string)
string_as_list = list(string)

permute(string_as_list, 0, total_indices)
'''

'''
# More testing...
def toString(List):
	return ''.join(List)

test = 'dog'
i = 0
for char in test:
	toString(test[i])
	print(toString(test[i]))
	i+=1
	
print(toString(test))
'''