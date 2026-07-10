# Creating dictionaries

student = {
   "name" : "ali",
   "age"  : 21,
   "dearement" : "SE"
}
print(student)

# Accessing values
print(student["name"])
print(student["age"])
print(student["dearement"])

print(student.get("name"))

# Adding new item
student["city"] = "Lahore"

# Updating
student["age"] = 22

# Looping
for key in student:
    print(key)

for value in student.values():
    print(value)

for key,value in student.items():
    print(key,value)

# Copy 
copy_student = student.copy()

# Nested dictionary
students = {
    "s1": {
        "name": "Ali",
        "cgpa": 3.8
    },
    "s2": {
        "name": "Sara",
        "cgpa": 3.9
    }
}
print(student["s1"]["name"])

# Dictionary comprehension
squares = {x : x*x for x in range(1,6)}
print(squares)

# Removing
student.pop("age")
student.popitem() # remove last item
del student["name"]
student.clear()



