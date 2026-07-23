"""
30 - Classes and Objects
"""

# -----------------------------------
# Example 1
# -----------------------------------

class Student:
    pass

student1 = Student()
print(type(student1))

# -----------------------------------
# Example 2
# -----------------------------------

student1.name = "Ali"
student1.age = 21

print(student1.name)
print(student1.age)

# -----------------------------------
# Example 3
# -----------------------------------

student2 = Student()
student2.name = "Gul"
student2.age = 21

print(student2.name)
print(student2.age)

# -----------------------------------
# Example 4
# -----------------------------------

print(id(student1))
print(id(student2))

# -----------------------------------
# Example 5
# -----------------------------------

print(isinstance(student1,student2))


# -----------------------------------
# Example 6
# -----------------------------------

class Car:
    pass

car1 = Car()
car2 = Car()

car1.brand="Honda"
car2.brand="Civic"

print(car1.brand)
print(car2.brand)