'''Scientific Calculator

Menu:

1 Addition
2 Subtraction
3 Multiplication
4 Division
5 Modulus
6 Power
7 Floor Division

User enters:

Choice:
Number 1:
Number 2:

Display result.

Handle division by zero.

Repeat until user exits.'''


while True:
    print("""
========== Scientific Calculator ==========

1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus
6. Power
7. Floor Division
8. Exit

===========================================
""")

    # Take user's choice
    choice = input("Enter your choice (1-8): ")

    # Exit option
    if choice == "8":
        print("Thank you for using the calculator!")
        break

    # Validate choice
    if choice not in ("1", "2", "3", "4", "5", "6", "7"):
        print(" Invalid choice! Please try again.\n")
        continue

    # Take numbers
    number_1 = float(input("Enter 1st number: "))
    number_2 = float(input("Enter 2nd number: "))

    # Handle division by zero
    if choice in ("4", "5", "7") and number_2 == 0:
        print(" Error: Division by zero is not allowed.\n")
        continue

    # Perform calculation
    if choice == "1":
        result = number_1 + number_2

    elif choice == "2":
        result = number_1 - number_2

    elif choice == "3":
        result = number_1 * number_2

    elif choice == "4":
        result = number_1 / number_2

    elif choice == "5":
        result = number_1 % number_2

    elif choice == "6":
        result = number_1 ** number_2

    elif choice == "7":
        result = number_1 // number_2

    # Display result
    print(f"\n Result: {result}\n")