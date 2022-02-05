from random import randint

# Jessie Jenkins

# CMIT-135

# Week 3 Conditional Logic Problems #4

# Implement a random number guessing game. The computer will pick a number at random from 0-9, the user will be asked to guess the number.
# Inform the user if they get the answer correct.

# Welcome user and generate value for random number
print('Hello! Welcome to the Random Number Guessing Game!!')
randomNum = randint(0, 9)

# Ask user for number
guess = int(input('Please input a number 0 - 9: '))

# Continues asking user for number while number is incorrect
while guess != randomNum:
    guess = int(input('That is not the correct number, try again: '))

# Congratulates user for correct answer
print('Congratulations, you are correct!')






