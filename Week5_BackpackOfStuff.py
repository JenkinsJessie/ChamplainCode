# Jessie Jenkins

# CMIT-135

# Week 5 - Backpack of Stuff

import sys

itemsInBackpack = ["book", "computer", "keys", "travel mug"]

while True:
    print("Would you like to:")
    print("1. Add an item to the backpack?")
    print("2. Check if an item is in the backpack?")
    print("3. Quit")
    userChoice = input()

    if(userChoice == "1"):
        print("What item do you want to add to the backpack?")
        itemToAdd = input()

        ####### YOUR CODE HERE ######
        # Adds items to backpack.
        itemsInBackpack.append(itemToAdd)
        ####### YOUR CODE HERE ######


    if(userChoice == "2"):
        print("What item do you want to check to see if it is in the backpack?")
        itemToCheck = input()

        ####### YOUR CODE HERE ######
        # Checks for item in backpack and informs user.
        if (itemToCheck in itemsInBackpack):
            print('Yes, that item is currently in your backpack. ')
        else:
            print('No, that item is not currently in your backpack.')
        ####### YOUR CODE HERE ######

    if(userChoice == "3"):
        sys.exit()
