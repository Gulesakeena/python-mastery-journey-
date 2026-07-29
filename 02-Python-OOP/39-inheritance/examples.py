"""
39 - Inheritance
"""

# -----------------------------
# Example 1 - Basic Inheritance
# -----------------------------

class Animal:
    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    pass


dog = Dog()
dog.speak()


# -----------------------------
# Example 2 - Child Method
# -----------------------------

class Vehicle:
    def start(self):
        print("Vehicle started")


class Car(Vehicle):
    def drive(self):
        print("Car is driving")


car = Car()
car.start()
car.drive()


# -----------------------------
# Example 3 - super()
# -----------------------------

class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

    def display(self):
        print(self.name, self.roll)


student = Student("Ali", 101)
student.display()


# -----------------------------
# Example 4 - Method Overriding
# -----------------------------

class Bird:
    def sound(self):
        print("Bird sound")


class Sparrow(Bird):
    def sound(self):
        print("Chirp Chirp")


sparrow = Sparrow()
sparrow.sound()


# -----------------------------
# Example 5 - MRO
# -----------------------------

class A:
    pass


class B(A):
    pass


print(B.mro())

# 1. Single Inheritance

class Animal:

    def speak(self):
        print("Animal speaks")


class Dog(Animal):

    def bark(self):
        print("Dog barks")


dog = Dog()

dog.speak()
dog.bark()

# 2. Multiple Inheritance


class Father:

    def skills(self):
        print("Programming")


class Mother:

    def talent(self):
        print("Cooking")


class Child(Father, Mother):

    def hobby(self):
        print("Gaming")


child = Child()

child.skills()
child.talent()
child.hobby()


# 3. Multilevel Inheritance


class GrandFather:

    def house(self):
        print("Grandfather's House")


class Father(GrandFather):

    def car(self):
        print("Father's Car")


class Son(Father):

    def bike(self):
        print("Son's Bike")


son = Son()

son.house()
son.car()
son.bike()


# 4. Hierarchical Inheritance


class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):

    def bark(self):
        print("Dog barks")


class Cat(Animal):

    def meow(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.eat()
dog.bark()

cat.eat()
cat.meow()


# 5. Hybrid Inheritance


class A:

    def show_a(self):
        print("Class A")


class B(A):

    def show_b(self):
        print("Class B")


class C(A):

    def show_c(self):
        print("Class C")


class D(B, C):

    def show_d(self):
        print("Class D")


obj = D()

obj.show_a()
obj.show_b()
obj.show_c()
obj.show_d()

print(D.mro())
