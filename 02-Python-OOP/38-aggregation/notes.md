````markdown
# 38 - Aggregation (Has-A Relationship)

# Learning Objectives

After completing this topic, you should be able to:

- Understand what Aggregation is.
- Know why Aggregation is needed.
- Identify a Has-A relationship.
- Differentiate Aggregation from Inheritance.
- Implement Aggregation in Python.
- Understand real-world use cases.

---

# Before Learning Aggregation

Remember:

OOP has relationships between classes.

The two most common relationships are:

1. **Inheritance**
2. **Aggregation**

Many beginners confuse them.

The easiest way to identify them is:

- **Inheritance → IS-A Relationship**
- **Aggregation → HAS-A Relationship**

Examples

```
Car IS A Vehicle      → Inheritance

Car HAS A Engine      → Aggregation
```

---

# What is Aggregation?

Aggregation means:

> One object **contains** or **uses** another object.

In simple words,

One class **has** another class as one of its attributes.

This is called a **Has-A Relationship**.

---

# Why Do We Need Aggregation?

Imagine you are creating a Car class.

A car has

- Engine
- Wheels
- Battery
- Seats

Should we write all Engine code inside the Car class?

❌ No.

That would make the Car class huge and difficult to manage.

Instead,

Create a separate Engine class.

Then give the Car class an Engine object.

This is Aggregation.

---

# Problem Without Aggregation

Without Aggregation

```python
class Car:

    def start(self):
        print("Engine Started")

    def stop(self):
        print("Engine Stopped")

    def engine_temperature(self):
        print("90°C")

    def engine_power(self):
        print("150 HP")
```

Problems

- Car becomes too large.
- Hard to maintain.
- Hard to reuse Engine.
- Duplicate code.

---

# Solution Using Aggregation

Create separate classes.

```python
class Engine:

    def start(self):
        print("Engine Started")
```

Now use it.

```python
class Car:

    def __init__(self):
        self.engine = Engine()
```

Now

Car HAS an Engine.

---

# First Example

```python
class Engine:

    def start(self):
        print("Engine Started")


class Car:

    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        self.engine.start()


car = Car()

car.start_car()
```

Output

```
Engine Started
```

---

# Memory Diagram

```
Car Object

engine
   │
   ▼
Engine Object
```

Car object contains an Engine object.

---

# Another Example

Person has a Laptop.

```python
class Laptop:

    def turn_on(self):
        print("Laptop On")


class Person:

    def __init__(self):

        self.laptop = Laptop()

    def work(self):

        self.laptop.turn_on()


person = Person()

person.work()
```

Output

```
Laptop On
```

Relationship

```
Person HAS A Laptop
```

---

# University Example

```python
class Department:

    def __init__(self, name):
        self.name = name


class University:

    def __init__(self):

        self.department = Department("Software Engineering")
```

Relationship

```
University HAS A Department
```

---

# Teacher Example

```python
class Book:

    def read(self):
        print("Reading Book")


class Teacher:

    def __init__(self):

        self.book = Book()

    def teach(self):

        self.book.read()


teacher = Teacher()

teacher.teach()
```

---

# Real-Life Examples

| Object | Has A |
|---------|--------|
| Car | Engine |
| Student | Laptop |
| Teacher | Book |
| House | Rooms |
| Mobile | Battery |
| Computer | Keyboard |
| Company | Employees |
| School | Classrooms |
| Hospital | Doctors |
| Restaurant | Menu |

---

# Aggregation with Constructor Injection

Instead of creating the object inside the class,

we can pass it from outside.

Example

```python
class Engine:

    def start(self):
        print("Engine Started")


class Car:

    def __init__(self, engine):

        self.engine = engine

    def start(self):

        self.engine.start()


engine = Engine()

car = Car(engine)

car.start()
```

Why is this better?

- More flexible.
- Easier testing.
- Reusable objects.
- Better design.

---

# Why is Aggregation Important?

Without Aggregation

```
One giant class
```

With Aggregation

```
Small reusable classes
```

Benefits

- Reusability
- Clean Code
- Easy Maintenance
- Better Design
- Low Code Duplication

---

# Aggregation vs Inheritance

| Aggregation | Inheritance |
|-------------|-------------|
| HAS-A Relationship | IS-A Relationship |
| Uses another object | Extends another class |
| Code Reuse | Code Reuse |
| Flexible | Less Flexible |
| Objects are independent | Child depends on Parent |

Example

```
Car HAS A Engine
```

Aggregation

```
Car IS A Vehicle
```

Inheritance

---

# Common Mistakes

❌ Thinking every relationship is Inheritance.

Wrong

```
Car IS A Engine
```

Correct

```
Car HAS A Engine
```

---

❌ Writing everything inside one class.

Wrong

```python
class Car:
    # Engine code
    # Wheel code
    # Battery code
```

Correct

Separate classes.

---

# Best Practices

✔ Use Aggregation when one object **uses** another object.

✔ Keep classes small.

✔ Create reusable classes.

✔ Prefer Aggregation over making one huge class.

✔ If the relationship is HAS-A, think Aggregation first.

---

# Interview Questions

## Q1. What is Aggregation?

Aggregation is a **Has-A relationship** where one class contains or uses another class.

---

## Q2. Why do we use Aggregation?

- Code Reusability
- Easy Maintenance
- Better Design
- Low Coupling

---

## Q3. Give a real-life example.

```
Car HAS A Engine

Student HAS A Laptop

House HAS A Room
```

---

## Q4. Difference between Aggregation and Inheritance?

Aggregation

```
HAS-A
```

Inheritance

```
IS-A
```

---

# Key Takeaways

✔ Aggregation means one class **has** another class.

✔ It represents a **Has-A Relationship**.

✔ It helps break large classes into smaller reusable classes.

✔ Aggregation improves code organization and maintainability.

✔ Examples:

- Car HAS A Engine
- Student HAS A Laptop
- Teacher HAS A Book
- Computer HAS A Keyboard

✔ If the relationship is **HAS-A**, Aggregation is usually the right choice.
````
