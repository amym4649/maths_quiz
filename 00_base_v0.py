"""
Base component for the game 'maths_quiz'
v0 - skeleton script

author - Amy Macpherson
CC AM 2022
"""

import random


# Functions
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        # If 'no', show instructions then continue the program
        elif response == "no" or response == "n":
            response = "no"
            return response

        # If an invalid answer, request either yes / no
        else:
            print("Please enter either yes / no")


def instructions():
    print("*** Instructions ***")
    print()
    print("1. Choose the type of basic facts you want to practice\n"
          "2. When a question is given, type in an integer to answer\n"
          "3. Press the 'return' key\n"
          "4. To exit the game, type 'xxx'\n"
          "5. After the round you will receive your score\n")


def which_type(type1, type2, type3, type4):
    choice_input = 0
    final_choice = ""
    valid_input = False

    # User input for their choice of basic facts
    while not valid_input:
        try:
            choice_input = int(input("Type your choice here: "))

            if choice_input == type1:
                final_choice = options[0]
                valid_input = True
                return final_choice

            elif choice_input == type2:
                final_choice = options[1]
                valid_input = True
                return final_choice

            elif choice_input == type3:
                final_choice = options[2]
                valid_input = True
                return final_choice

            elif choice_input == type4:
                final_choice = options[3]
                valid_input = True
                return final_choice

            else:
                print(option_error)
                print()

        # Value error message
        except ValueError:
            print(option_error)
            print()


def addition(minimum_number, maximum_number):
    valid_input = False
    number_1 = random.randint(minimum_number, maximum_number)
    number_2 = random.randint(minimum_number, maximum_number)
    answer = number_1 + number_2

    while not valid_input:
        try:
            user_answer = int(input("{}. {} + {} = ".format(NUM_TRIES, number_1, number_2)))

            # If the user enters a correct answer
            if user_answer == answer:
                print("Correct!\n")
                return

            # If the user enters and incorrect answer
            elif user_answer != answer:
                print("Incorrect!\n"
                      "The answer is {}\n".format(answer))
                return

        # Value error so repeats the question
        except ValueError:
            print(error_message)


# Constants and variables
ADDITION = 1
SUBTRACTION = 2
MULTIPLICATION = 3
DIVISION = 4
NUM_TRIES = 1

x = 1
option_error = "This is in an invalid input. Please enter an integer between 1 to 4."
options = ["addition", "subtraction", "multiplication", "division"]
error_message = "This is an invalid input. Please enter an integer between 1 to 100.\n"
num_questions = 10

# Main routine
# Introduction to the game
print("Welcome to the Maths Quiz!\n")

name = input("What is your name? ").capitalize()
print()

played_before = yes_no("Hi {}! Have you played the game before? ".format(name))
print()

print("You chose {}.\n".format(played_before))

if played_before == "no":
    instructions()

# Display the basic facts options
print("Choose the type of basic facts by typing the number.\n")

for basic_facts_type in options:
    print(x, ".", basic_facts_type.capitalize())
    x += 1

print()

# Where user types in their choice
user_choice = which_type(ADDITION, SUBTRACTION, MULTIPLICATION, DIVISION)
print()
print("You chose {}. Let's do this!\n".format(user_choice))

# If user chooses addition (options[0]), give user 10 addition questions
if user_choice == options[0]:
    while NUM_TRIES <= num_questions:
        addition(0, 50)
        NUM_TRIES += 1
