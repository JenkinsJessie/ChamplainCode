# Jessie Jenkins

# CMIT-135

# Week 3 Conditional Logic Problems #3

# Write a program that asks for two numbers.
# If the sum of the numbers is greater than 100, print "They add up to a big number" if it is less than/equal to 100 than print "They add up to ____".

# Prompts user for 2 numbers
number_1 = float(input('Please input number #1: '))
number_2 = float(input('Please input number #2: '))

# Program adds numbers for total
total = number_1 + number_2

if total > 100:
    print('They add up to a big number')
elif total < 100:
    print(f'They add up to {total}')
