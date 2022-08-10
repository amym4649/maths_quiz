# Function
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        # If 'yes', skip instructions
        if response == "yes" or response == "y":
            response = "yes"
            return response

        # If 'no', show instructions then continue the program
        elif response == "no" or response == "n":
            response = "no"
            return response

        # If an invalid answer, request either yes / no
        else:
            print("Please enter either yes / no")


# Main routine

# Introduction to the game
print("Welcome to the Maths Quiz!")
print()

name = input("What is your name? ").capitalize()
print()

# Asks the user if they have played before
played_before = yes_no("Hi {}! Have you played the game before? ".format(name))
print()

print("You chose {}.".format(played_before))
