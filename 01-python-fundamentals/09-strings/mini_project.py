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

password = input("Enter your password")

if password.isalnum() and len(password)>=8 and password.issupper() and password.islower() and password.isalnum() :

    print("Length ✔\nUppercase ✔\nLowercase ✔\nDigit ✔\nSpecial Character ✔")
    print("Strength: Strong")
else:
    print("please write strong password")
