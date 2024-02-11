# In this program we took our pseudo-code algorithm for the game of Hide & Seek,
# and turned it into an actual program, which mimics many aspects of the actual game.

import random
hiders = 10
#need to make this a dictionary...
hiders_names = ['Larry', 'Susan', 'Elvis', 'Chad', 'George', 'Albert', 'Sara', 'Todd', 'Sally', 'Tina']
hidden_status = [False, False, False, False, False, False, False, False, False, False]
hider_locations = []
locations = ['tree', 'bench', 'bush', 'trash cans', 'slide', 'sandbox', 'swings', 'cars', 'tables', 'playground']
seekers = 1
seekers_names = ['Julia']
count_down = 20
eyes_covered = False
all_hidden = False

def vision():
    if eyes_covered == True:
        print("My eyes are covered!")
    elif eyes_covered == False:
        print("My eyes aren't covered!")

def hide():
    if all_hidden == False:
        for i in hiders_names:
            hidden_status[i] = True
            #hider location update
        all_hidden = True

def seek():
    print("This is a placeholder.")

vision()

print("Okay, I'm going to count! Start hiding!")

hide()

while count_down > 0:
    if eyes_covered == False:
        eyes_covered = True
        vision()
    print(count_down)
    count_down = count_down - 1

print("Here I come!")
eyes_covered = False

while hiders > 1:
    print("I'm looking for you!")
    #Seek function... seek()
    hiders = hiders - 1
    print("I found somebody!")

print("Alright, last person! Come out!")
#Winner function... winner_check()