'''ATM Simulator'''

balance = 1000
history = []

while True:

    print("""
========== ATM MENU ==========
1. Deposit
2. Withdraw
3. Balance
4. History
5. Exit
==============================
""")

    choice = input("Enter your choice: ")

    if not choice.isdigit():
        print("Invalid input! Please enter a number.")
        continue

    choice = int(choice)

    if choice == 1:

        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            history.append(f"Deposited: {amount}")
            print("Deposit Successful.")
        else:
            print("Invalid amount.")

    elif choice == 2:

        amount = float(input("Enter withdrawal amount: "))

        if amount > 0:

            if amount <= balance:

                if balance - amount >= 500:
                    balance -= amount
                    history.append(f"Withdrawn: {amount}")
                    print("Withdrawal Successful.")
                else:
                    print("Minimum balance of 500 must remain.")

            else:
                print("Insufficient balance.")

        else:
            print("Invalid amount.")

    elif choice == 3:

        print(f"Current Balance: {balance}")

    elif choice == 4:

        if len(history) == 0:
            print("No transactions yet.")
        else:
            print("\nTransaction History")
            for transaction in history:
                print(transaction)

    elif choice == 5:

        print("Thank you for using the ATM.")
        break

    else:

        print("Invalid menu choice.")
        continue