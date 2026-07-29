"""
42 - Dataclasses
"""

from dataclasses import dataclass, field

# --------------------------------
# Example 1 - Basic Dataclass
# --------------------------------

@dataclass
class Student:
    name: str
    age: int


student = Student("Ali", 22)
print(student)

# --------------------------------
# Example 2 - Default Values
# --------------------------------

@dataclass
class Employee:
    name: str
    salary: float = 50000


employee = Employee("Sara")
print(employee)

# --------------------------------
# Example 3 - field()
# --------------------------------

@dataclass
class Classroom:
    students: list = field(default_factory=list)


room = Classroom()
room.students.append("Ali")
print(room)

# --------------------------------
# Example 4 - __post_init__()
# --------------------------------

@dataclass
class Product:
    price: float
    quantity: int

    def __post_init__(self):
        self.total = self.price * self.quantity


product = Product(15, 3)
print(product.total)

# --------------------------------
# Example 5 - Frozen Dataclass
# --------------------------------

@dataclass(frozen=True)
class User:
    username: str


user = User("admin")
print(user)

# --------------------------------
# Example 6 - Inheritance
# --------------------------------

@dataclass
class Person:
    name: str


@dataclass
class Teacher(Person):
    subject: str


teacher = Teacher("Ahmed", "Python")
print(teacher)