"""
Mini Project

Employee Management System
"""


class Employee:

    company = "TechNova Solutions"

    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def display(self):
        print("=" * 45)
        print("Company    :", Employee.company)
        print("Employee ID:", self.emp_id)
        print("Name       :", self.name)
        print("Department :", self.department)
        print("Salary     :", self.salary)


employees = [

    Employee(101, "Ali", "Software", 85000),
    Employee(102, "Sara", "HR", 70000),
    Employee(103, "Ahmed", "Finance", 65000)

]

for emp in employees:
    emp.display()