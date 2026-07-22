"""
27 - Exception Handling Examples
"""

# ----------------------------------
# ZeroDivisionError
# ----------------------------------
try:
    print(10/0)
except ZeroDivisionError:
    print("Cannot divide by zero")


# ----------------------------------
# ValueError
# ----------------------------------
try:
    age = int(input("Enter ege : "))
except ValueError:
    print("Invalid Number")


# ----------------------------------
# Multiple Exceptions
# ----------------------------------
try:
    number = int(input("Enter number: "))
    print(100 / number)
except ValueError:
    print("Please enter an integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

# ----------------------------------
# else
# ----------------------------------
try:
    x = int(input("Enter x: "))
except ValueError:
    print("Invalid Input")
else:
    print("square : ",x*x)

# ----------------------------------
# finally
# ----------------------------------

try:
    file = open("sample.txt")
except FileNotFoundError:
    print("File not found.")
finally:
    print("Execution completed.")


# ----------------------------------
# raise
# ----------------------------------
age = 18
if age < 0 :
    raise ValueError("Age cannot be negative")
print("Age :",age)

# ----------------------------------
# Custom Exception
# ----------------------------------
class InvalidMarksError(Exception):
    pass

marks = -10
try:
    if marks<0:
        raise InvalidMarksError("Marks cannot be negative ")
except InvalidMarksError as e:
    print(e)
