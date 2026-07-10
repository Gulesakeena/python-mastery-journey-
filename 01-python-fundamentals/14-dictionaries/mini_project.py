'''Student Management System (Dictionary Version)

Each student:

{
    "id":101,
    "name":"Ali",
    "department":"CS",
    "cgpa":3.8
}

Store students in a list.

Menu

1 Add Student

2 Search Student

3 Update Student

4 Delete Student

5 Display Students

6 Exit'''

'''Student Management System (Dictionary Version)

Each student:

{
    "id":101,
    "name":"Ali",
    "department":"CS",
    "cgpa":3.8
}

Store students in a list.
'''

students = []

print("""
======== Student Management System ========

1. Add Student
2. Search Student
3. Update Student
4. Delete Student
5. Display Students
6. Exit

===========================================
""")

while True:
    option = int(input("Enter your choice: "))

    # ---------------- Add Student ----------------
    if option == 1:
        student_id = int(input("Enter Student ID: "))
        name = input("Enter Name: ")
        department = input("Enter Department: ")
        cgpa = float(input("Enter CGPA: "))

        student = {
            "id": student_id,
            "name": name,
            "department": department,
            "cgpa": cgpa
        }

        students.append(student)
        print("Student added successfully!")

    # ---------------- Search Student ----------------
    elif option == 2:
        student_id = int(input("Enter Student ID to search: "))

        found = False

        for student in students:
            if student["id"] == student_id:
                print("Student Found!")
                print(student)
                found = True
                break

        if not found:
            print("Student not found.")

    # ---------------- Update Student ----------------
    elif option == 3:
        student_id = int(input("Enter Student ID to update: "))

        found = False

        for student in students:
            if student["id"] == student_id:

                student["name"] = input("Enter New Name: ")
                student["department"] = input("Enter New Department: ")
                student["cgpa"] = float(input("Enter New CGPA: "))

                print("Student updated successfully!")
                found = True
                break

        if not found:
            print("Student not found.")

    # ---------------- Delete Student ----------------
    elif option == 4:
        student_id = int(input("Enter Student ID to delete: "))

        found = False

        for student in students:
            if student["id"] == student_id:
                students.remove(student)
                print("Student deleted successfully!")
                found = True
                break

        if not found:
            print("Student not found.")

    # ---------------- Display Students ----------------
    elif option == 5:

        if len(students) == 0:
            print("No students available.")

        else:
            print("\n------ Student Records ------")

            for student in students:
                print(f"ID         : {student['id']}")
                print(f"Name       : {student['name']}")
                print(f"Department : {student['department']}")
                print(f"CGPA       : {student['cgpa']}")
                print("-----------------------------")

    # ---------------- Exit ----------------
    elif option == 6:
        print("Thank you!")
        break

    else:
        print("Invalid choice.")