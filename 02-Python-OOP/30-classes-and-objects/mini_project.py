"""
Mini Project

Student Record System
"""

class Student:
    pass

student1 = Student()

student1.name = "Ali"
student1.roll_no = "SE101"
student1.department = "Software Engineering"

student2 = Student()

student2.name = "Sara"
student2.roll_no = "SE102"
student2.department = "Computer Science"

students = [student1,student2]
print ('='*40)

for student in students:
    print("Name       :", student.name)
    print("Roll No    :", student.roll_no)
    print("Department :", student.department)
    print("-" * 40)