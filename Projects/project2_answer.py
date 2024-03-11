# Tic-tac-toe Game
# (One Human Player vs One AI Player)
# Author: Phil van der Linden
# Date: 01/30/2024

import os
import random
import time

print("\nThe Tic-tac-toe Game!\n")

legal_selection = False
while legal_selection == False:
    human_play_as = input("Would you like to play as 'x' or 'o'?: ")
    if human_play_as not in ('x', 'o'):
        print("Only 'x' or 'o' can be chosen.")
    else:
        legal_selection = True

os.system('clear')
print("\nYou've selected to play as "+human_play_as+".")

ai_play_as = 'x'
if human_play_as == 'x':
    ai_play_as = 'o'

print("The AI player will play as "+ai_play_as+".")

row1 = ["_______________________________"]
row2 = ["|","1","|","2","|","3","|"]
row3 = ["_______________________________"]
row4 = ["|","4","|","5","|","6","|"]
row5 = ["_______________________________"]
row6 = ["|","7","|","8","|","9","|"]
row7 = ["_______________________________"]

def board_state():
    print(row1)
    print(row2)
    print(row3)
    print(row4)
    print(row5)
    print(row6)
    print(row7)
board_state()

human_turn = True
game_won = False
human_won = False
ai_won = False
marked_1 = False
marked_2 = False
marked_3 = False
marked_4 = False
marked_5 = False
marked_6 = False
marked_7 = False
marked_8 = False
marked_9 = False

def win_check():
    # Check if the human player won.
    global game_won
    # Horizontal win check...
    if row2[1] == human_play_as and row2[3] == human_play_as and row2[5] == human_play_as:
        game_won = True
        print("Congratulations! You've defeated the AI! \o/ ")
    if row4[1] == human_play_as and row4[3] == human_play_as and row4[5] == human_play_as:
        game_won = True
        print("Congratulations! You've defeated the AI! \o/ ")
    if row6[1] == human_play_as and row6[3] == human_play_as and row6[5] == human_play_as:
        game_won = True
        print("Congratulations! You've defeated the AI! \o/ ")
    # Veritical win check...
    if row2[1] == human_play_as and row4[1] == human_play_as and row6[1] == human_play_as:
        game_won = True
        print("Congratulations! You've defeated the AI! \o/ ")
    if row2[3] == human_play_as and row4[3] == human_play_as and row6[3] == human_play_as:
        game_won = True
        print("Congratulations! You've defeated the AI! \o/ ")
    if row2[5] == human_play_as and row4[5] == human_play_as and row6[5] == human_play_as:
        game_won = True
        print("Congratulations! You've defeated the AI! \o/ ")
    # Diagonal win check...
    if row2[1] == human_play_as and row4[3] == human_play_as and row6[5] == human_play_as:
        game_won = True
        print("Congratulations! You've defeated the AI! \o/ ")
    if row2[5] == human_play_as and row4[3] == human_play_as and row6[1] == human_play_as:
        game_won = True
        print("Congratulations! You've defeated the AI! \o/ ")

    # Check if the AI player won.
    # Horizontal win check...
    if row2[1] == ai_play_as and row2[3] == ai_play_as and row2[5] == ai_play_as:
        game_won = True
        print("You've been defeated by the AI! :( ")
    if row4[1] == ai_play_as and row4[3] == ai_play_as and row4[5] == ai_play_as:
        game_won = True
        print("You've been defeated by the AI! :( ")
    if row6[1] == ai_play_as and row6[3] == ai_play_as and row6[5] == ai_play_as:
        game_won = True
        print("You've been defeated by the AI! :( ")
    # Veritical win check...
    if row2[1] == ai_play_as and row4[1] == ai_play_as and row6[1] == ai_play_as:
        game_won = True
        print("You've been defeated by the AI! :( ")
    if row2[3] == ai_play_as and row4[3] == ai_play_as and row6[3] == ai_play_as:
        game_won = True
        print("You've been defeated by the AI! :( ")
    if row2[5] == ai_play_as and row4[5] == ai_play_as and row6[5] == ai_play_as:
        game_won = True
        print("You've been defeated by the AI! :( ")
    # Diagonal win check...
    if row2[1] == ai_play_as and row4[3] == ai_play_as and row6[5] == ai_play_as:
        game_won = True
        print("You've been defeated by the AI! :( ")
    if row2[5] == ai_play_as and row4[3] == ai_play_as and row6[1] == ai_play_as:
        game_won = True
        print("You've been defeated by the AI! :( ")

def tie_check():
    global game_won
    if game_won == False:
        # Check if all spaces have been filled.
        if row2[1] != '1' and row2[3] != '2' and row2[5] != '3':
            if row4[1] != '4' and row4[3] != '5' and row4[5] != '6':
                if row6[1] != '7' and row6[3] != '8' and row6[5] != '9':
                    game_won = True
                    print("The game was a tie! No Winners!")

while game_won == False:

    # --- HUMAN TURN ---
    legal_selection = False
    while legal_selection == False and human_turn == True:
        human_move = input("\nWhich position would you like to mark?: ")
        if human_move in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            if human_move == '1' and marked_1 == False:
                row2[1] = human_play_as
                marked_1 = True
                legal_selection = True
                os.system('clear')
                print("\n\n")
                board_state()
                print("You've marked position "+human_move+".")
                human_turn = False
            if human_move == '2' and marked_2 == False:
                row2[3] = human_play_as
                marked_2 = True
                legal_selection = True
                os.system('clear')
                print("\n\n")
                board_state()
                print("You've marked position "+human_move+".")
                human_turn = False
            if human_move == '3' and marked_3 == False:
                row2[5] = human_play_as
                marked_3 = True
                legal_selection = True
                os.system('clear')
                print("\n\n")
                board_state()
                print("You've marked position "+human_move+".")
                human_turn = False
            if human_move == '4' and marked_4 == False:
                row4[1] = human_play_as
                marked_4 = True
                legal_selection = True
                os.system('clear')
                print("\n\n")
                board_state()
                print("You've marked position "+human_move+".")
                human_turn = False
            if human_move == '5' and marked_5 == False:
                row4[3] = human_play_as
                marked_5 = True
                legal_selection = True
                os.system('clear')
                print("\n\n")
                board_state()
                print("You've marked position "+human_move+".")
                human_turn = False
            if human_move == '6' and marked_6 == False:
                row4[5] = human_play_as
                marked_6 = True
                legal_selection = True
                os.system('clear')
                print("\n\n")
                board_state()
                print("You've marked position "+human_move+".")
                human_turn = False
            if human_move == '7' and marked_7 == False:
                row6[1] = human_play_as
                marked_7 = True
                legal_selection = True
                os.system('clear')
                print("\n\n")
                board_state()
                print("You've marked position "+human_move+".")
                human_turn = False
            if human_move == '8' and marked_8 == False:
                row6[3] = human_play_as
                marked_8 = True
                legal_selection = True
                os.system('clear')
                print("\n\n")
                board_state()
                print("You've marked position "+human_move+".")
                human_turn = False
            if human_move == '9' and marked_9 == False:
                row6[5] = human_play_as
                marked_9 = True
                legal_selection = True
                os.system('clear')
                print("\n\n")
                board_state()
                print("You've marked position "+human_move+".")
                human_turn = False
        else:
            print("You must select an available number.")

    time.sleep(1) # Two second screen delay.
    win_check()
    tie_check()

    # --- AI TURN ---
    legal_selection = False
    while legal_selection == False and human_turn == False and game_won == False:
        ai_move = str(random.randint(1,9))
        if ai_move == '1' and marked_1 == False:
            row2[1] = ai_play_as
            marked_1 = True
            legal_selection = True
            os.system('clear')
            print("\n\n")
            board_state()
            print("The AI player has marked position "+ai_move+".")
            human_turn = True
        if ai_move == '2' and marked_2 == False:
            row2[3] = ai_play_as
            marked_2 = True
            legal_selection = True
            os.system('clear')
            print("\n\n")
            board_state()
            print("The AI player has marked position "+ai_move+".")
            human_turn = True
        if ai_move == '3' and marked_3 == False:
            row2[5] = ai_play_as
            marked_3 = True
            legal_selection = True
            os.system('clear')
            print("\n\n")
            board_state()
            print("The AI player has marked position "+ai_move+".")
            human_turn = True
        if ai_move == '4' and marked_4 == False:
            row4[1] = ai_play_as
            marked_4 = True
            legal_selection = True
            os.system('clear')
            print("\n\n")
            board_state()
            print("The AI player has marked position "+ai_move+".")
            human_turn = True
        if ai_move == '5' and marked_5 == False:
            row4[3] = ai_play_as
            marked_5 = True
            legal_selection = True
            os.system('clear')
            print("\n\n")
            board_state()
            print("The AI player has marked position "+ai_move+".")
            human_turn = True
        if ai_move == '6' and marked_6 == False:
            row4[5] = ai_play_as
            marked_6 = True
            legal_selection = True
            os.system('clear')
            print("\n\n")
            board_state()
            print("The AI player has marked position "+ai_move+".")
            human_turn = True
        if ai_move == '7' and marked_7 == False:
            row6[1] = ai_play_as
            marked_7 = True
            legal_selection = True
            os.system('clear')
            print("\n\n")
            board_state()
            print("The AI player has marked position "+ai_move+".")
            human_turn = True
        if ai_move == '8' and marked_8 == False:
            row6[3] = ai_play_as
            marked_8 = True
            legal_selection = True
            os.system('clear')
            print("\n\n")
            board_state()
            print("The AI player has marked position "+ai_move+".")
            human_turn = True
        if ai_move == '9' and marked_9 == False:
            row6[5] = ai_play_as
            marked_9 = True
            legal_selection = True
            os.system('clear')
            print("\n\n")
            board_state()
            print("The AI player has marked position "+ai_move+".")
            human_turn = True

        time.sleep(1) # Two second screen delay.
        if game_won == False:
            win_check()
            tie_check()