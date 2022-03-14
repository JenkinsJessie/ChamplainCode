# Jessie Jenkins
# CMIT-135
# Conversation with a computer

# User inputs name
name = input("Please enter your name: ")
print('Good Morning ' + name)
# Computer asks user for time they went to bed.
mid = int(input('What time did you go to bed?  Please input your answer in 24 hour format: '))
# while loop checks for correct input
while mid > 2400:
    mid = int(input('Please enter a correct time using the 24 hour format: '))
if 2401 > mid >= 2200:
    print('Oh my! You didn\'t go to bed until ' + str(mid) + '!  That is late!')
elif 0 < mid < 2200:
    print('That is good that you went to bed at ' + str(mid) + '.')
# Computer asks user for time they woke up.
after_mid = int(input('What time did you wake up?  Please input your answer in 24 hour format: '))
# while loop checks for correct input
while after_mid > 2400:
    after_mid = int(input('Please enter a correct time using the 24 hour format: '))
if int(after_mid) <= 600:
    print('Wow, you woke up at ' + str(after_mid) + '! You must be an early riser.')
else:
    print('You must have enjoyed sleeping in until ' + str(after_mid) + '!')
# Computer computes hours that user slept.
mid_hour = 2400 - int(mid)
sleep = int(mid_hour) + int(after_mid)
(hours) = sleep / 100
if hours < 8:
    print('By my calculations you received under 8 hours of sleep.  You should try to get 8 hours of sleep a night to wake restful.')
else:
    print('By my calculations you received over 8 hours of sleep.  That is great! Doctors recommend 8 hours of sleep for the body to be restful.')
# Computer asks user about homework or other activity performed last night.
homework = input('Did you work on homework last night? (y or n) ')
if homework == 'y':
    subject = input('What type of homework did you work on? ')
    print('When you work on your ' + subject + ',  Be sure to work on it early, so that you may get to bed at a decent time.')
else:
    no_homework = input('What did you do last night? ')
    print('Make sure that when you "' + no_homework + '", that you finish early so you may get plenty of rest for the next day!')
# Computer wishes user a great day.
print('I hope you have a great day and remember the human body needs rest so that it may perform at its greatest potential!')
