import random


# Function
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
NUM_TRIES = 1

error_message = "This is an invalid input. Please enter an integer between 1 to 100.\n"
num_questions = 10

# Main routine
# Gives the user ten questions
while NUM_TRIES <= num_questions:
    addition(0, 50)
    NUM_TRIES += 1
