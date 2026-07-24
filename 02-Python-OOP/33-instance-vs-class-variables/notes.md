# 33 - Instance Variables vs Class Variables

# What is an Instance Variable?

An instance variable belongs to **one specific object**.

Each object has its own copy.

Example

```python
class Student:

    def __init__(self, name):
        self.name = name
```

Creating objects

```python
s1 = Student("Ali")

s2 = Student("Sara")
```

Output

```
s1.name → Ali

s2.name → Sara
```

Changing one object does NOT affect another.

---

# What is a Class Variable?

A class variable belongs to the **class itself**, not to individual objects.

It is shared by every object.

Example

```python
class Student:

    school = "University of Gujrat"
```

Every student automatically shares the same school.

---

# Example

```python
class Student:

    school = "UOG"

    def __init__(self,name):
        self.name = name
```

Objects

```python
s1 = Student("Ali")

s2 = Student("Sara")
```

Output

```
s1.school

UOG

s2.school

UOG
```

---

# Changing an Instance Variable

```python
s1.name = "Ahmed"
```

Only `s1` changes.

---

# Changing a Class Variable

```python
Student.school = "FAST"
```

Every object now sees

```
FAST
```

unless an instance overrides it.

---

# Accessing Variables

Instance Variable

```python
student.name
```

Class Variable

```python
Student.school
```

or

```python
student.school
```

---

# Instance vs Class Variables

| Instance Variable | Class Variable |
|-------------------|----------------|
| Belongs to object | Belongs to class |
| Different for every object | Shared by all objects |
| Created using `self` | Created inside class |
| Stored separately | Stored once |

---

# Memory Representation

```
Student Class

school = UOG

        ▲
        │
 -------------------------
 |         |            |
s1        s2           s3

name      name         name

Ali       Sara         Ahmed
```

Only one copy of `school`.

---

# Common Mistakes

❌ Putting unique data into class variables.

Wrong

```python
class Student:

    name = ""
```

Every object shares the same name.

Correct

```python
self.name
```

---

❌ Modifying a class variable using an object.

```python
student.school = "FAST"
```

This creates a **new instance variable** instead of modifying the shared class variable.

Correct

```python
Student.school = "FAST"
```

---

# When to Use Class Variables

Use for data shared by all objects.

Examples

- Company Name
- University Name
- Tax Rate
- Country
- Currency
- PI value

---

# When to Use Instance Variables

Use for object-specific data.

Examples

- Name
- Age
- Salary
- Marks
- Balance

---

# Best Practices

✔ Shared data → Class Variable

✔ Object-specific data → Instance Variable

✔ Modify shared values using the class name.

---

# Interview Notes

Instance Variable

Unique

Uses `self`

Stored in object

Class Variable

Shared

Stored in class

One copy

---

# Key Takeaways

✔ Every object has its own instance variables.

✔ Every class has one shared copy of class variables.

✔ Use instance variables for unique data.

✔ Use class variables for shared data.