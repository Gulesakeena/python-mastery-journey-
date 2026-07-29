# 42 - Dataclasses

# What is a Dataclass?

A dataclass is a special type of class that automatically generates common methods such as:

- __init__()
- __repr__()
- __eq__()

This reduces repetitive code.

---

# Import

```python
from dataclasses import dataclass
```

---

# Basic Example

Without Dataclass

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

With Dataclass

```python
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
```

Python automatically creates the constructor.

---

# Generated Methods

Dataclasses automatically generate:

- __init__()
- __repr__()
- __eq__()

Example

```python
student = Student("Ali", 22)

print(student)
```

Output

```
Student(name='Ali', age=22)
```

---

# Default Values

```python
@dataclass
class Student:

    name: str
    age: int = 20
```

---

# field()

Used for advanced configuration.

```python
from dataclasses import field
```

Example

```python
grades: list = field(default_factory=list)
```

---

# Why default_factory?

Wrong

```python
grades = []
```

Every object shares the same list.

Correct

```python
grades = field(default_factory=list)
```

Each object gets a new list.

---

# __post_init__()

Runs immediately after __init__().

Useful for validation and calculated fields.

Example

```python
@dataclass
class Product:

    price: float
    quantity: int

    def __post_init__(self):
        self.total = self.price * self.quantity
```

---

# Frozen Dataclass

```python
@dataclass(frozen=True)
class Employee:
    id: int
```

Objects become immutable.

```python
employee.id = 10
```

Raises

```
FrozenInstanceError
```

---

# Dataclass Inheritance

```python
@dataclass
class Person:
    name: str

@dataclass
class Student(Person):
    roll: int
```

---

# Advantages

✔ Less code

✔ Readable

✔ Automatic methods

✔ Great for APIs

✔ Easy maintenance

---

# Dataclass vs Normal Class

| Dataclass | Normal Class |
|-----------|--------------|
| Less code | More boilerplate |
| Auto methods | Manual methods |
| Cleaner | More verbose |

---

# Best Practices

- Use dataclasses for data models.
- Use default_factory for mutable objects.
- Use __post_init__ for validation.
- Use frozen=True for immutable objects.

---

# Key Takeaways

- Dataclasses reduce boilerplate.
- Python generates common methods automatically.
- field() customizes fields.
- __post_init__ performs post-processing.
- Frozen dataclasses are immutable.