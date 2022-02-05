# Jessie Jenkins

# CMIT-135

# Week 3 Conditional Logic Problems #2

# Ask the user to enter a grade percentage.  Convert the grade into a letter grade.
# For instance, if the user types 99 then print A+. You can find a sample grading scale here (Links to an external site.).

# Ask for User's name
name = input('Hello, what is your name? ')
# Ask the User if the class is graduate level
level = input(f'Hello {name}, Are you currently in your graduate studies? Please answer yes or no? ')

if level == 'yes':
    level = 'graduate'
elif level == 'no':
    level = 'undergraduate'

# Ask the User for the grade percentage
grade = float(input(f'{name}, Please enter the grade percentage for your {level} class to receive your letter grade: '))

# Calculates grade based on undergraduate scale
if level == 'undergraduate':
    if grade >= 93:
        print('Congratulations, you have an A!')
    elif 93 > grade >= 90:
        print('Good job, you have an A-.')
    elif 90 > grade >= 87:
        print('Good job, you have a B+.')
    elif 87 > grade >= 83:
        print('Good job, you have a B.')
    elif 83 > grade >= 80:
        print('Good job, you have a B-.')
    elif 80 > grade >= 77:
        print('You have a C+.')
    elif 77 > grade >= 73:
        print('You have a C.')
    elif 73 > grade >= 70:
        print('You have a C-.')
    elif 70 > grade >= 67:
        print('You have a D+.')
    elif 67 > grade >= 63:
        print('You have a D.')
    elif 63 > grade >= 60:
        print('You have a D-.')
    elif 60 > grade >= 0:
        print('You have an F.')

# Calculates grade based on graduate scale
if level == 'graduate':
    if grade >= 93:
        print('Congratulations, you have an A+!')
    elif 93 > grade >= 90:
        print('Good job, you have an A.')
    elif 90 > grade >= 87:
        print('Good job, you have a B+.')
    elif 87 > grade >= 83:
        print('Good job, you have a B.')
    elif 83 > grade >= 80:
        print('Good job, you have a B-.')
    elif 80 > grade >= 77:
        print('You have a C+.')
    elif 77 > grade >= 73:
        print('You have a C-.')
    elif 73 > grade >= 0:
        print('You have an F.')
