# Project 7 (100 Points) - Python Host Discovery Scanner

# The goal of this project is to learn more about computer networking and Python libaries with networking capabilities.

# For this project you will create a 'Host Discovery Scanner.'
# The scanner should scan a particular network range. Bonus points if the user can set the range.
# The scanner will then scan the given network range for available hosts.
# In most cases host discovery is determined by sending pings to the different possible host addresses, followed by a response.
# This means your scanner will need to be able to identify when a response ping is received.
# Additionally, the scanner will need some way to calculate the different host addresses for the given network range.
# Some libaraies, such as OS, NMAP, SOCKETS, etc. will have helpful functions or other features to assist you.

# Grading Rubric...
# 1) Does the program work? (60 Points)
#   a) The program scans a network range.
#   b) The program successfully registers responses.
#   c) the program prints the scan output.
# 2) Can you explain the code, and answer questions about the code? (40 Points)
#   a) Which libaries did you use? Why?
#   b) How does the scanner identify the possible hosts for the given range?
#   c) How does the scanner identify a response?
# 3) Does your program have any bonus flavor? (10 Points)
#   a) The user can specify a network range to scan.
#   b) The scanner can save the scan output to a text file.