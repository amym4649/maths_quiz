print("Choose the type of basic facts by typing the number.")
print()
print("1. Addition\n"
      "2. Subtraction\n"
      "3. Multiplication\n"
      "4. Division\n")

choice = int(input("Type your choice here: "))

if choice == 1:
    choice = "addition"

elif choice == 2:
    choice = "subtraction"

elif choice == 3:
    choice = "subtraction"

elif choice == 4:
    choice = "division"

else:
    print("This is in an invalid input. Please enter an integer between 1 to 4.")

print()
print("You chose {}".format(choice))
