"""
Student Record Manager using JSON
"""

import json

students = []

while True:
    print("\n===== Student Record Manager =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Save")
    print("4. Load")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        age = int(input("Age: "))
        course = input("Course: ")

        students.append({
            "name": name,
            "age": age,
            "course": course
        })

    elif choice == "2":
        print(json.dumps(students, indent=4))

    elif choice == "3":
        with open("students.json", "w") as file:
            json.dump(students, file, indent=4)

        print("Saved Successfully!")

    elif choice == "4":
        try:
            with open("students.json") as file:
                students = json.load(file)

            print("Loaded Successfully!")

        except FileNotFoundError:
            print("No file found.")

    elif choice == "5":
        break

    else:
        print("Invalid Choice")