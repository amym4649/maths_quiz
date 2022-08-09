"""
Base component for the game 'maths_quiz'
v0 - skeleton script

author - Amy Macpherson
CC AM 2022
"""


# Functions
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

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


def instructions():
    print("*** Instructions ***")
    print()
    print("1. Choose the type of basic facts you want to practice\n"
          "2. When a question is given, type in an integer to answer\n"
          "3. Press the 'return' key\n"
          "4. To exit the game, type 'xxx'\n"
          "5. After the round you will receive your score")


# Main routine

# Introduction to the game
print("Welcome to the Maths Quiz!")
print()

name = input("What is your name? ").capitalize()
print()

played_before = yes_no("Hi {}! Have you played the game before? ".format(name))
print()

print("You chose {}.".format(played_before))
print()

if played_before == "no":
    instructions()

