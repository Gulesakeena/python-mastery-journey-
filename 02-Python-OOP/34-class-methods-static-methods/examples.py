"""
34 - Class Methods & Static Methods
"""

# ----------------------------------
# Example 1 - Instance Method
# ----------------------------------

class Student:
    school = "University of Gujrat"

    def __init__(self,name):
        self.name=name

    def display(self):
        print(self.name)

student1 = Student("Ali")
student1.display()

# ----------------------------------
# Example 2 - Class Method
# ----------------------------------

class Employee:
    company = "OpenAI"

    @classmethod
    def show_company(cls):
        print(cls.company)

employee = Employee()
employee.show_company()


# ----------------------------------
# Example 3 - Static Method
# ----------------------------------

class MathUtility:
    @staticmethod
    def square(number):
        return number*number
print(MathUtility.square(6))

# ----------------------------------
# Example 4 - All Three Together
# ----------------------------------
class Car:
    company = "Toyota"

    def __init__(self,model):
        self.model = model
    def display(self):
        print("Model : ",self.model)

    @classmethod
    def company_name(cls):
        print("Comany name",cls.company)

    @staticmethod
    def wheels():
        print("Every standard car has 4 wheels")

car = Car("Corolla")
car.display()
car.company_name()
car.wheels()

