# Main routine
# Constants
ADDITION = 1
SUBTRACTION = 2
MULTIPLICATION = 3
DIVISION = 4

# Variables
choice_input = 0
x = 1
final_choice = ""
valid_input = False
error = "This is in an invalid input. Please enter an integer between 1 to 4."

options = ["addition", "subtraction", "multiplication", "division"]

# Display the basic facts options
print("Choose the type of basic facts by typing the number.\n")

for basic_facts_type in options:
    print(x, ".", basic_facts_type.capitalize())
    x += 1

print()

# User input for their choice of basic facts
while not valid_input:
    try:
        choice_input = int(input("Type your choice here: "))

        if choice_input == ADDITION:
            final_choice = options[0]
            valid_input = True

        elif choice_input == SUBTRACTION:
            final_choice = options[1]
            valid_input = True

        elif choice_input == MULTIPLICATION:
            final_choice = options[2]
            valid_input = True

        elif choice_input == DIVISION:
            final_choice = options[3]
            valid_input = True

        else:
            print(error)
            print()

    # Value error message
    except ValueError:
        print(error)
        print()

print()
print("You chose {}.".format(final_choice))
