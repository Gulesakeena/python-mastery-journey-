'''mini_project.py
Project: Calculator Module

Create this structure:

calculator_project/
│
├── calculator.py
└── main.py
'''
'''calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# main.py

import calculator

print(calculator.add(10, 20))
print(calculator.subtract(20, 5))
print(calculator.multiply(5, 6))
print(calculator.divide(100, 5))'''