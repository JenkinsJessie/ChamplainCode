# Jessie Jenkins

# CMIT-135

# Week 6 Password Saver

import csv
import sys

# The password list - We start with it populated for testing purposes
passwords = [["yahoo","XqffoZeo"],["google","CoIushujSetu"]]


# The password file name to store the passwords to
passwordFileName = "samplePasswordFile"

# The encryption key for the caesar cypher
encryptionKey = 16

# Caesar Cypher Encryption
def passwordEncrypt (unencryptedMessage, key):

    # We will start with an empty string as our encryptedMessage
    encryptedMessage = ''

    # For each symbol in the unencryptedMessage we will add an encrypted symbol into the encryptedMessage
    for symbol in unencryptedMessage:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            encryptedMessage += chr(num)
        else:
            encryptedMessage += symbol

    return encryptedMessage

def loadPasswordFile(fileName):

    with open(fileName, newline='') as csvfile:
        passwordreader = csv.reader(csvfile)
        passwordList = list(passwordreader)

    return passwordList

def savePasswordFile(passwordList, fileName):

    with open(fileName, 'w+', newline='') as csvfile:
        passwordwriter = csv.writer(csvfile)
        passwordwriter.writerows(passwordList)



while True:
    print("What would you like to do:")
    print(" 1. Open password file")
    print(" 2. Lookup a password")
    print(" 3. Add a password")
    print(" 4. Save password file")
    print(" 5. Print the encrypted password list (for testing)")
    print(" 6. Delete password")
    print(" 7. Quit program")
    print("Please enter a number (1-7)")
    choice = input()

    if(choice == '1'): # Load the password list from a file
        passwords = loadPasswordFile(passwordFileName)

    if(choice == '2'): # Lookup at password
        print("Which website do you want to lookup the password for?")
        for keyvalue in passwords:
            print(keyvalue[0])
        passwordToLookup = input()

        for i in range(len(passwords)):   # For loop iterates through passwords list.
          if passwordToLookup in passwords[i][0]:  # Checks for website in passwords list.
               print('The password to ' + passwordToLookup + ' is ', end = '')
               print(passwordEncrypt(passwords[i][1], -encryptionKey))  # Prints unencrypted password.

    if(choice == '3'):
        print("What website is this password for?")
        website = input()
        print("What is the password?")
        unencryptedPassword = input()

        # Uses passwordEncrypt function to encrypt password
        encryptedPassword = passwordEncrypt(unencryptedPassword, encryptionKey)
        # Creates list
        listaddition = [website, encryptedPassword]
        # Adds to passwords list
        passwords.append(listaddition)


    if(choice == '4'): #Save the passwords to a file
            savePasswordFile(passwords,passwordFileName)


    if(choice == '5'): #print out the password list
        for keyvalue in passwords:
            print(', '.join(keyvalue))

    if(choice == '6'):  #deletes entry and password
        print('From what website do you want to delete the password?')
        for keyvalue in passwords:
            print(keyvalue[0])
        website = input()

        for i in range(len(passwords)):  # for loop iterates through password list
            if website in passwords[i]:  # if website found, website and password is deleted
                del passwords[i]
                print(website + '\'s entry and password has been deleted.')
                break   # Essential for not getting list error

    if(choice == '7'):  #quit our program
        sys.exit()

    print()
    print()
