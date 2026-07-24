"""
Mini Project

Bank Account Demo
"""

class BankAccount:

    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def display(self):
        print("=" * 40)
        print("Account Number :", self.account_number)
        print("Holder Name    :", self.holder_name)
        print("Balance        :", self.balance)


accounts = [

    BankAccount("PK1001", "Ali", 50000),
    BankAccount("PK1002", "Sara", 75000),
    BankAccount("PK1003", "Ahmed", 65000)

]

for account in accounts:
    account.display()