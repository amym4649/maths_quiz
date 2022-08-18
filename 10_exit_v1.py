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
            print("Please enter either yes / no\n")


# Main routine
# Ask the user if they enjoyed the game
had_fun = yes_no("Did you enjoy this game? ")
print()

if had_fun == "yes":
    print("That's great! Glad to hear!\n")

elif had_fun == "no":
    print("Oh no... \n"
          "At least you were able to practice your maths!\n")

# Let the user know that it is the end
print("*** End of game ***\n"
      "Thank you for playing!")
