# Week 17 - Dictionary review, APIs/JSON continued, and an interview question.

# Q1
# Alice has been working in VScode so much, she's forgotten how to execute a Python file from CLI.
# Help Alice run the following code from CLI.

print("Hello CLI!")

# Q2
# Bob needs help turning the following data into three dictionaries.
# The dictionaries should contain all three attributes.
# Data...
# Animal - Elephant / Personality - Peaceful / Size - Very Large
# Animal - Tiger / Personality - Stealthy / Size - Large
# Animal - Seagull / Personality - Sky Dog / Size - Small
# Once you've created the dictionaries, print the seagull dictionary.
 


# Q3
# Alice found Bobs new dictionaries on GitHub and forked the file.
# However, she noticed the Seagull dictionary is incomplete.
# Alice wants to update the dictionary to include the additional Personality items for Seagulls...
# Personality - Sky Dog, Stealthy, Scavenger, Pack Hunter, Ferocious, Adaptable
# Help Alice update the original dictionary to include the new Personality attributes.
# Print the updated dictionary once you're done.



# Q4
# Bob read Alice's updated code and noticed that dictionaries are similar to a matrices.
# For example, a dictionary resembles...
# [[1,2,3]
# [3,4,5]
# [6,7,8]]
# Bob wants to access specific Seagull personality attributes from Alice's Seagull dictionary.
# Help Bob write some code to access the third personality attribute and print it.



# Q5
# Alice wrote some code to make an API call.
# She would like to convert the response to a Python object.
# Alice thinks json.loads() function will work for this.
# Help Alice add a line before her print statement, to convert the response.
# Lastly, update the print statement to print the Python object.

'''
import requests
import json
response = requests.get("https://zenquotes.io/api/random")
print(py_obj)
'''

# Q6
# Now that you've helped Alice convert the response to a Python object, she noticed something about the response.
# It's currently sending the entire response, and the JSON data appears to be formatted like a dictionary...
# Alice thinks she can write a request that only retrives the 'q' item from the JSON data.
# Help Alice add update her code to explicitly retrieve 'q'.



# Q7
# Bob saw Alice's code from Q6 and thinks it can be improved.
# Alice's code returns 'q' but should also include 'a' on the same line.
# Bob wants to also add a hyphen '-' character to made the line look perfect.
# Expected output: "Some Quote." -John Smith
# Help Bob update the code.



# Q8
# Bob is preparing for an interview at Microhard.
# Alice told him that she recently had an interview question which asked her to write a palindrome function.
# Bob wants to tackle this problem for practice.
# Help Bob write a function that takes a single string input.
# The function should determine if the given word is a palindrome or not.
# Test output 1, 'llama': "This word is NOT a palindrome."
# Test output 2, ''lionoil': "This word IS a palindrom."
# Note: If you get stuck, read this page (half credit): https://www.w3schools.com/python/python_howto_reverse_string.asp

