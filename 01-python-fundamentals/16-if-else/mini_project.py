'''Banking Authentication System

Menu

1 Login

2 Check Balance

3 Deposit

4 Withdraw

5 Exit

Rules

Validate username.
Validate password.
Maximum 3 login attempts.
Minimum balance must remain 500.
Show proper error messages.
Use only conditional statements for decision making.'''

username = "admin"
password = "1234"

balance = 10000
attempts = 0
logged_in = False

while True:

    print("""
========= Banking System =========

1. Login
2. Check Balance
3. Deposit
4. Withdraw
5. Exit

==================================
""")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        if logged_in:
            print("You are already logged in.")

        else:

            while attempts < 3:

                user = input("Enter Username: ")
                pwd = input("Enter Password: ")

                if user == username:

                    if pwd == password:
                        print("Login Successful")
                        logged_in = True
                        break

                    else:
                        attempts += 1
                        print("Incorrect Password")
                        print("Attempts Left:", 3 - attempts)

                else:
                    attempts += 1
                    print("Invalid Username")
                    print("Attempts Left:", 3 - attempts)

            if attempts == 3:
                print("Maximum login attempts reached.")

    elif choice == 2:

        if logged_in:
            print("Current Balance =", balance)
        else:
            print("Please login first.")

    elif choice == 3:

        if logged_in:

            amount = float(input("Enter Deposit Amount: "))

            if amount > 0:
                balance += amount
                print("Deposit Successful")
                print("Current Balance =", balance)

            else:
                print("Invalid Amount")

        else:
            print("Please login first.")

    elif choice == 4:

        if logged_in:

            amount = float(input("Enter Withdrawal Amount: "))

            if amount > 0:

                if amount <= balance:

                    if balance - amount >= 500:

                        balance -= amount
                        print("Withdrawal Successful")
                        print("Remaining Balance =", balance)

                    else:
                        print("Minimum balance of Rs.500 must remain.")

                else:
                    print("Insufficient Balance")

            else:
                print("Invalid Amount")

        else:
            print("Please login first.")

    elif choice == 5:

        print("Thank You!")
        break

    else:
        print("Invalid Choice")