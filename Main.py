# Stephan Bosch

# This program is a study timer that will alert the user to take a break
# as well as give them a randomly assigned task to do during their break.
# The tasks will be selected or input from the user at the beginning of
# the session.

import random
import time


def is_float(user_input):
    try:
        float(user_input)
        return True
    except:
        print("Error with your input.")
        return False


def is_valid_length(user_input):
    if user_input > 0 and user_input % 0.5 == 0:
        return True
    else:
        print("Error with your input.")
        return False


def is_integer(user_input):
    try:
        int(user_input)
        return True
    except:
        print("Error with your input")
        return False


def is_valid_break_interval(user_input):
    if user_input == 25 or user_input == 50:
        return True
    else:
        print("Error with your input.")
        return False


def study_session_length():
    # The next code group asks user for study time and verifies input
    length_proceed = False
    while not length_proceed:
        float_proceed = False
        while not float_proceed:
            # Ask how long they intend to study
            study_length = input("In 0.5 hour increments, how many hours do you intend to study for? ")
            float_proceed = is_float(study_length)
        study_length = float(study_length)
        length_proceed = is_valid_length(study_length)
    return study_length


def break_interval_time():
    # Figure study/break lengths:
    # Some 25/5  fine for studying notes and memorizing materials cite MIT
    # Some 50/10 needed for problem-solving tasks, psets, and writing papers cite MIT
    print("\nStudies show that a study to break ratio of 25:5 is great for note taking and memorizing materials, "
          "while a ratio of 50:10 is better for problem-solving and writing tasks.")
    break_proceed = False
    while not break_proceed:
        integer_proceed = False
        while not integer_proceed:
            # Ask how long they intend to study
            break_interval = input("How often would you like to break? Please enter either 25 or 50. ")
            integer_proceed = is_integer(break_interval)
        break_interval = int(break_interval)
        break_proceed = is_valid_break_interval(break_interval)
    return break_interval


def activities():
    # string array to store break activities
    activities_list = []
    # Prompt user for break activities
    activity_input = input("\nPlease type an activity that you would like to do on"
                           " your break (Type 'End' when done): ")
    integer_proceed = False
    while not integer_proceed:
        # Prompt user for maximum number of times they would like to do this activity
        multiplier = input("Up to how many times would you like to do this activity? ")
        integer_proceed = is_integer(multiplier)
    multiplier = int(multiplier)
    while multiplier >= 1:
        # Add user input to the activities string array
        activities_list.append(activity_input)
        multiplier -= 1
    while activity_input != "End" and activity_input != "end":
        activity_input = input("Please type another activity that you would like "
                               "to do on your break: ")
        if activity_input == "End" or activity_input == "end":
            break
        integer_proceed = False
        while not integer_proceed:
            multiplier = input("Up to how many times would you like to do this activity? ")
            integer_proceed = is_integer(multiplier)
        multiplier = int(multiplier)
        while multiplier >= 1:
            activities_list.append(activity_input)
            multiplier -= 1
    random.shuffle(activities_list)
    return activities_list


def number_breaks(study_time, break_interval):
    if break_interval == 25:
        break_cycles = int(study_time / 0.5)
        return break_cycles
    elif break_interval == 50:
        break_cycles = int(study_time // 1)
        return break_cycles


def is_ready():
    user_ready = input("Are you ready to begin? Please type 'Yes' or 'yes': ")
    if user_ready == 'Yes' or user_ready == 'yes':
        return True
    else:
        print("Invalid input.")
        return False


# Timer - taken directly from https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/
# PyCharm interpreter doesn't actually show timer. How do I go about making sure the clock is shown?
def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1
    return False


def interval_timer(break_interval, number_of_breaks, activities):
    if break_interval == 25:
        study_time_seconds = 25 * 60
        break_time_seconds = 5 * 60
    elif break_interval == 50:
        study_time_seconds = 50 * 60
        break_time_seconds = 10 * 60
    for i in range(number_of_breaks):
        run_timer = False
        while not run_timer:
            run_timer = is_ready()
        while run_timer:
            print("Happy studying!")
            countdown(study_time_seconds)
            print("It's break time! Your break activity is:", activities[0])
            activities.pop(0)
            run_timer = countdown(break_time_seconds)
            print("Time to return to studying!")


def run_timer_again():
    print("The timer program has ended.")
    run_again = input("Would you like to restart the timer? Please type 'Yes' or 'yes': ")
    if run_again == 'Yes' or run_again == 'yes':
        main()
    else:
        print("Goodbye.")


def main():
    # Greeting to the user
    print("Welcome to the Study Timer!\n")
    # Get the amount on time the person wants to study for
    study_length = study_session_length()
    # Ask how often they want to break
    break_interval = break_interval_time()
    # Ask the user what activities they would like to do during break
    shuffled_list_of_activities = activities()
    # Determine number of breaks
    number_of_breaks = number_breaks(study_length, break_interval)
    # Start timer
    interval_timer(break_interval, number_of_breaks, shuffled_list_of_activities)
    # Ask user to start over
    run_timer_again()


main()

def do_you_want_to_call_other_code():
    call_code = False
    while not call_code:
        user_input = input("Would you like to run the random code? ")
        if user_input == 'Yes' or user_input == 'yes':
            other_sprint_code()
            call_code = True
        elif user_input == 'No' or user_input == 'no':
            break
        else:
            print("Answer not understood. please type 'yes' or 'no'.")

# Other lines of code to meet Sprint requirements:
def other_sprint_code():
    print("The following is other random code.")
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    print(num1 + num2)  # adds them together
    print(num1 - num2)  # subtracts num2 from num1
    print(num1 * num2)  # multiplies together
    print(num1 / num2)  # divides num1 by num2
    print(num1 ** num2)  # raises num1 to the power of num2
    print(num1 // num2)  # how many whole number times num1 is divided by num2
    print(num1 % num2)  # remainder of num1 divided by num2
    print("Give me a good grade. " * 10)  # prints the string literal 10 times #
    print("Where" + "did" + "my" + "spaces" + "go?")  # joins the string literals with no spaces
    print("The sep= function", "overrides the comma",
          sep=': ')  # instead of a space with the comma, it inserted a colon then a space

do_you_want_to_call_other_code()