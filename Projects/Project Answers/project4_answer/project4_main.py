# Python API Program - Project 4
# Author: Phil van der Linden
# From this (main) file we run our three APIs for demonstration.

from api1 import *
from api2 import *
from api3 import *
import os

cat1 = " _._     _,-'""`-._"
cat2 = "(,-.`._,'(       |\`-/|"
cat3 = "    `-.-' \ )-`( , o o)"
cat4 = "          `-    \`_`\"'-"

def cat_ascii():
    print("\n" + cat1 + "\n" + cat2 + "\n" + cat3 + "\n" + cat4 + "\n")

cat_ascii()

print("You've launched the Project 3 API program.\n")

legal_selection = False
while legal_selection == False:
    selection = input("Which API would you like to run?\n1: Random Cat Fact\n2: Cat Breed Info\n3: Get a Cat Image\n")
    os.system('clear')

    if selection == '1':
        print("\nRuning API " + selection + " Random Cat Fact...")
        legal_selection = True
        cat_ascii()
        catfacts()
    if selection == '2':
        print("\nRuning API " + selection + " Cat Breed Info...")
        choice = input("Enter a cat breed. For example, 'persian'...\n")
        legal_selection = True
        cat_ascii()
        catbreed(choice)
    if selection == '3':
        print("\nRuning API " + selection + " Opening a random cat pic...")
        legal_selection = True
        cat_ascii()
        catimage()
    elif selection not in ('1','2','3'):
        print("You must select a number 1-3.")