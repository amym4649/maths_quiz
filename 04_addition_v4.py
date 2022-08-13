import random


# Function
def addition():
    valid_input = False
    number_1 = random.randint(0, 50)
    number_2 = random.randint(0, 50)
    answer = number_1 + number_2

    while not valid_input:
        user_answer = int(input("{}. {} + {} = ".format(NUM_TRIES, number_1, number_2)))

        try:
            # If the user enters correct answer
            if user_answer == answer:
                print("Correct!\n")
                break

            # If the user enters and incorrect answer
            elif user_answer != answer:
                print("Incorrect!\n"
                      "The answer is {}\n".format(answer))
                break

        # Value error so repeats the question
        except ValueError:
            print(error_message)


# Constants and variables
NUM_TRIES = 1

error_message = "This is in an invalid input. Please enter an integer between 1 to 100."
num_questions = 3
num_tries = 1

# Main routine

# Repeats the question 10 times
while NUM_TRIES <= num_questions:
    addition()
    NUM_TRIES += 1
