# Simple if

age = 20
if age >= 20:
    print("Eligible")

# if else
age = 20
if age >= 20:
    print("Eligible")
else:
    print("Not eligible")

# if elif else
marks = 87

if marks >= 90:
    grade = 'A+'
elif marks >= 80:
    grade = 'A'
elif marks >= 70:
    grade = "B"
else:
    grade = "Fail"

print(grade)

# Logical Operators
username = "Gul"
password = "python"

if username =="Gul" and password == "python":
    print("loin successfully")

# Membership
marks = [10,20,30,40,50]
if 50 in marks:
    print("pass")

# Membership
a = [1,2]
b = a
print(a is b)

# Truthy / Falsy
item = []
if item :
    print("Not Empty")
else:
    print("Not Empty")

# Ternary Operator
age = 22
message = "adult" if age >= 18 else "Minor"
print(message)

# Match Case
status = 404

match status:
    case 200:
        print("Success")
    case 404:
        print("Not Found")
    case _:
        print("Unknown")