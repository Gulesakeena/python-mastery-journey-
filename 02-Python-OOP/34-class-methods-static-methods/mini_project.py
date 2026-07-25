"""
Mini Project

University Management System
"""

class Student:

    university = "University of Gujrat"

    def __init__(self, name, department):
        self.name = name
        self.department = department

    def display(self):
        print("=" * 40)
        print("Name       :", self.name)
        print("Department :", self.department)
        print("University :", Student.university)

    @classmethod
    def change_university(cls, new_name):
        cls.university = new_name

    @staticmethod
    def university_motto():
        print("Knowledge, Integrity, Excellence")


students = [
    Student("Ali", "Software Engineering"),
    Student("Sara", "Computer Science"),
    Student("Ahmed", "Information Technology")
]

Student.university_motto()
Student.change_university("National University")

for student in students:
    student.display()