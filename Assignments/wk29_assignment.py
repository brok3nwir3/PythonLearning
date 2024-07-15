# Week 29 - Transforming user input, list comprehension refresh, search algorithms, and sorting algorithms.

# Q1
# Alice recently had a coding interview at a tech company.
# She was given a list (below) and asked to write code that would identify the middle number in the list.
# Alice is curious how you'd approach this problem.
# See if you can solve this problem without the use of the Internet.

num_list = [1, 2, 3, 4, 5]


# Q2
# Bob is preparing for an interview and wants to refresh himself on how "list comprehension" works.
# He read the following article to remember the concept: https://www.w3schools.com/python/python_lists_comprehension.asp
# He remembers that list comprehension is simply a way to create a new list based off an existing one.
# Now he wants to practice what he learned by solving the following problem...
# Given a list of numbers, create a new list from the original, but only append numbers that are divisible by 9.

original_list = [10, 90, 9, 17, 23, 81, 27, 55, 46]


# Q3
# Alice is working on some code that she plans to use in a large program.
# The code will be used to take a first name input from a user.
# However, Alice wants the code to capitalize the first letter of given name.
# Additionally, the code should be able to fix any capitalization errors with the name.
# For example, an input of 'joSH' would return 'Josh', or an input of 'keVin' would return 'Kevin'.
# Help Alice write the code.
'''
name = input("Please enter your first name: ")
'''

# Q4
# Bob wants to improve his knowledge of commonly used algorithms.
# He wants to start by learning how to write a 'linear search' algorithm.
# For most 'search' algorithms we're given an array (or list) of numbers, and a target to find within that list.
# With the linear search approach, we simply write a program that searches the list one item at a time.
# This type of search can be effective when the items in the array are unsorted.
# Help Bob write a linear search program, given the below array and target.

my_array = [105, 19, 2000, 777, 89, 17, 504, 32]
target = 17


# Q5
# Now that Bob has solved the linear search problem, he wants to try 'binary search.'
# Binary search is a useful algorithm to use when your array (or list) is sorted.
# The first step is to find the middle number of the array.
# Once the middle number is found, we determine if it is less than or greater than our target number.
# For example, if we have numbers 0-10 our middle number would be 5.
# Then we'd split the array into two halves... 0-5 and 6-10.
# If the target in this example was 7, we could simply ignore the first half of the array because it is less than our target.
# Lastly, we would perform a linear search against the second half of the array.
# Help Bob write a binary search algorithm for the given array and target.

my_array2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target2 = 7


# Q6
# Bob would like to write his own number sorting algorithm.
# Alice told Bob he could use the built in Python .sort() function...
# Here's an example of the .sort() function Alice sent Bob...
'''
test = [5, 3, 1, 4, 2]
test.sort()
print(test)
'''
# However, Bob wants to try to make a sorting algorithm by hand, without use of a built-in sorting function.
# Bob read about 'bubble sort' here: https://en.wikipedia.org/wiki/Bubble_sort
# Bubble sort works by comparing two numbers at a time, left to right.
# When bubble sort sees that a number on the right is smaller than the number of the left, a swap is performed.
# Help Bob write a bubble sort algorithm.

bubble_array = [5, 3, 1, 4, 2]


# Q7 - BONUS
# Bob read about an algorithm called 'insertion sort' on Wikipedia: https://en.wikipedia.org/wiki/Insertion_sort
# Insertion sort is ideal for small data sets, such as the one below.
# Read the 'Algorithm' section of the article and then try to help Bob write an insertion sort program.

unsorted_array = [5, 3, 1, 4, 2]
sorted_array = []
