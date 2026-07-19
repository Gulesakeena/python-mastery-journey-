# Basic Function
def greet():
    return "Hello World"

print(greet())

# Parameters
def add(a,b):
    return a+b
print(add(2,3))

# Default Arguments
def info(name="ali",age=21):
    print(f"my name is {name} and age is {age} .")
info()
print(info(name="Gul",age=22))

# Keyword Arguments
def info(name="ali",age=21):
    print(f"my name is {name} and age is {age} .")
info()
print(info(name="Gul",age=22))

# *args
def add(*numbers):

    total = 0

    for num in numbers:
        total += num

    print(total)

print(add(10,20,30))

# **kwargs
def student(**info):
    print(info)
print(student(name="ali",age=21))

# Return Values
def sub(a,b):
    return a-b
print(sub(10,6))

# Recursion
def multi(a, b):
    if b == 0:
        return 0
    else:
        return a + multi(a, b - 1)

print(multi(4, 4))

# Lambda
add = lambda a,b : a+b
print(add(2,4))

# Type Hints
def add(a:int , b:int):
    return a+b
print(add(3,2))

# Docstrings
def add(a,b):

    """
    Returns the sum of two numbers.
    """

    return a+b
print(add.__doc__)