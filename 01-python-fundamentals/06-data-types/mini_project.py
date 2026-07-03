'''
Student Management System (Version 1)

Create a program that stores multiple students using dictionaries inside a list.

'''

students = [
    {
        "id": 1,
        "name": "Ali",
        "age": 22,
        "cgpa": 3.8,
        "skills": ["Python", "Git"]
    },
    {
        "id": 2,
        "name": "Sara",
        "age": 21,
        "cgpa": 3.9,
        "skills": ["SQL", "Pandas"]
    }
]

# Print all students.
print(students[0])
print(students[1])

# Print only names.
print(students[0]['name'])
print(students[1]['name'])

#Print the student with the highest CGPA.
if students[0]['cgpa'] > students[1]['cgpa'] :
    print(students[0]["name"]," has highest cgpa")
else :
    print(students[1]["name"]," has highest cgpa")

#Print students who know Python.
if 'Python' in students[0]["skills"]:
    print(students[0]["name"]," knows the python")
elif 'Python' in students[1]["skills"]:
    print(students[1]["name"]," knows the python")
else: 
    print("No student knows python")

#Count total students.
total_students = len(students)

print("Total Students:", total_students)

#Print average CGPA.
average_cgpa = sum(student["cgpa"] for student in students) / len(students)

print("Average CGPA:", average_cgpa)