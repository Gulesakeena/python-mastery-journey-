'''Student Management System (Functions Version)

Menu

1 Add Student

2 Search Student

3 Update Student

4 Delete Student

5 Display Students

6 Exit'''
student = []


def Add_Student(name):
    student.append(name)
    return "Student Added Successfully"


def Search_Student(name):
    for stu in student:
        if stu == name:
            return "Student Found"

    return "Student Not Found"


def Update_Student(old_name, new_name):
    for i in range(len(student)):
        if student[i] == old_name:
            student[i] = new_name
            return "Student Updated Successfully"

    return "Student Not Found"


def Delete_Student(name):
    for stu in student:
        if stu == name:
            student.remove(stu)
            return "Student Deleted Successfully"

    return "Student Not Found"


def Display_Students():
    return student


while True:

    print("""
1 Add Student
2 Search Student
3 Update Student
4 Delete Student
5 Display Students
6 Exit
""")

    choice = int(input("Enter Choice: "))

    if choice == 1:

        name = input("Enter Student Name: ")
        print(Add_Student(name))

    elif choice == 2:

        name = input("Enter Student Name: ")
        print(Search_Student(name))

    elif choice == 3:

        old_name = input("Enter Old Name: ")
        new_name = input("Enter New Name: ")

        print(Update_Student(old_name, new_name))

    elif choice == 4:

        name = input("Enter Student Name: ")
        print(Delete_Student(name))

    elif choice == 5:

        print(Display_Students())

    elif choice == 6:

        print("Program Ended")
        break

    else:

        print("Invalid Choice")