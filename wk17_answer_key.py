# Week 17 - Answer Key

# AVOID PEEKING AHEAD OF TIME!










# Scroll down.
# |
# |
# v




























# Q1
# Use: python3 wk17_assignment.py

# Q2
elephant_dict =	{
  "Animal": "Elephant",
  "Personality": "Peaceful",
  "Size": "Very Large"
} 
tiger_dict =	{
  "Animal": "Tiger",
  "Personality": "Stealthy",
  "Size": "Large"
} 
seagull_dict =	{
  "Animal": "Seagull",
  "Personality": "Sky Dog",
  "Size": "Small"
} 
print(seagull_dict)


# Q3
seagull_dict =	{
  "Animal": "Seagull",
  "Personality": ["Sky Dog", "Stealthy", "Scavenger", "Pack Hunter", "Ferocious", "Adaptable"],
  "Size": "Small"
} 
print(seagull_dict)

# Q4
print(seagull_dict["Personality"][2])

# Q5
import requests
import json
response = requests.get("https://zenquotes.io/api/random")
py_obj = json.loads(response.text)
print(py_obj)

# Q6
import requests
import json
response = requests.get("https://zenquotes.io/api/random")
py_obj = json.loads(response.text)
json_parsed = py_obj[0]['q']
print(json_parsed)
#OR...
print(py_obj[0]['q'])

# Q7
import requests
import json
response = requests.get("https://zenquotes.io/api/random")
py_obj = json.loads(response.text)
json_parsed = py_obj[0]['q'] + " -" + py_obj[0]['a']
print(json_parsed)

# Q8
def palindrome_check(mystring):
    if mystring[::-1] == mystring:
        print('This word IS a palindrome.')
    else:
        print('This word is NOT a palindrome.')

palindrome_check('llama')

