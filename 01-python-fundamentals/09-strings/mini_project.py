'''mini_project.py
Password Strength Checker

Ask the user for a password.

Check whether it contains:

Uppercase letter
Lowercase letter
Number
Special character
Minimum 8 characters

Output:

Password Report

Length ✔
Uppercase ✔
Lowercase ✔
Digit ✔
Special Character ✔

Strength:
Strong'''

'''
mini_project.py

Password Strength Checker

Requirements:
- Minimum 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- At least one special character
'''

password = input("Enter your password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif not char.isalnum():
        has_special = True

print("\nPassword Report")

if len(password) >= 8:
    print("Length ✔")
else:
    print("Length ✘")

if has_upper:
    print("Uppercase ✔")
else:
    print("Uppercase ✘")

if has_lower:
    print("Lowercase ✔")
else:
    print("Lowercase ✘")

if has_digit:
    print("Digit ✔")
else:
    print("Digit ✘")

if has_special:
    print("Special Character ✔")
else:
    print("Special Character ✘")

if (
    len(password) >= 8
    and has_upper
    and has_lower
    and has_digit
    and has_special
):
    print("\nStrength: Strong 💪")
else:
    print("\nStrength: Weak ❌")
