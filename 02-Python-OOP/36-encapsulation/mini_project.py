"""
Mini Project

Employee Management System
"""

class Employee:

    company = "Tech Solutions"

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, amount):

        if amount < 0:
            raise ValueError("Salary cannot be negative.")

        self.__salary = amount

    def display(self):
        print("=" * 40)
        print("Company :", Employee.company)
        print("Employee:", self.name)
        print("Salary  :", self.salary)


employees = [
    Employee("Ali", 50000),
    Employee("Sara", 70000),
    Employee("Ahmed", 65000)
]

employees[0].salary = 55000

for employee in employees:
    employee.display()