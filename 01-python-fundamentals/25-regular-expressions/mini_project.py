"""
Email & Password Validator
"""

import re

email = input("Enter Email: ")

password = input("Enter Password: ")

email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

password_pattern = (
    r'^(?=.*[a-z])'
    r'(?=.*[A-Z])'
    r'(?=.*\d)'
    r'.{8,}$'
)

if re.fullmatch(email_pattern, email):
    print("Email: Valid")
else:
    print("Email: Invalid")

if re.fullmatch(password_pattern, password):
    print("Password: Strong")
else:
    print("Password: Weak")