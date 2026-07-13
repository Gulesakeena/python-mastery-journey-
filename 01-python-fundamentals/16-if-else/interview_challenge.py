'''Challenge 1

Predict the output.

x = 10

if x:
    print("Hello")'''
# Hello

'''Challenge 2

Explain:

if []:
    print("True")
else:
    print("False")'''
# False

'''Challenge 3

Difference between

==

and

is'''
# ==  → compares values

# is  → compares memory location (object identity)

'''Challenge 4

Predict.

print(True and False or True)

Explain operator precedence.'''
# True and False or True --> False or True --> True 
'''
operator precedence
()

**

not

and

or'''



'''Challenge 5

Predict.

x = None

if x:
    print("A")
else:
    print("B")'''
# B

'''Challenge 6

Rewrite nested if into cleaner code.'''
member_id = 3
option = 1

id = int(input("Enter ID: "))

if option == 1 and id == member_id:
    print("Member")
else:
    print("Not a Member")

'''Challenge 7

Implement login without nested if.'''
username = "Gul"
password = "12345"

if username == "Gul" and password == "12345":
    print("Login succfully ")
else:
    print("Failed to login")

'''Challenge 8

Difference between

if x == True

and

if x'''
# if x == True
# Checks whether x is exactly equal to True.

# if x
# Checks whether x is truthy (non-zero, non-empty, not None, etc.).

'''Challenge 9

Explain short-circuit evaluation with examples.

'''

# Short-Circuit Evaluation

#Python stops evaluating as soon as the final result is known.

#Example 1

False and print("Hello")

#Output

# Nothing Because
'''
False AND anything

is always False
'''

# so Python never evaluates the second part.

'''Challenge 10

Implement grading using match-case.'''
grade = input("Enter Grade (A/B/C/D/F): ").upper()

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Very Good")
    case "C":
        print("Good")
    case "D":
        print("Pass")
    case "F":
        print("Fail")
    case _:
        print("Invalid Grade")