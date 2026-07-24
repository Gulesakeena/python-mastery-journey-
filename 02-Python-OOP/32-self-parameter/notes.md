# 32 - self Parameter

# What is self?

`self` is a reference to the **current object (instance)** of a class.

It allows an object to access its own data and methods.

---

# Why do we need self?

Suppose we create two students.

```python
student1 = Student("Ali",22)

student2 = Student("Sara",21)
```

Both objects use the same class.

How does Python know which object's data to use?

The answer is **self**.

---

# Example

```python
class Student:

    def __init__(self,name):

        self.name = name
```

When we write

```python
student = Student("Ali")
```

Python internally does

```python
Student.__init__(student,"Ali")
```

Notice that Python automatically sends the object as the first argument.

---

# self is NOT a Keyword

Many beginners think `self` is a keyword.

It is **not**.

You could technically write

```python
def __init__(abc,name):
```

But according to Python conventions (PEP 8), always use `self`.

---

# Accessing Attributes

```python
self.name = name
```

`self.name`

means

"The name variable belonging to this object."

---

# Accessing Methods

```python
class Student:

    def study(self):

        print("Studying...")
```

Calling

```python
student.study()
```

Internally becomes

```python
Student.study(student)
```

---

# Multiple Objects

```python
student1 = Student("Ali")

student2 = Student("Sara")
```

Each object has its own `self`.

```
self → student1

self → student2
```

---

# Common Mistakes

❌ Missing self

```python
def display():
```

Correct

```python
def display(self):
```

---

❌ Forgetting self while accessing variables

Wrong

```python
print(name)
```

Correct

```python
print(self.name)
```

---

# Why not use Global Variables?

Global variables are shared by everyone.

Instance variables belong only to one object.

That's why OOP uses `self`.

---

# Interview Notes

self

Current object

Automatically passed

Not a keyword

Used in every instance method

---

# Key Takeaways

✔ `self` refers to the current object.

✔ Python passes it automatically.

✔ Use `self` to access attributes.

✔ Use `self` to call methods.

✔ `self` is a convention, not a keyword.