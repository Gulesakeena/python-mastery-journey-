"""
Mini Project

Student Record System using Dataclasses
"""

from dataclasses import dataclass, field

@dataclass
class Student:
    id: int
    name: str
    marks: list = field(default_factory=list)

    def __post_init__(self):
        self.average = (
            sum(self.marks) / len(self.marks)
            if self.marks
            else 0
        )

    def display(self):
        print(f"ID      : {self.id}")
        print(f"Name    : {self.name}")
        print(f"Marks   : {self.marks}")
        print(f"Average : {self.average:.2f}")
        print("-" * 35)


students = [
    Student(1, "Ali", [90, 85, 88]),
    Student(2, "Sara", [78, 81, 80]),
]

for student in students:
    student.display()