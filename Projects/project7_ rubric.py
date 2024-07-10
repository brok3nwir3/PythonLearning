# Project 7 (100 Points) - Python Host Discovery Scanner

# The goal of this project is to learn more about computer networking and Python libaries with networking capabilities.

# For this project you will create a 'Host Discovery Scanner.'
# The scanner should have a target network range, this can be hard-coded, (but bonus points if the user can set the range).
# The scanner will then scan the network range for available hosts.
# In most cases host discovery is determined by sending pings to the different possible host addresses, followed by a response.
# This means your scanner will need to be able to identify when a response ping is received.
# Additionally, the scanner will need some way to calculate the different host addresses for the given network range.
# Once the program finishes running, the user should see terminal output with the results (bonus points if you can save ouput).
# HINT: Some libraries, such as OS, NMAP, IPADDRESS, SOCKETS, etc. have helpful functions and other features to assist you.

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