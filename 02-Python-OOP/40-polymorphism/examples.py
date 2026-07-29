"""
40 - Polymorphism
"""

# -----------------------------
# Example 1 - Basic Polymorphism
# -----------------------------

class Dog:
    def sound(self):
        print("Dog: Bark")


class Cat:
    def sound(self):
        print("Cat: Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()


# -----------------------------
# Example 2 - Method Overriding
# -----------------------------

class Animal:
    def move(self):
        print("Animal moves")


class Bird(Animal):
    def move(self):
        print("Bird flies")


class Fish(Animal):
    def move(self):
        print("Fish swims")


for obj in [Bird(), Fish()]:
    obj.move()


# -----------------------------
# Example 3 - Duck Typing
# -----------------------------

class Airplane:
    def fly(self):
        print("Airplane is flying")


class Drone:
    def fly(self):
        print("Drone is flying")


def start_flight(obj):
    obj.fly()


start_flight(Airplane())
start_flight(Drone())


# -----------------------------
# Example 4 - Built-in Polymorphism
# -----------------------------

print(len("Python"))
print(len([1, 2, 3, 4]))
print(len({"a": 1, "b": 2}))


# -----------------------------
# Example 5 - Operator Overloading
# -----------------------------

print(10 + 20)
print("Hello " + "World")
print([1, 2] + [3, 4])