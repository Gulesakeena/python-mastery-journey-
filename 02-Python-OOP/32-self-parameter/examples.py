"""
32 - self Parameter
"""

# ----------------------------------
# Example 1
# ----------------------------------

class Student:

    def __init__(self, name):
        self.name = name

student = Student("Ali")

print(student.name)

# ----------------------------------
# Example 2
# ----------------------------------

class Car:

    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print("Brand:", self.brand)

car = Car("Toyota")

car.display()

# ----------------------------------
# Example 3
# ----------------------------------

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

employee = Employee("Sara", 85000)

print(employee.name)
print(employee.salary)

# ----------------------------------
# Example 4
# ----------------------------------

class Book:

    def __init__(self, title):
        self.title = title

    def show(self):
        print("Book:", self.title)

book = Book("Python Crash Course")

book.show()

# ----------------------------------
# Example 5
# ----------------------------------

class Laptop:

    def __init__(self, brand):
        self.brand = brand

laptop1 = Laptop("Dell")
laptop2 = Laptop("HP")

print(laptop1.brand)
print(laptop2.brand)