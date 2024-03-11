# Week 18 - Modules, Environment Files, and Handling API Keys

# Q1
# Bob is learning about modules and would like to create a simple "Hello World" module.
# Help Bob by creating a file called hello_world.py .
# The file should include a function called "test1", which prints a "Hello World" statement.
# Lastly, import the module and call it in this file.
# Bob thinks this document will help: https://docs.python.org/3/tutorial/modules.html



# Q2
# Bob wants to create a second function in the same module.
# The function shoul be named "test2", which prints "Hello Universe".
# After you add the function, call it here (in the main file).



# Q3
# Alice saw Bobs code, but wants to rewrite the code to simplify the module calls.
# Alice would prefer to write "test1()" rather than "hello_world.test1()".
# Help Alice update the main file (here), to make the module call in the specified way.
# Hint: This other method depends on how the "import" line if structured.



# Q4
# Bob found a cool new API to use in his programs.
# However, the new API requires an API key to be used in the requests.
# Bob read that API keys can be securely stored in environment files.
# Help Bob create an environment file called ".env".
# Create a variable within the environment file, called "SECRET_1".
# Set the variable equal to his API key: ABCD1234
# According to an article Bob found (https://pypi.org/project/python-dotenv/), ...
# he thinks he can pull the secret data into the main file.
# Read the article, then import the environment file, and print SECRET_1 from the main file.
# Hint: You may need to import a 2nd module, and write a variable in main for the secret...
# Check online for examples.



# Q5
# Now that the .env file has been successfully created, Bob needs to add the secret to his API request string.
# Read the documentation for the free API, here: https://malshare.com/doc.php
# Help Bob write the URL string using the API key from the environment file.

# URL = "you-url-string-here"
# print(URL)

# Q6
# Read the comments for this Discord bot code on GitHub.
# What are some considerations mentioned for the APIs used?
# https://github.com/brok3nwir3/Python/blob/main/Discord%20News%20Bot.py



# Q7
# Alice is interviewing at VM Care.
# She was asked the following nterview question: "How is Memory managed in Python?"
# Use Google to answer this question.
# Your answer should address the following...
# a) What handles memory sharing, caching, segmentation, and allocation?
# b) Where are Python objects stored?
# c) Can the user control the heap?
