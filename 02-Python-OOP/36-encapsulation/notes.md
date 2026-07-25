# 36 - Encapsulation

## Objective

Learn what **Encapsulation** is, why it is used, and how Python controls access to data using **Public**, **Protected**, and **Private** members.

---

# What is Encapsulation?

**Encapsulation** means:

> Keeping **data (variables)** and **methods (functions)** together inside a class and controlling how that data is accessed or modified.

Simple definition:

```
Data + Methods + Access Control = Encapsulation
```

Think of it like a **capsule**.

A medicine capsule keeps everything safely inside.

Similarly, a class keeps its data and methods together and protects important data.

---

# Why Do We Need Encapsulation?

Imagine a Bank Account.

Without encapsulation:

```python
class Bank:

    def __init__(self):
        self.balance = 10000
```

Anyone can do this:

```python
account = Bank()

account.balance = -5000
```

Now the balance becomes

```
-5000
```

This is invalid.

We don't want users to directly change important data.

So we use **Encapsulation**.

---

# Benefits of Encapsulation

- Protects data
- Prevents invalid values
- Makes code easier to maintain
- Improves security
- Makes programs easier to understand

---

# Types of Members in Python

Python has **three levels of access**.

```
Public

Protected

Private
```

---

# 1. Public Members

A normal variable without any underscore.

Example

```python
class Student:

    def __init__(self):
        self.name = "Ali"
```

Access

```python
student = Student()

print(student.name)
```

Output

```
Ali
```

Modify

```python
student.name = "Ahmed"
```

Allowed.

### Flow

```
Object

↓

name

↓

Anyone can Read

Anyone can Modify
```

Public members have **no restrictions**.

---

# 2. Protected Members

Protected variables start with **one underscore**.

Example

```python
class Employee:

    def __init__(self):
        self._salary = 50000
```

Access

```python
employee = Employee()

print(employee._salary)
```

Output

```
50000
```

Notice

Python **does not stop you** from accessing `_salary`.

So why use `_`?

Because it tells other programmers:

```
This variable is for internal use.

Please don't modify it directly.
```

It is **only a convention**, not real protection.

### Flow

```
_salary

↓

Accessible

↓

But developers should avoid using it directly.
```

---

# 3. Private Members

Private variables start with **two underscores**.

Example

```python
class User:

    def __init__(self):
        self.__password = "abc123"
```

Now try

```python
user = User()

print(user.__password)
```

Output

```
AttributeError
```

Why?

Because Python changes the variable name internally.

This is called **Name Mangling**.

---

# What is Name Mangling?

Suppose you write

```python
self.__password
```

Python secretly changes it to

```python
self._User__password
```

where `User` is the class name.

So internally it becomes

```
_User__password
```

That's why

```python
user.__password
```

fails.

But this works

```python
print(user._User__password)
```

Output

```
abc123
```

Although it works, **you should never access private variables this way in normal code.**

---

# Why Does Python Use Name Mangling?

Name mangling is used to

- Prevent accidental access
- Prevent accidental modification
- Avoid variable name conflicts in inheritance

It is **not true security**.

It simply discourages direct access.

---

# Public vs Protected vs Private

Imagine a house.

### Public

```
Living Room

Everyone can enter.
```

### Protected

```
Kitchen

Family members use it.

Guests normally don't.
```

### Private

```
Personal Bedroom

No one should enter without permission.
```

---

# Encapsulation with Getters and Setters

Suppose we have

```python
class Student:

    def __init__(self, age):
        self.__age = age
```

Age is private.

We cannot access

```python
student.__age
```

Instead we provide controlled access.

Getter

```python
@property
def age(self):
    return self.__age
```

Setter

```python
@age.setter
def age(self, value):

    if value < 0:
        raise ValueError("Invalid Age")

    self.__age = value
```

Usage

```python
student = Student(20)

print(student.age)

student.age = 25
```

Notice

The user never touches

```python
__age
```

They only use

```python
student.age
```

The getter and setter do the work behind the scenes.

---

# Internal Workflow

Reading

```
student.age

↓

Getter

↓

Returns __age
```

Writing

```
student.age = 25

↓

Setter

↓

Validation

↓

__age = 25
```

---

# Why Use Private Variables with Properties?

Suppose you write

```python
student.age = -10
```

Without a setter

```
Age becomes -10
```

Wrong.

With a setter

```
Setter

↓

Checks Value

↓

Rejects Invalid Data
```

This keeps the object safe.

---

# Common Mistakes

## Mistake 1

Thinking

```python
_variable
```

is private.

Wrong.

It is only a naming convention.

---

## Mistake 2

Thinking

```python
__variable
```

cannot be accessed.

Wrong.

It can still be accessed using

```python
_ClassName__variable
```

But it should not be.

---

## Mistake 3

Accessing private variables directly

Wrong

```python
student._Student__age = -5
```

Correct

```python
student.age = 25
```

Always use properties.

---

# Best Practices

- Use **public** variables for information everyone can access.
- Use **protected** variables for internal implementation.
- Use **private** variables for sensitive data.
- Use **@property** with private variables.
- Never modify protected or private variables directly from outside the class.

---

# Interview Questions

## What is Encapsulation?

Wrapping data and methods inside a class while controlling access to the data.

---

## What is a Public Member?

A normal variable that can be accessed from anywhere.

Example

```python
self.name
```

---

## What is a Protected Member?

A variable starting with one underscore.

Example

```python
self._salary
```

It is a convention for internal use.

---

## What is a Private Member?

A variable starting with two underscores.

Example

```python
self.__password
```

Python applies **name mangling** to it.

---

## What is Name Mangling?

Python changes

```python
__password
```

into

```python
_User__password
```

internally to reduce accidental access and naming conflicts.

---

## Why use Properties with Private Variables?

Properties provide a safe way to read and modify private data while allowing validation.

---

# Summary

- **Encapsulation** protects object data by controlling access.
- **Public (`name`)** → Accessible from anywhere.
- **Protected (`_name`)** → Internal use by convention.
- **Private (`__name`)** → Python applies name mangling.
- **Name Mangling** changes `__variable` to `_ClassName__variable`.
- Use **@property**, **getter**, and **setter** with private variables to safely expose data.
- Encapsulation makes code safer, cleaner, and easier to maintain.