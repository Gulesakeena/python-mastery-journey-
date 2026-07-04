'''Calculator with Safe Input

Requirements:

Ask user for two numbers.
Convert input using float().
Handle invalid input.
Perform:
Addition
Subtraction
Multiplication
Division
Handle division by zero.
Display clear error messages.

This combines type casting with exception handling, just like real applications.'''


def calculator(num1,num2):

  print("addition : " , num1 + num2)
  print("subtraction : " , num1 - num2)
  print("multiplication : " , num1 * num2)
  if num2 == 0 :
      print("division by zero error")
  else:
      print("devision : " , num1 / num2)
try:
    num1 = float(input("Enter 1st number"))
    num2 = float(input("Enter 2nd number"))
    calculator(num1,num2)
except:
    print("Please enter valid numbers.")




