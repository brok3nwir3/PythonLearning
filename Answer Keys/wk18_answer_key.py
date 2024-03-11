# Week 18 - Answer Key

# AVOID PEEKING AHEAD OF TIME!










# Scroll down.
# |
# |
# v




























# Q1
# The module function...
def test1():
    print("Hello World")

# The import + function call...
import hello_world
hello_world.test1()

# Q2
# The module function...
def test2():
    print("Hello Universe")

# The import + function call...
import hello_world
hello_world.test2()

# Q3
from hello_world import *
test1()

# Q4
# The environment module...
# SECRET_1=ABCD1234

# Modules imported + function call...
import os
from dotenv import load_dotenv
load_dotenv()
MY_TOKEN = os.getenv("SECRET_1")
print(MY_TOKEN)

# Q5
URL = "https://malshare.com/api.php?api_key=" + MY_TOKEN + "&action=getlist"
print(URL)

# Q6
# Some free APIs require a key.
# Some APIs are limited to a certain number of requests for a given time interval.
# Some APIs are restricted by day of the week.
# Some APIs may use system time to determine the date to use.

# Q7
# a) What handles memory sharing, caching, segmentation, and allocation?
# answer: The Python memory manager.
# b) Where are Python objects stored?
# answer: Python has a private heap space that stores all the objects.
# c) Can the user control the heap?
# answer: No. The user has no control over the heap; only the Python interpreter has access.