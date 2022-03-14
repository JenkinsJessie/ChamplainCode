# Jessie Jenkins

# CMIT-135

# Week 5 - Comma Code

# Code for adding new items to list and breaking looping after list finished.
listToPrint = []
while True:
    newWord = input("Enter a word to add to the list (press return to stop adding words) > ")
    if newWord == "":
        break
    else:
        listToPrint.append(newWord)

# Check for length of code
list_number = len(listToPrint)

# Adds and to the end of code if it is larger than 1 item.
if list_number >= 2:
    listToPrint.insert(-1, 'and')

# Prints List
print(listToPrint)
