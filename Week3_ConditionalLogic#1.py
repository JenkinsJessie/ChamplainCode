# Jessie Jenkins

# CMIT-135

# Week 3 Conditional Logic Problems #1

# Implement a voting test. The user enters their age and then the program prints either, You must be 18 to vote or You are of voting age.

# Ask user for age
age = int(input("Please enter your age for verification: "))

# Compare user age to voting age
if age >= 18:
    print('You are of voting age.')
else:
    print('You must be 18 to vote.')
