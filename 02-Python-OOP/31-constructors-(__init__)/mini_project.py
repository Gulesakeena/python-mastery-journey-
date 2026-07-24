"""
Employee Management System
"""


class Employee:

    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary


employees = [

    Employee(101, "Ali", "Software", 70000),

    Employee(102, "Sara", "HR", 65000),

    Employee(103, "Ahmed", "Finance", 60000),

    Employee(104, "Ayesha", "Marketing", 62000)

]

print("=" * 50)

for emp in employees:

    print(f"ID         : {emp.emp_id}")

    print(f"Name       : {emp.name}")

    print(f"Department : {emp.department}")

    print(f"Salary     : {emp.salary}")

    print("-" * 50)