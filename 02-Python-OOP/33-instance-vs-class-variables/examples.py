"""
33 - Instance Variables vs Class Variables
"""

# ----------------------------------
# Example 1
# ----------------------------------

class Student:

    school = "University of Gujrat"   # Class Variable

    def __init__(self, name):
        self.name = name              # Instance Variable


s1 = Student("Ali")
s2 = Student("Sara")

print(s1.name)
print(s2.name)

print(s1.school)
print(s2.school)

# ----------------------------------
# Example 2
# ----------------------------------

Student.school = "FAST University"

print(s1.school)
print(s2.school)

# ----------------------------------
# Example 3
# ----------------------------------

s1.name = "Ahmed"

print(s1.name)
print(s2.name)

# ----------------------------------
# Example 4
# ----------------------------------

class Employee:

    company = "OpenAI"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


e1 = Employee("Ali", 50000)
e2 = Employee("Sara", 70000)

print(e1.company)
print(e2.company)

# ----------------------------------
# Example 5
# ----------------------------------

print(Employee.company)
print(e1.company)

print(type(e1))