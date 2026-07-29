"""
Mini Project

Payment Processing System
"""


class Payment:
    def pay(self, amount):
        pass


class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card")


class PayPal(Payment):
    def pay(self, amount):
        print(f"Paid ${amount} using PayPal")


class BankTransfer(Payment):
    def pay(self, amount):
        print(f"Paid ${amount} using Bank Transfer")


payments = [
    CreditCard(),
    PayPal(),
    BankTransfer()
]

for payment in payments:
    payment.pay(500)