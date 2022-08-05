# Introduction to the game
print("Welcome to the Maths Quiz!")
print()

name = input("What is your name? ")
print()

played_before = ""
while played_before != "xxx":

    # Ask the user if they have played before
    played_before = input("Hello {}! Have you played this game before? ".format(name)).lower()

    # If 'yes', skip the instructions and continue the program
    if played_before == "yes":
        print("Program continues")

    elif played_before == "y":
        print("Program continues")

    # If 'no', show instructions then continue the program
    elif played_before == "no":
        print("Here are the instructions")

    elif played_before == "n":
        print("Here are the instructions")

    # If an invalid answer, request either yes / no
    else:
        print("Please enter either yes / no")
