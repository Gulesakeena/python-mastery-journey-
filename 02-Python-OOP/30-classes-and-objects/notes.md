# 30 - Classes and Objects

# What is a Class?

A class is a blueprint used to create objects.

Think of it like a house blueprint.

The blueprint is not the actual house.

It only defines how a house should look.

Example

```
Student
```

The Student class may contain

Attributes

- Name
- Roll Number
- Department

Methods

- Study()
- Sleep()
- Attend_Class()

---

# What is an Object?

An object is an instance of a class.

Example

Class

```
Student
```

Objects

```
Ali
Ahmed
Sara
```

Each student has different data but follows the same blueprint.

---

# Creating a Class

Syntax

```python
class Student:
    pass
```

`pass` means the class is empty.

---

# Creating an Object

```python
student1 = Student()
```

Now `student1` is an object.

---

# Multiple Objects

```python
student1 = Student()
student2 = Student()
student3 = Student()
```

Each object is independent.

---

# Adding Attributes

Python allows adding attributes dynamically.

```python
student1.name = "Ali"
student1.age = 22
```

---

# Accessing Attributes

```python
print(student1.name)
```

---

# Object Identity

Each object has its own memory location.

```python
print(id(student1))
print(id(student2))
```

IDs will be different.

---

# Built-in Functions

```python
type(student1)
```

Returns

```
<class '__main__.Student'>
```

```python
isinstance(student1, Student)
```

Returns

```
True
```

---

# Real-World Example

Car Class

Objects

Toyota

Honda

BMW

Each has different

- Color
- Speed
- Model

But all are Cars.

---

# Why Create Multiple Objects?

Instead of writing

```
student1_name
student2_name
student3_name
```

We create multiple Student objects.

Cleaner

Scalable

Maintainable

---

# Common Beginner Mistakes

❌ Forgetting ()

```python
student = Student
```

Correct

```python
student = Student()
```

---

❌ Using an attribute before assigning it

```python
print(student.name)
```

Raises

```
AttributeError
```

---

# Interview Notes

Class

Blueprint

Object

Instance of a class

One class

↓

Many objects

---

# Key Takeaways

✔ Classes define structure.

✔ Objects store actual data.

✔ One class can create many objects.

✔ Every object has its own identity.