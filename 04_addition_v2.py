import random

# Main routine
# Variables
number_1 = random.randint(0, 50)
number_2 = random.randint(0, 50)
answer = number_1 + number_2
user_answer = ""
number_of_questions = 10
number_of_tries = 1
error_message = "This is in an invalid input. Please enter an integer between 1 to 100."

# Addition
while number_of_tries <= number_of_questions:
    user_answer = int(input("{}. {} + {} = ".format(number_of_tries, number_1, number_2)))

    if user_answer == answer:
        print("correct")
        number_of_tries += 1

    elif user_answer != answer:
        number_of_tries += 1
        print("Incorrect!\n"
              "The answer is {}".format(answer))

    else:
        print(error_message)





