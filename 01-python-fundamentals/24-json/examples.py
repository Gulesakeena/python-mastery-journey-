"""
24 - Python JSON
"""

import json

# -------------------------
# Dictionary to JSON
# -------------------------
student = {
    "name": "Alice",
    "age": 22,
    "skills": ["Python", "AI", "FastAPI"]
}

json_text = json.dumps(student)
print(json_text)

# -------------------------
# Pretty Print
# -------------------------

print(json.dumps(student,indent=4))

# -------------------------
# Sort Keys
# -------------------------
print(json.dumps(student,indent=4,sort_keys=True))

# -------------------------
# JSON String to Dictionary
# -------------------------

text = '{"city":"Lahore","country":"Pakistan"}'
data = json.loads(text)
print(data)
print(type(data))


# -------------------------
# Write JSON File
# -------------------------
with open("student","w") as file:
    json.dumps(student,file,indent=4)

# -------------------------
# Read JSON File
# -------------------------

with open("student") as file:
    data=json.load(file)
print(file)

# -------------------------
# Error Handling
# -------------------------

try:
    json.loads("{invalid}")
except json.JSONDecodeError:
    print("Invalid JSON")

# -------------------------
# Python to JSON Types
# -------------------------

sample = {
    "name": "John",
    "active": True,
    "marks": None,
    "scores": [10, 20, 30]
}

print(json.dumps(sample, indent=4))