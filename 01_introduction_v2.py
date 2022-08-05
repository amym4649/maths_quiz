# Introduction to the game
print("Welcome to the Maths Quiz!")
print()

name = input("What is your name? ").capitalize()
print()

played_before = ""
while played_before != "xxx":

    # Ask the user if they have played before
    played_before = input("Hello {}! Have you played this game before? ".format(name)).lower()

    # If 'yes', skip the instructions and continue the program
    if played_before == "yes" or played_before == "y":
        played_before = "yes"
        print("Program continues")

    # If 'no', show instructions then continue the program
    elif played_before == "no" or played_before == "n":
        played_before = "no"
        print("Here are the instructions")

    # If an invalid answer, request either yes / no
    else:
        print("Please enter either yes / no")
