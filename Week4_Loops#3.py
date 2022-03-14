from random import randint

# Jessie Jenkins

# CMIT-135

# Week 4 Loops #3

# Write a program that picks a random number from 1-100.  Then ask the user to guess a number.
# Tell the user if the answer is higher or lower than the number they guessed, or if they got the correct answer.
# Allow them to guess again if they got the guess incorrect.

# Welcome user and generate value for random number.
print('Hello! Welcome to the Random Number Guessing Game!!')
randomNum = randint(1, 101)

# Ask user for number.
guess = int(input('Please input a number 1 - 100: '))

# While statements gives user hint if they are higher or lower than random number.
while guess > randomNum:
    guess = int(input('Your guess is too high! try again: '))

while guess < randomNum:
    guess = int(input('Your guess is too low! Try again: '))

# Congratulates user for correct answer.
print('Congratulations, you are correct!')
