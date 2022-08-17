import random


# Function
# Generates random number between mini_num and max_num
def random_generator(mini_num, maxi_num):
    num_1 = random.randint(mini_num, maxi_num)
    num_2 = random.randint(mini_num, maxi_num)
    return num_1, num_2


# Addition question function using the numbers from random_generator
def question(num_1, num_2, operator):
    quiz = "{}. {} {} {} = ".format(NUM_TRIES, num_1, operator, num_2)
    return quiz


# Answer to the addition_question
def addition_answer(num_1, num_2):
    answer = num_1 + num_2
    return answer


# Checks the answer with the user input
def answer_checker(quiz, answer):
    valid_input = False

    while not valid_input:
        try:
            user_answer = int(input(quiz))

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
operator_type = ["+", "-", "x", "÷"]

# Main routine
# Gives the user ten questions
while NUM_TRIES <= num_questions:
    ran_num_1, ran_num_2 = random_generator(0, 50)
    addition_question = question(ran_num_1, ran_num_2, operator_type[0])
    question_answer = addition_answer(ran_num_1, ran_num_2)
    answer_checker(addition_question, question_answer)
    NUM_TRIES += 1

