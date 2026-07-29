"""
41 - Abstraction
"""

from abc import ABC, abstractmethod

# ---------------------------------
# Example 1 - Basic Abstract Class
# ---------------------------------

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Dog: Bark")


dog = Dog()
dog.sound()

# ---------------------------------
# Example 2 - Multiple Methods
# ---------------------------------

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


rectangle = Rectangle(10, 5)

print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())

# ---------------------------------
# Example 3 - Payment System
# ---------------------------------

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(Payment):

    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card")


payment = CreditCard()

payment.pay(500)

# ---------------------------------
# Example 4 - Vehicle
# ---------------------------------

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car Started")


Car().start()