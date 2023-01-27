# Random Signals
# Project 1 - Question 2
# Patrick Laverty in collaboration with Jose Perez.

import random
correct = 0
timesran = 0
def MontyHall():
    global correct, timesran
    Doors = [0,0,0] # Define workspace: 1 for car 0 for goat.
    print("\n\nCurrent Cycle: " + str(timesran + 1) + "")
    CorrectDoor = random.randint(0,2) # We will choose which door has the car
    Doors[CorrectDoor] = 1 # Set that to a 1
    print("The correct door: " + str(CorrectDoor + 1))

    # Now we have our setup, lets choose a random door
    choice = random.randint(0,2)
    print("We will choose: " + str(choice + 1))

    TheDoorItIsnt = 0
    # Now we display a door that it isn't
    for i in range(0,3):
        if ((Doors[i] == 0) and (i != choice)):
            print("It isn't " + str(i + 1))
            TheDoorItIsnt = i
            break

    print("Now we switch:")
    if (choice == 0 and TheDoorItIsnt == 1): 
        choice = 2
    elif (choice == 0 and TheDoorItIsnt == 2): 
        choice = 1
    elif (choice == 1 and TheDoorItIsnt == 2):
        choice = 0
    elif (choice == 1 and TheDoorItIsnt == 0):
        choice = 2
    elif (choice == 2 and TheDoorItIsnt == 0): 
        choice = 1
    elif (choice == 2 and TheDoorItIsnt == 1): 
        choice = 0

    correct += (1 if (choice == CorrectDoor) else 0)
    timesran += 1
    print("We chose door " + str(choice + 1) + " and it was " + ("correct." if (choice == CorrectDoor) else "incorrect."))

for i in range(0,100):
    MontyHall()

print("\n\nThe frequency correct is " + str((correct/timesran) * 100) + "%")