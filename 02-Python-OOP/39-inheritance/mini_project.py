"""
Employee Management System
"""


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Employee : {self.name}")
        print(f"Salary   : ${self.salary}")


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display(self):
        super().display()
        print(f"Department : {self.department}")


class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def display(self):
        super().display()
        print(f"Language : {self.language}")


manager = Manager("Sara", 90000, "AI")
developer = Developer("Ali", 80000, "Python")

print("=" * 40)
manager.display()

print("=" * 40)
developer.display()