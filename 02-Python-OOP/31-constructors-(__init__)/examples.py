"""
31 - Constructors (__init__)
"""

# ----------------------------------
# Example 1
# ----------------------------------

class Student:
    def __init__(self):
        print("Student Object is created")
student = Student()

# ----------------------------------
# Example 2
# ----------------------------------

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = self.salary

employee = Employee("Ali",2000)
print(employee.salary)
print(employee.name)

# ----------------------------------
# Example 3
# ----------------------------------

employee2 = Employee("Sara", 75000)

print(employee2.name)
print(employee2.salary)

# ----------------------------------
# Example 4
# ----------------------------------

class Car:

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color


car1 = Car("Toyota", "White")
car2 = Car("Honda", "Black")

print(car1.brand)
print(car2.brand)

# ----------------------------------
# Example 5
# ----------------------------------

class Laptop:

    def __init__(self, brand, ram=8):
        self.brand = brand
        self.ram = ram


laptop = Laptop("Dell")

print(laptop.brand)
print(laptop.ram)

