# Stephan Bosch

# This program is a study timer that will alert the user to take a break
# as well as give them a randomly assigned task to do during their break.
# The tasks will be selected or input from the user at the beginning of
# the session.

import random
import time

# Greeting to the user
print("Welcome to the Study Timer!\n")

# Ask how long they intend to study
study_length = float(input("In 0.5 hour increments, how many hours do you intend to study for? "))

# while loop determining whether user input is acceptable, remainder of user input must equal zero
while study_length % 0.5 != 0:
    print("\nError with your input.\n")
    study_length = float(input("In 0.5 hour increments, how many hours do you intend to study for? "))
    if study_length % 0.5 == 0:
        break

# Figure study/break lengths:
# Some 25/5  fine for studying notes and memorizing materials cite MIT
# Some 50/10 needed for problem-solving tasks, psets, and writing papers cite MIT
print("\nStudies show that a study to break ratio of 25:5 is great for note taking and memorizing materials, "
      "while a ratio of 50:10 is better for problem-solving and writing tasks.") # Need to fit to window length
      
break_interval = int(input("\nAfter how many minutes of studying would you like to break? Please enter either 25 or 50: "))

# while loop determining whether user imput is acceptable: either 25 or 50

while break_interval != 25 and break_interval != 50:
    print("\nError with your input.\n")
    break_interval = int(input("After how many minutes of studying would you like to break? Please enter either 25 or 50: "))
    if break_interval == 25 or break_interval == 50:
        break

# string array to store break activities                  
activities = []

# Prompt user for break activities
# Add user input to the activities string array
# Prompt user for maximum number of times they would like to do this acitivity
activity_input = input("\nPlease type an activity that you would like to do on"
" your break (Type 'End' when done): ")
multiplier = int(input("Up to how many times would you like to do this activity? "))
while multiplier >= 1:
    activities.insert(len(activities),activity_input)
    multiplier = multiplier - 1
        
# kills after second input. Any advice? Happened after I inserted the multiplier inputs/loops
while activity_input != "End" and activity_input != "end":
    activity_input = input("Please type another activity that you would like "
    "to do on your break: ")
    if activity_input == "End" or activity_input == "end":
        break
    multiplier = int(input("Up to how many times would you like to do this "
    "activity? "))
    while multiplier >= 1:
        activities.insert(len(activities),activity_input)
        multiplier = multiplier - 1

# Shuffle the activities array
# random.sample() returns a new shuffled list. The original list remains unchanged.
# random.shuffle() The original list can be shuffled in place by using this
random.shuffle(activities)
print("\nYou have selected", activities, "as your activities.") # will need to fix to format correctly                
# Offer reminders:
# Turn off phone while studying and on only during breaks
# Get up and move on breaks
# Eat healthy snacks

# Change user input for study hour to seconds:
study_length_seconds = int(study_length * 3600)

# Timer - taken directly from https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/ 
def countdown(study_length_seconds): 
    
    while study_length_seconds: 
        mins, secs = divmod(study_length_seconds, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end='\r')
        time.sleep(1) 
        study_length_seconds -= 1
        
# User input for start study timer
are_you_ready = input("Are you ready to start? ")

while are_you_ready != "Yes" and are_you_ready != "yes":
    are_you_ready = input("Type 'Yes' when ready: ")
    if are_you_ready == "Yes" or are_you_ready == "yes":
        break
        
# Timer starts    
# function call
countdown(study_length_seconds)

# If studying more than 3 hours, give a 20 min break in the second or third hour

# Sound alarm and display activity when timer reaches zero

# Option to switch to between 25 and 50 min timers between sessions

# Other lines of code to meet Sprint 1 requirements:
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print(num1 + num2) # adds them together
print(num1 - num2) # subratcts num2 from num1
print(num1 * num2) # multiplies together
print(num1 / num2) # divides num1 by num2
print(num1 ** num2) # raises num1 to the power of num2
print(num1 // num2) # how many whole number times num1 is divided by num2
print(num1 % num2) # remainder of num1 divided by num2
print("Give me a good grade. " * 10) # prints the string literal 10 times # 
print("Where" + "did" + "my" + "spaces" + "go?") # joins the string literals with no spaces
print("The sep= function","overrides the comma", sep=': ') # instead of a space with the comma, it inserted a colon then a space
