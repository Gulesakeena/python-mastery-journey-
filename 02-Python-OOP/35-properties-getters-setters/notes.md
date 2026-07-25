# 35 - Properties, Getters & Setters

## Objective

Learn how to protect object data using **Getters**, **Setters**, and Python's **@property** decorator.

---

# Real-Life Problem

Suppose we have a `Student` class.

```python
class Student:

    def __init__(self, age):
        self.age = age
```

Now create an object.

```python
student = Student(20)
```

Everything looks fine.

Current data:

```
Age = 20
```

But anyone can change the value.

```python
student.age = -10
```

Now

```
Age = -10
```

This is **invalid data** because a person's age cannot be negative.

So the question is:

**How can we stop users from storing invalid values?**

Answer:

- Validation
- Getters
- Setters

---

# What is a Getter?

A **Getter** is a method used to **read (get)** the value of an attribute.

Example

```python
class Student:

    def __init__(self, age):
        self._age = age

    def get_age(self):
        return self._age
```

Usage

```python
student = Student(20)

print(student.get_age())
```

Output

```
20
```

### Flow

```
student.get_age()

        │

        ▼

Returns _age

        │

        ▼

20
```

Getter only **returns** data.

It never changes it.

---

# What is a Setter?

A **Setter** is a method used to **change (set)** the value of an attribute.

Before storing the value, it can perform validation.

Example

```python
class Student:

    def __init__(self, age):
        self._age = age

    def set_age(self, age):

        if age >= 0:
            self._age = age
        else:
            print("Invalid Age")
```

Usage

```python
student = Student(20)

student.set_age(25)

print(student.get_age())
```

Output

```
25
```

Now

```python
student.set_age(-10)
```

Output

```
Invalid Age
```

The age is **not updated**.

---

# Why Do We Use _age Instead of age?

Notice this variable.

```python
self._age
```

Why not

```python
self.age
```

The underscore (`_`) is a **Python naming convention**.

It tells other developers:

```
This is an internal variable.

Don't modify it directly.
```

It is **not private**.

It is only a convention.

---

# Traditional Getters & Setters

Many programming languages use methods like this.

```python
student.set_age(25)

print(student.get_age())
```

This works.

But Python has a cleaner way.

---

# Pythonic Way → @property

Python provides a decorator called

```python
@property
```

It allows methods to behave like normal variables.

Instead of

```python
student.get_age()
```

we simply write

```python
student.age
```

Even though a method is being called behind the scenes.

---

# Creating a Property (Getter)

```python
class Student:

    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age
```

Usage

```python
student = Student(20)

print(student.age)
```

Output

```
20
```

Notice

There are **no parentheses**.

We wrote

```python
student.age
```

instead of

```python
student.get_age()
```

Python automatically calls the getter.

---

# How @property Works

When you write

```python
print(student.age)
```

Python actually does this internally

```
student.age

      │

      ▼

@property

      │

      ▼

Getter Method

      │

      ▼

Returns _age
```

---

# Property Setter

Now we also want validation while changing the value.

```python
class Student:

    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):

        if value < 0:
            raise ValueError("Age cannot be negative")

        self._age = value
```

Usage

```python
student = Student(20)

student.age = 25

print(student.age)
```

Output

```
25
```

---

# What Happens Internally?

When we write

```python
student.age = 25
```

Python automatically calls

```python
age.setter
```

Flow

```
student.age = 25

        │

        ▼

Setter Method

        │

        ▼

Validation

        │

        ▼

_age = 25
```

If we write

```python
student.age = -10
```

Flow

```
student.age = -10

        │

        ▼

Setter

        │

        ▼

Validation Failed

        │

        ▼

ValueError
```

The invalid value is never stored.

---

# Read-Only Property

Sometimes we want users to **read** a value but never change it.

Example

```python
class Student:

    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age
```

Now

```python
print(student.age)
```

works.

But

```python
student.age = 30
```

raises

```
AttributeError
```

Because there is **no setter**.

---

# Common Validation Example

```python
class Employee:

    def __init__(self, salary):
        self.salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):

        if value < 0:
            raise ValueError("Salary cannot be negative")

        self._salary = value
```

Now

```python
emp = Employee(50000)

emp.salary = -100
```

Output

```
ValueError
```

---

# Why Not Access _age Directly?

Technically, this is still possible.

```python
student._age = -100
```

Python allows it.

But developers understand that variables beginning with `_`

```
_age
_salary
_marks
```

are **internal**.

They should normally not be modified directly.

---

# Common Mistake

Wrong

```python
@age.setter
def age(self, value):

    self.age = value
```

Why is it wrong?

Because

```
self.age

↓

Calls Setter Again

↓

Calls Setter Again

↓

Calls Setter Again

↓

Infinite Loop

↓

RecursionError
```

Correct

```python
@age.setter
def age(self, value):

    self._age = value
```

Always store data in the internal variable.

---

# Advantages of Properties

- Validation before storing data
- Cleaner syntax
- Easier to maintain
- Better code readability
- Hides implementation details
- Pythonic approach
- Allows read-only attributes

---

# Traditional vs Pythonic

Traditional

```python
student.set_age(20)

print(student.get_age())
```

Pythonic

```python
student.age = 20

print(student.age)
```

Both perform the same work.

The second version is cleaner.

---

# Interview Questions

## What is a Getter?

A method used to read an attribute.

---

## What is a Setter?

A method used to modify an attribute after validation.

---

## Why use @property?

It allows methods to behave like normal attributes.

---

## Why do we use _age?

It is an internal variable used to avoid recursion and indicate that it should not be modified directly.

---

## What happens if a property has only a getter?

The attribute becomes **read-only**.

---

## What happens if we write self.age inside the setter?

The setter calls itself repeatedly, causing an infinite recursion and eventually a `RecursionError`.

---

# Summary

- **Getter** → Reads data.
- **Setter** → Validates and updates data.
- **@property** → Makes methods behave like attributes.
- **@property + @setter** → Provides safe and controlled access to object data.
- Store values in **_variable**, not in the property itself.
- Use properties whenever you need validation or controlled access to class attributes.