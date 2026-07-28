"""
38 - Aggregation
"""

# ------------------------------------
# Example 1
# ------------------------------------

class Student:

    def __init__(self, name):
        self.name = name


class University:

    def __init__(self, student):
        self.student = student

    def display(self):
        print("Student:", self.student.name)


student = Student("Ali")

university = University(student)

university.display()

# ------------------------------------
# Example 2
# ------------------------------------

class Employee:

    def __init__(self, name):
        self.name = name


class Company:

    def __init__(self, employee):
        self.employee = employee

    def show(self):
        print(self.employee.name)


employee = Employee("Sara")

company = Company(employee)

company.show()

# ------------------------------------
# Example 3
# ------------------------------------

class Engine:

    def __init__(self, horsepower):
        self.horsepower = horsepower


class Car:

    def __init__(self, engine):
        self.engine = engine

    def details(self):
        print(f"Horsepower: {self.engine.horsepower}")


engine = Engine(180)

car = Car(engine)

car.details()

# ------------------------------------
# Example 4
# ------------------------------------

class Department:

    def __init__(self, name):
        self.name = name


class UniversityDepartment:

    def __init__(self, department):
        self.department = department

    def show(self):
        print(self.department.name)


department = Department("Software Engineering")

uni = UniversityDepartment(department)

uni.show()

# ------------------------------------
# Example 5
# ------------------------------------

class Laptop:

    def __init__(self, brand):
        self.brand = brand


class EmployeeLaptop:

    def __init__(self, laptop):
        self.laptop = laptop

    def display(self):
        print(self.laptop.brand)


laptop = Laptop("Dell")

owner = EmployeeLaptop(laptop)

owner.display()