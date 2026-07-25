"""
35 - Properties, Getters & Setters
"""

# ---------------------------------
# Example 1
# ---------------------------------

class Student:
    def __init__(self,age):
        self._age = age

    @property
    def age(self):
        return self._age

student = Student(22)
student.age

# ---------------------------------
# Example 2
# ---------------------------------
class Employee:
    def __init__(self,salary):
        self._salary = salary
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self,value):
        if value>0:
            self._salary = value
        else:
            raise ValueError("Salary cannot be negative.")
employee = Employee(60000)
employee._salary = 650000
print(employee.salary)

# ---------------------------------
# Example 3
# ---------------------------------

class Circle:

    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14159 * self._radius ** 2

circle = Circle(5)

print(circle.area)

# ---------------------------------
# Example 4
# ---------------------------------

class Product:

    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):

        if value <= 0:
            raise ValueError("Price must be greater than zero.")

        self._price = value

product = Product(100)

product.price = 150

print(product.price)

# ---------------------------------
# Example 5
# ---------------------------------

class Temperature:

    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

temp = Temperature(25)

print(temp.fahrenheit)

    
