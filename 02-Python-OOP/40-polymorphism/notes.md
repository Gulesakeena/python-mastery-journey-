# 40 - Polymorphism

# What is Polymorphism?

The word **Polymorphism** comes from two Greek words:

- Poly = Many
- Morph = Forms

Meaning:

> **One interface, many forms.**

The same method name can perform different actions depending on the object.

---

# Real-Life Example

Think about a remote control.

```
Remote.pressPower()

TV → Turns on TV

AC → Turns on AC

Projector → Turns on Projector
```

The same button performs different actions.

---

# Example

```python
class Dog:
    def sound(self):
        print("Bark")


class Cat:
    def sound(self):
        print("Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
```

Output

```
Bark
Meow
```

---

# Method Overriding

Method overriding is the most common form of polymorphism.

```python
class Animal:

    def sound(self):
        print("Animal")


class Dog(Animal):

    def sound(self):
        print("Bark")
```

---

# Runtime Polymorphism

Python decides which method to call at runtime.

```python
animal.sound()
```

The object's type determines which method executes.

---

# Duck Typing

Python follows Duck Typing.

"If it walks like a duck and quacks like a duck, treat it like a duck."

Python checks behavior instead of class type.

```python
class Bird:

    def fly(self):
        print("Flying")


class Airplane:

    def fly(self):
        print("Flying Fast")


def start(obj):
    obj.fly()
```

Both objects work.

---

# Built-in Polymorphism

Many built-in functions are polymorphic.

Example

```python
len("Python")

len([1,2,3])

len({"A":1})
```

Same function.

Different object.

---

# Operator Overloading

Operators work differently for different data types.

```python
5 + 3

"Hello" + "World"

[1] + [2]
```

The same operator (+) behaves differently.

---

# Advantages

✔ Reusable code

✔ Flexible design

✔ Easy maintenance

✔ Less coupling

✔ Cleaner architecture

---

# Polymorphism vs Inheritance

Inheritance creates relationships.

Polymorphism changes behavior.

Inheritance often enables polymorphism.

---

# Best Practices

- Prefer polymorphism over many if-else statements.
- Design methods with the same interface.
- Use duck typing when appropriate.

---

# Key Takeaways

- One interface can have many implementations.
- Python supports runtime polymorphism.
- Duck typing is a core Python feature.
- Operator overloading is built-in polymorphism.