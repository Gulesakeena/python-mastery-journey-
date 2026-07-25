class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0

    def menu(self):
        user_input = int(input("""
            Hello ! how would you like to proceed ?
            1. Enter 1 to create pin
            2. Enter 2 to deposit
            3. Enter 3 to withdraw
            4. Enter 4 to check balance
            5. Enter 5 to exit
            """))

        if user_input == 1:
            print('Create pin')
        if user_input == 2:
            self.deposit()
        if user_input == 3:
            self.withdraw()
        if user_input == 4:
            self.check_balance()
        if user_input == 5:
            print("Buy")

    def create_pin(self):
        self.pin = input("Enter your pin ")
        print("Pin created successfully!")
    def deposit(self):
        temp = input("Enter your pin ")
        if temp == self.pin :
            amount = int(input("Enter the amount : "))
            self.balance = self.balance + amount 
            print("Deposit successfully!")
        else:
            print("Invalid pin")
    def withdraw(self):
        temp = input("Enter your pin ")
        if temp == self.pin :
            amount = int(input("Enter the amount : "))
            if amount <= self.balance :
                self.balance = self.balance - amount
                print("withdraw successfully!")
            else:
                print("Insuffient balance")
        else:
            print("invalid Pin")
    def check_balance(self):
        temp = input("Enter your pin ")
        if temp == self.pin :
            print(self.balance)
        else:
            print("Invalid Pin")
        