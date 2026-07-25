"""
Mini Project

Bank Account System
"""

class BankAccount:

    def __init__(self, holder, balance):

        self.holder = holder
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):

        if amount < 0:
            raise ValueError("Balance cannot be negative.")

        self._balance = amount

    def display(self):

        print("=" * 40)
        print("Holder :", self.holder)
        print("Balance:", self.balance)


account = BankAccount("Ali", 5000)

account.display()

account.balance = 8000

account.display()