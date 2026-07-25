# 34 - Class Methods & Static Methods

# Types of Methods

Python classes have three main types of methods:

1. Instance Method
2. Class Method
3. Static Method

---

# 1. Instance Method

Instance methods work with **instance variables**.

They require an object to be called.

Syntax

```python
class Student:

    def display(self):
        print(self.name)
```

Call

```python
student.display()
```

Uses

- self
- Object data
- Instance variables

---

# 2. Class Method

Class methods work with **class variables**.

They use the `@classmethod` decorator.

Instead of `self`, they receive `cls`.

Syntax

```python
class Student:

    school = "UOG"

    @classmethod
    def show_school(cls):
        print(cls.school)
```

Call

```python
Student.show_school()
```

Uses

- cls
- Class variables
- Shared data

---

# 3. Static Method

A static method belongs to the class but **does not use** instance variables or class variables.

It behaves like a normal utility function placed inside a class.

Syntax

```python
class Student:

    @staticmethod
    def greet():
        print("Welcome")
```

Call

```python
Student.greet()
```

Uses

- No self
- No cls
- Utility/helper functions

---

# self vs cls

self

- Current object
- Access instance variables

cls

- Current class
- Access class variables

---

# Comparison

| Feature | Instance Method | Class Method | Static Method |
|----------|-----------------|--------------|---------------|
| First Parameter | self | cls | None |
| Uses Object Data | ✅ | ❌ | ❌ |
| Uses Class Data | ✅ | ✅ | ❌ |
| Needs Decorator | ❌ | @classmethod | @staticmethod |
| Called Using | Object | Class | Class/Object |

---

# Real-Life Example

Bank Account

Instance Method

```python
deposit()
```

Changes one customer's balance.

---

Class Method

```python
change_interest_rate()
```

Changes the interest rate for all accounts.

---

Static Method

```python
validate_pin(pin)
```

Checks if a PIN format is valid.

No object data is required.

---

# Common Mistakes

❌ Forgetting decorators

Wrong

```python
def show_school(cls):
```

Correct

```python
@classmethod
def show_school(cls):
```

---

❌ Using self inside a static method

Wrong

```python
@staticmethod
def display():
    print(self.name)
```

No `self` exists in a static method.

---

# Best Practices

✔ Use instance methods for object-specific operations.

✔ Use class methods for shared class data.

✔ Use static methods for helper or utility functions.

---

# Interview Notes

Instance Method

- Uses self
- Works with object data

Class Method

- Uses cls
- Works with class data

Static Method

- Uses neither self nor cls
- Independent helper function

---

# Key Takeaways

✔ Instance methods access object data.

✔ Class methods access shared class data.

✔ Static methods perform utility tasks.

✔ Choose the method type based on what data is needed.