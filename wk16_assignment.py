# Week 16 - An interview question, some 2D array review, and then an intro to JSON and APIs.

# Q1
# *** Time yourself for this question! ***
# Alice is interviewing for a job at Goople.
# They've asked her to write a "FizzBuzz" program.
# The program should print the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”.
# Expected Output...
# 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz...



# Q2
# Bob was hired at the local weather station.
# His first task is to create a 2D array for some recent weather data.
# The company has provided him with the data from last week.
# Help bob create a 2D array for the data.
# Hint: Don't forget about the .append() function for arrays.

# Daily data from 1PM, during the past week.
monday = 86.4
tuesday = 92.1
wednesday = 85.4
thursday = 80.3
friday = 91.9
saturday = 78.8
sunday = 82.7

# Daily data from 2PM, during the past week.
monday = 83.8
tuesday = 91.5
wednesday = 86.6
thursday = 90.2
friday = 93.4
saturday = 79.1
sunday = 86.7



# Q3
# Bob is happy with the output of the 2D array.
# However, he would like the data to be presented as stacked rows.
# Help Bob reformat the output.



# Q4
# Alice is learning about JSON and APIs.
# She found a free API that returns a random quote.
# She also discovered that she can view the output of the API call by simply visiting the URL.
# Navigate to the following URL and see what shows up.
# https://zenquotes.io/api/random
# Congrats! You've manually made your first API call. Try refreshing the page to make another call.


# Q5
# Alice wants to check whether the page is up or not.
# She started by importing a necessary module.
# Help Alice write some code to get the status code of the API URL.
# She thinks this article will be helpful...
# https://www.dataquest.io/blog/python-api-tutorial/

import requests


# Q6
# Alice is satisfied that the server handling the API requests is operational and returning data she likes.
# She started by importing the necessary modules.
# Now she'd like to write some code to make an API call and then print the output.
# Use the above article and help Alice write the code.

import requests
import json
response = requests.get("https://zenquotes.io/api/random")
print(response.json())

# Q7
# Compare the printed output from Q6 to what you see when you make a manual API call to the URL via browser.
# What do you notice?
# Do some googling for the zenquotes API documentation. It may help explain the output.

