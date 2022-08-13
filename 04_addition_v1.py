import random

# Main routine
# Variables
x = 1
number_1 = random.randint(0, 50)
number_2 = random.randint(0, 50)
answer = number_1 + number_2
number_of_errors = 0
user_answer = ""
number_of_questions = 11
number_of_tries = 1
error_message = "This is in an invalid input. Please enter an integer between 1 to 100."

# Addition
while user_answer != answer:
    user_answer = int(input("{}. {} + {} = ".format(number_of_tries, number_1, number_2)))

    if user_answer == answer:
        print("Correct!\n")

    elif user_answer != answer:
        print("Incorrect, try again\n")

    else:
        print(error_message)





