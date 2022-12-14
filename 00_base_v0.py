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
                return final_choice

            elif choice_input == type2:
                final_choice = options[1]
                return final_choice

            elif choice_input == type3:
                final_choice = options[2]
                return final_choice

            elif choice_input == type4:
                final_choice = options[3]
                return final_choice

        # Value error message
        except ValueError:
            print(option_error)
            print()


# Generates random number between mini_num and max_num
def random_generator(mini_num, maxi_num):
    num_1 = random.randint(mini_num, maxi_num)
    num_2 = random.randint(mini_num, maxi_num)
    return num_1, num_2


# Addition question function using the numbers from random_generator
def maths_question(num_1, num_2, operator):
    quiz = "{}. {} {} {} = ".format(NUM_TRIES, num_1, operator, num_2)
    return quiz


# Addition answer to the question
def addition_answer(num_1, num_2):
    answer = num_1 + num_2
    return answer


# Subtraction answer to the question
def subtraction_answer(num_1, num_2):
    answer = num_1 - num_2
    return answer


# Multiplication answer to the question
def multiplication_answer(num_1, num_2):
    answer = num_1 * num_2
    return answer


#  Question function using the numbers from random_generator
# To make an integer answer, answer = num_2
def div_quiz(num_1, num_2, operator):
    answer = num_2
    starting_num = num_1 * answer
    quiz = "{}. {} {} {} = ".format(NUM_TRIES, starting_num, operator, num_1)
    return quiz


# Division answer
def division_answer(num_1, num_2):
    answer = num_2
    starting_num = num_1 * answer
    return answer


# Checks the answer with the user input
def answer_checker(quiz, answer, num_correct):
    valid_input = False

    while not valid_input:
        try:
            user_answer = int(input(quiz))

            # If the user enters a correct answer
            if user_answer == answer:
                result = "correct"
                num_correct.append(result)
                print("Correct!\n")
                return num_correct

            # If the user enters and incorrect answer
            elif user_answer != answer:
                print("Incorrect!\n"
                      "The answer is {}\n".format(answer))
                return

        # Value error so repeats the question
        except ValueError:
            print(error_message)


# Calculate the total score
def score(num_correct, out_of):
    # Results
    print("You got {}/{} for your quiz!\n".format(len(num_correct), out_of))
    return


# Constants and variables
ADDITION = 1
SUBTRACTION = 2
MULTIPLICATION = 3
DIVISION = 4
NUM_TRIES = 1

options = ["addition", "subtraction", "multiplication", "division"]
operator_type = ["+", "-", "x", "??"]
num_correct_lst = []

option_error = "This is in an invalid input. Please enter an integer between 1 to 4."
error_message = "This is an invalid input. Please enter an integer between 0 to 100.\n"
error_message_subtraction = "This is an invalid input. Please enter an integer under 100.\n"
num_questions = 10
x = 1

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

# Start the game by <enter>
play_again = input("Press <enter> to play ")
print()

# If user chooses addition (options[0]), give user num_questions of addition questions
if user_choice == options[0]:
    while NUM_TRIES <= num_questions:
        ran_num_1, ran_num_2 = random_generator(0, 50)
        addition_question = maths_question(ran_num_1, ran_num_2, operator_type[0])
        question_answer = addition_answer(ran_num_1, ran_num_2)
        answer_checker(addition_question, question_answer, num_correct_lst)
        NUM_TRIES += 1

        # Results
        score(num_correct_lst, num_questions)
        # Reset result
        num_correct_lst = []

        # Ask if the user wants to play again (the same operator)
        play_again = input("Press <enter> to play again or xxx to exit ")
        print()

# If user chooses subtraction (options[1]), give user num_questions of subtraction questions
if user_choice == options[1]:
    while NUM_TRIES <= num_questions:
        ran_num_1, ran_num_2 = random_generator(0, 100)
        subtraction_question = maths_question(ran_num_1, ran_num_2, operator_type[1])
        question_answer = subtraction_answer(ran_num_1, ran_num_2)
        answer_checker(subtraction_question, question_answer, num_correct_lst)
        NUM_TRIES += 1

        # Results
        score(num_correct_lst, num_questions)
        # Reset result
        num_correct_lst = []

        # Ask if the user wants to play again (the same operator)
        play_again = input("Press <enter> to play again or xxx to exit ")
        print()

# If user chooses multiplication (options[2]), give user num_questions of multiplication questions
if user_choice == options[2]:
    while NUM_TRIES <= num_questions:
        ran_num_1, ran_num_2 = random_generator(0, 10)
        multiplication_question = maths_question(ran_num_1, ran_num_2, operator_type[2])
        question_answer = multiplication_answer(ran_num_1, ran_num_2)
        answer_checker(multiplication_question, question_answer, num_correct_lst)
        NUM_TRIES += 1

        # Results
        score(num_correct_lst, num_questions)
        # Reset result
        num_correct_lst = []

        # Ask if the user wants to play again (the same operator)
        play_again = input("Press <enter> to play again or xxx to exit ")
        print()

# If user chooses division (options[3]), give user num_questions of division questions
if user_choice == options[3]:
    while play_again == "":
        for NUM_TRIES in range(1, num_questions + 1):
            ran_num_1, ran_num_2 = random_generator(1, 10)
            division_question = div_quiz(ran_num_1, ran_num_2, operator_type[3])
            question_answer = division_answer(ran_num_1, ran_num_2)
            answer_checker(division_question, question_answer, num_correct_lst)
            NUM_TRIES += 1

        # Results
        score(num_correct_lst, num_questions)
        # Reset result
        num_correct_lst = []

        # Ask if the user wants to play again (the same operator)
        play_again = input("Press <enter> to play again or xxx to exit ")
        print()

# Ask the user if they enjoyed the game
had_fun = yes_no("Did you enjoy this game? ")
print()

if had_fun == "yes":
    print("That's great! Glad to hear!\n")

elif had_fun == "no":
    print("Oh no... \n"
          "At least you were able to practice your maths!\n")

# Let the user know that it is the end
print("*** End of game ***\n"
      "Thank you for playing!")
