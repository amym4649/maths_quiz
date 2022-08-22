# Function


def str_checker(question, error_message):
    valid = False
    while not valid:
        response = input(question).capitalize()

        if response.isalpha():
            return response
        else:
            print(error_message)


# Variable
str_error = "Please try again. Type your name using letters.\n"

# Main routine
name = str_checker("What is your name? ", str_error)



