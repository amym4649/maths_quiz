import random


# Function
def addition():
    number_1 = random.randint(0, 50)
    number_2 = random.randint(0, 50)
    answer = number_1 + number_2

    user_answer = int(input("{} + {} = ".format(number_1, number_2)))

    if user_answer == answer:
        print("Correct!\n")

    elif user_answer != answer:
        print("Incorrect!\n"
              "The answer is {}\n".format(answer))

    else:
        print(error_message)


# Variables
error_message = "This is in an invalid input. Please enter an integer between 1 to 100."
num_questions = 3
num_tries = 1

# Main routine
while num_tries <= num_questions:
    print("{}.".format(num_tries))
    addition()
    num_tries += 1
