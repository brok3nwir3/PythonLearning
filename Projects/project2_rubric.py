# Project 2 (100 Points)

# For this project you'll be making a Hide and Seek game.
# This project will utilize many of the things we learned during the first several assignments, including:
# dictionaries, lists, type casting, functions, if statements, indices, importing libraries, and more.
# The entire program should be around 110 lines, including comments.

# You will demonstrate your finished project, once it's completed.
# You should be able to show a working game, and explain how the code works.

# Because this is your first large project, you will have very detailed instructions to assist you.

# Use the following steps for your project...
# 1. Create a list of 5-10 locations (strings) for players to hide at.
# 2. Create 3-4 dictionaries called "player1", "player2", etc.
# 3. Give each dictionary the following properties: name, location, hidden.
#   a. For each of the dictionaries, set player name strings, set location to "Placeholder", and hidden to boolean True.
# 4. Import the random library and set a random location for each player.
#   a. You'll need to determine how many indices there are for your locations list.
#   b. If you created 6 locations, then your indices would be 0-5.
#   c. You can use the randrange() function to roll random indices.
# 5. Test 1: At this point you should print each player dictionary to test that you are correctly assigning locations.
#   a. Remove the test line/s once you've confirmed the current code is working.
# 6. Create a print statement to display a welcome message, and to list all of your location options to choose from.
# 7. Create a user input variable called "guess", for users to submit a single number guess.
#   a. Remember, input is saved to a variable as a string, so you'll need to cast the input as an integer.
#   b. You'll need to prompt the user to submit a value 0-X, where X is the last index they can choose from.
# 8. Create a new function for each player, called player1_check, player2_check, etc. 
#   a. The function should take one parameter called "num".
#   b. The function should have an if statement that checks if the player location is equal to the guess location index number.
#   c. The if statement should also check whether the player is still hidden.
#   d. If both requirements are true, a player located message should be printed, and the player should be set to hidden False.
#   e. Otherwise, if the location was wrong and the player is still hidden, a player still hidden message should be printed.
# 9.Call all of the player check functions.
#   a. Bonus: Clear the screen before calling all the player check functions.
# 10. Test 2: Run our program and see if your functions work as expected.
# 11. Put all your print statements, player input, and player check functions, inside a while loop.
#   a. The while loop should run as long as a variable called game_finished is False.
#   b. Create the game_finished variable above the while loop and set it to False.
#   c. Add an if statement to the bottom of the while loop, to check whether there are any players still hidden.
#   d. If there are no players hidden, then the if statement should get game_finished to True, and print a victory message.

# Bonus: Earn kudos by adding some flavor to the program.
# Things like ASCII art, style elements, etc. will make your game unique.

# Grading Rubric...
# 1) Does the game work? (60 Points)
#   a) Demo walk-through.
#   b) Does the game crash, or print unintended output?
# 2) Can you explain the code, and answer questions about the code? (40 Points)
#   a) How did you randomly assign locations to players?
#   b) How many locations did you create? How many players did you create?
#   c) Which parts of the program were the toughest to code?
#   d) How would you improve the game in a future version?
# 3) Does your game have any bonus flavor? (10 Points)
#   a) ASCII Art?
#   b) Text Coloring?
#   c) Screen clearing?