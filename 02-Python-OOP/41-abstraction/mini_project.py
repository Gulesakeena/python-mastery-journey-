"""
Mini Project

Banking System using Abstraction
"""

from abc import ABC, abstractmethod


class BankAccount(ABC):

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    @abstractmethod
    def calculate_interest(self):
        pass

    def show_details(self):
        print(f"Holder : {self.holder}")
        print(f"Balance : ${self.balance}")


class SavingsAccount(BankAccount):

    def calculate_interest(self):
        return self.balance * 0.05


class CurrentAccount(BankAccount):

    def calculate_interest(self):
        return self.balance * 0.02


accounts = [
    SavingsAccount("Ali", 5000),
    CurrentAccount("Sara", 5000)
]

for account in accounts:
    account.show_details()
    print("Interest:", account.calculate_interest())
    print("-" * 40)