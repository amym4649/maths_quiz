import random


# Function
# Lets the user choose the type of basic fats they want to practice
def user_choice(question):
    valid_input = False

    while not valid_input:
        try:
            user_input = int(input(question))
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
    if index == 1:
        num_1, num_2 = ran_generator(0, 50)
        question = str(num_1) + " + " + str(num_2)
        answer = num_1 + num_2
    elif index == 2:
        num_1, num_2 = ran_generator(0, 100)
        question = str(num_1) + " - " + str(num_2)
        answer = num_1 - num_2
    elif index == 3:
        num_1, num_2 = ran_generator(0, 10)
        question = str(num_1) + " x " + str(num_2)
        answer = num_1 * num_2
    else:
        num_1, num_2 = ran_generator(1, 10)
        divided_num = num_1 * num_2
        question = str(divided_num) + " ÷ " + str(num_1)
        answer = num_2
    return question, answer


# Checks the answer with the user input
def answer_checker(question, answer):
    valid_input = False

    while not valid_input:
        try:
            user_answer = int(input(question + " = "))

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


# variables
NUM_TRIES = 1

error_message = "This is an invalid input. Please enter an integer between 1 to 100.\n"
num_questions = 10
option_error = "This is in an invalid input. Please enter an integer between 1 to 4."
options = ["addition", "subtraction", "multiplication", "division"]
option_number = 1

# Main routine
print("Choose the type of basic facts by typing the number.")

for basic_facts_type in options:
    print(option_number, ".", basic_facts_type.capitalize())
    option_number += 1
print()

operation_choice = user_choice("Type the number for your operation choice: ")
print()

# loop
equation, equation_answer = quiz(operation_choice)

answer_checker(equation, equation_answer)



