# Function
def str_checker(question):
    valid = False
    while not valid:
        response = str(input(question).capitalize())
        if response == str:
            return response
            return
        else:
            print(str_error)


# Variable
str_error = "Please try again. Type your name using letters.\n"


name = str_checker("What is your name? ")


