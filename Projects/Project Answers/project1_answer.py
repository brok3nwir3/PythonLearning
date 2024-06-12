### Hide & Seek Game ###
# Project 1
# Author: Phil van der Linden
# Date: 09/01/2023


import random
import os

# Create a list of several locations.
locations = ["Tree House", "Bushes", "Creek", "Garden", "Garage", "Sandbox", "Flowerbed", "Monkey Bars"]

# Create a few players as dictionaries.
player1 = {
  "name": "John",
  "hidden": True,
  "location": "Placeholder"
}
player2 = {
  "name": "Alex",
  "hidden": True,
  "location": "Placeholder"
}
player3 = {
  "name": "Greg",
  "hidden": True,
  "location": "Placeholder"
}
player4 = {
  "name": "Tina",
  "hidden": True,
  "location": "Placeholder"
}

# Hide each player in a random location, using a random index.
# The index range (0,8) translates to 0-7.
# Note: It's possible for more than one player to be in the same location.

player1["location"] = locations[random.randrange(0,8)]
player2["location"] = locations[random.randrange(0,8)]
player3["location"] = locations[random.randrange(0,8)]
player4["location"] = locations[random.randrange(0,8)]

game_finished = False

print("\n ~~~~~~ The Hide & Seek Game! ~~~~~~\nCan you find all four of the hidden players?")

while game_finished == False:
    print("\nPlayers might be hidden in one of the following locations...\n\
        1. Tree House\n\
        2. Bushes\n\
        3. Creek\n\
        4. Garden\n\
        5. Garage\n\
        6. Sandbox\n\
        7. Flowerbed\n\
        8. Monkey Bars\n")
    
    # Take the user input and cast it from a string to an actual integer.
    # We then subtract the user input by 1 to account for indices starting at 0.
    guess = int(input("Where would you like to look? Choose a number 1-8: ")) - 1

    def player1_check(num):
        if player1["location"] == locations[num] and player1["hidden"] == True:
            print("\n* You found " + player1["name"] + "! *")
            player1["hidden"] = False
        elif player1["location"] != locations[num] and player1["hidden"] == True:
            print("\n" + player1["name"] + " is still hidden...")

    def player2_check(num):
        if player2["location"] == locations[num] and player2["hidden"] == True:
            print("\n* You found " + player2["name"] + "! *")
            player2["hidden"] = False
        elif player2["location"] != locations[num] and player2["hidden"] == True:
            print("\n" + player2["name"] + " is still hidden...")

    def player3_check(num):
        if player3["location"] == locations[num] and player3["hidden"] == True:
            print("\n* You found " + player3["name"] + "! *")
            player3["hidden"] = False
        elif player3["location"] != locations[num] and player3["hidden"] == True:
            print("\n" + player3["name"] + " is still hidden...")

    def player4_check(num):
        if player4["location"] == locations[num] and player4["hidden"] == True:
            print("\n* You found " + player4["name"] + "! *")
            player4["hidden"] = False
        elif player4["location"] != locations[num] and player4["hidden"] == True:
            print("\n" + player4["name"] + " is still hidden...")

    os.system('clear')
    player1_check(guess)
    player2_check(guess)
    player3_check(guess)
    player4_check(guess)

    # If there are no more hidden players, end the game.
    if player1["hidden"] == False and \
    player2["hidden"] == False and \
    player3["hidden"] == False and \
    player4["hidden"] == False:
        game_finished = True
        print("\n*** Great work! You found everyone! \o/ ***")
