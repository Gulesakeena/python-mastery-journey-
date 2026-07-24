# 31 - Constructors (__init__)

# What is a Constructor?

A constructor is a special method that runs automatically whenever an object is created.

In Python, the constructor is:

```python
__init__()
```

You do **not** call it yourself. Python calls it automatically.

---

# Why do we need Constructors?

Without constructors:

```python
student = Student()

student.name = "Ali"
student.age = 22
student.department = "SE"
```

We manually assign values after creating the object.

With constructors:

```python
student = Student("Ali",22,"SE")
```

Cleaner.

Shorter.

Professional.

---

# Syntax

```python
class Student:

    def __init__(self):
        print("Constructor Called")
```

Creating an object

```python
student = Student()
```

Output

```
Constructor Called
```

---

# Constructor with Parameters

```python
class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age
```

Object

```python
student = Student("Ali",22)
```

---

# What is self?

`self` represents the current object.

Whenever an object calls a method,

Python automatically passes that object as the first argument.

Example

```python
student1 = Student()
```

Internally

```
Student.__init__(student1)
```

---

# Assigning Attributes

```python
self.name = name
```

Left side

Object Variable

Right side

Constructor Parameter

---

# Multiple Objects

```python
student1 = Student("Ali",22)

student2 = Student("Sara",21)

student3 = Student("Ahmed",23)
```

Every object stores different values.

---

# Default Parameters

```python
class Student:

    def __init__(self,name,department="Software Engineering"):
        self.name = name
        self.department = department
```

Now

```python
Student("Ali")
```

works perfectly.

---

# Accessing Attributes

```python
print(student.name)

print(student.age)
```

---

# Common Mistakes

❌ Forgetting self

```python
def __init__(name):
```

Correct

```python
def __init__(self,name):
```

---

❌ Forgetting self while assigning

Wrong

```python
name = name
```

Correct

```python
self.name = name
```

---

❌ Wrong number of arguments

```python
Student()
```

Raises

```
TypeError
```

because constructor expects arguments.

---

# Constructor vs Normal Method

Constructor

- Runs automatically
- Used for initialization

Normal Method

- Called manually
- Performs specific tasks

---

# Best Practices

✔ Keep constructors simple.

✔ Initialize object attributes.

✔ Avoid unnecessary logic.

✔ Use meaningful parameter names.

---

# Interview Notes

Constructor

Special method

Runs automatically

Name

```
__init__
```

Purpose

Initialize object data

---

# Key Takeaways

✔ Constructors initialize objects.

✔ `__init__()` runs automatically.

✔ `self` refers to the current object.

✔ Constructors make code cleaner and reusable.