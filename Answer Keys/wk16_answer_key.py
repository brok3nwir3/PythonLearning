# Week 16 - Answer Key

# AVOID PEEKING AHEAD OF TIME!










# Scroll down.
# |
# |
# v




























# Q1
x = 1
while x < 101:
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0 and x % 5 != 0:
        print("Fizz")
    elif x % 3 != 0 and x % 5 == 0:
        print("Buzz")
    else:
        print(x)
    x += 1

# Q2
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
temps_1pm = [86.4, 92.1, 85.4, 80.3, 91.9, 78.8, 82.7]
temps_2pm = [83.8, 91.5, 86.6, 90.2, 93.4, 79.1, 86.7]
days_temps = []
days_temps = [days]
days_temps.append(temps_1pm)
days_temps.append(temps_2pm)
print(days_temps)

# Q3
for row in days_temps:
        print(row)

# Q4
# Simply visit: https://zenquotes.io/api/random
# View the results, then refresh the page.

# Q5
print(response.json())
print(response)

# Q6
response = requests.get("https://zenquotes.io/api/random")
print(response.json())

# Q7
# Both the manual request and programmatic request return specific fields.
# The Zenquote API documentation can be found here:
# https://docs.zenquotes.io/zenquotes-documentation/
# According to the documentation...
# q = quote text
# a = author name
# i = author image (key required)
# c = character count
# h = pre-formatted HTML quote