import random


# Function
# Generates random number between mini_num and max_num
def random_generator(mini_num, maxi_num):
    num_1 = random.randint(mini_num, maxi_num)
    num_2 = random.randint(mini_num, maxi_num)
    return num_1, num_2


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


def score(num_correct, out_of):
    # Results
    print("You got {}/{} for your quiz!\n".format(len(num_correct), out_of))
    return


# variables
NUM_TRIES = 0

error_message = "This is an invalid input. Please enter an integer between 1 to 100.\n"
num_questions = 2
operator_type = ["+", "-", "x", "÷"]
num_correct_lst = []

# Main routine
# Start the game by <enter>
play_again = input("Press <enter> to play ")
print()

# Gives the user ten questions
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
