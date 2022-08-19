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
            print("Please enter either yes / no\n")


def instructions():
    print("*** Instructions ***")
    print()
    print("1. Enter your basic facts choice by typing its number\n"
          "2. When a question is given, type in an integer to answer\n"
          "3. Press <return>\n"
          "4. After the round you will receive your score\n"
          "5. Press <return> to play again or type 'xxx' to quit\n")


# Lets the user choose the type of basic fats they want to practice
def user_choice(question):
    valid_input = False

    while not valid_input:
        try:
            user_input = int(input(question))
            # If the user chooses one of the four options
            if 0 < user_input < 5:
                return user_input
            else:
                print(option_error)

        except ValueError:
            print(option_error)


# Generates random number between mini_num and max_num
def ran_generator(mini_num, maxi_num):
    num_1 = random.randint(mini_num, maxi_num)
    num_2 = random.randint(mini_num, maxi_num)
    return num_1, num_2


def quiz(index):
    # Addition
    if index == 1:
        num_1, num_2 = ran_generator(1, 50)
        question = str(num_1) + " + " + str(num_2)
        answer = num_1 + num_2
    # Subtraction
    elif index == 2:
        num_1, num_2 = ran_generator(1, 100)
        question = str(num_1) + " - " + str(num_2)
        answer = num_1 - num_2
    # Multiplication
    elif index == 3:
        num_1, num_2 = ran_generator(1, 10)
        question = str(num_1) + " x " + str(num_2)
        answer = num_1 * num_2
    # Division
    else:
        num_1, num_2 = ran_generator(1, 10)
        divided_num = num_1 * num_2
        question = str(divided_num) + " ÷ " + str(num_1)
        answer = num_2
    return question, answer


# Checks the answer with the user input
def answer_checker(question, answer, num_correct):
    valid_input = False

    while not valid_input:
        try:
            # Basic facts question
            user_answer = int(input("{}. {} = ".format(NUM_TRIES, question)))

            # If the user enters a correct answer
            if user_answer == answer:
                print("Correct!\n")
                result = "correct"
                num_correct.append(result)
                return num_correct

            # If the user enters and incorrect answer
            elif user_answer != answer:
                print("Incorrect!\n"
                      "The answer is {}\n".format(answer))
                return

        # Value error so repeats the question
        except ValueError:
            print(error_message)


# Constants and variables
NUM_TRIES = 1
options = ["addition", "subtraction", "multiplication", "division"]
operator_type = ["+", "-", "x", "÷"]
num_correct_lst = []

option_error = "This is in an invalid input. Please enter an integer between 1 to 4."
error_message = "This is an invalid input. Please enter an integer between 1 to 100.\n"
num_questions = 10
operation_option_number = 1
play_again = ""

# Main routine
# Introduction to the game
print("Welcome to the Maths Quiz!\n")

name = input("What is your name? ").capitalize()
print()

played_before = yes_no("Hi {}! Have you played the game before? ".format(name))
print()

if played_before == "no":
    instructions()

input("Press <enter> to continue")
print()

# Gives the user the basic facts type that they can choose from
print("Here are your options. Choose the one you want to practice.")

for basic_facts_type in options:
    print(operation_option_number, ".", basic_facts_type.capitalize())
    operation_option_number += 1
print()

# User enter their choice
operation_choice = user_choice("Type the number for your operation choice: ")
print()

# The questions get repeated for num_question (10 for the game)
while play_again == "":
    for NUM_TRIES in range(1, num_questions + 1):
        equation, equation_answer = quiz(operation_choice)
        answer_checker(equation, equation_answer, num_correct_lst)
        NUM_TRIES += 1

    # Result
    print("You got {}/{} for your quiz!\n".format(len(num_correct_lst), num_questions))

    # Reset result
    num_correct_lst = []

    # Ask if the user wants to play again (the same operator)
    play_again = input("Press <enter> to play again or xxx to exit ")
    print()

# Ask the user if they enjoyed the game
had_fun = yes_no("Did you enjoy this game? ")
print()

if had_fun == "yes":
    print("That's great! Thank you for playing!\n")

elif had_fun == "no":
    print("Oh no... \n"
          "At least you were able to practice your maths!\n")

# Let the user know that it is the end
print("*** End of game ***\n")
