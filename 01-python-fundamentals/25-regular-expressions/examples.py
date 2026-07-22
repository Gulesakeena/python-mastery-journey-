"""
25 - Python Regular Expressions
"""

import re

text = "Python 3.15 was released in 2026."

# -------------------------
# search()
# -------------------------

print(re.search(r"Python", text))

# -------------------------
# match()
# -------------------------

print(re.match(r"Python", text))

# -------------------------
# fullmatch()
# -------------------------

print(re.fullmatch(r"\d+", "12345"))

# -------------------------
# findall()
# -------------------------

print(re.findall(r"\d+", text))

# -------------------------
# finditer()
# -------------------------

for match in re.finditer(r"\d+", text):
    print(match.group())

# -------------------------
# split()
# -------------------------

print(re.split(r",", "Apple,Banana,Mango"))

# -------------------------
# sub()
# -------------------------

print(re.sub(r"Python", "Java", text))

# -------------------------
# Email Validation
# -------------------------

email = "student@example.com"

pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.fullmatch(pattern, email):
    print("Valid Email")

# -------------------------
# Phone Validation
# -------------------------

phone = "03001234567"

print(bool(re.fullmatch(r"\d{11}", phone)))

# -------------------------
# Extract Words
# -------------------------

sentence = "AI, Python and FastAPI"

print(re.findall(r"\w+", sentence))