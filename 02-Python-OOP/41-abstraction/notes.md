# 41 - Abstraction

# What is Abstraction?

Abstraction means **hiding implementation details** and exposing only the necessary functionality.

Users know **what** an object does, but not **how** it does it.

---

# Real-Life Example

ATM Machine

You insert your card.

You enter your PIN.

You withdraw money.

You never see how the bank verifies your account internally.

Only the required functionality is exposed.

---

# Another Example

Car

You press the accelerator.

The car moves.

You do not need to know how the engine, transmission, and fuel injection work.

---

# Why Use Abstraction?

- Hides unnecessary complexity.
- Makes code easier to use.
- Improves maintainability.
- Encourages consistent interfaces.
- Reduces coupling between classes.

---

# Abstract Class

An abstract class cannot be instantiated directly.

It serves as a blueprint for other classes.

Python provides the **abc** module for creating abstract classes.

```python
from abc import ABC, abstractmethod
```

---

# Creating an Abstract Class

```python
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
```

`Shape` cannot be instantiated.

---

# Child Class

```python
class Circle(Shape):

    def area(self):
        return 3.14 * 5 * 5
```

The child class must implement all abstract methods.

---

# What Happens If You Don't?

```python
class Rectangle(Shape):
    pass
```

Creating an object

```python
Rectangle()
```

Results in

```
TypeError

Can't instantiate abstract class Rectangle
```

because `area()` was not implemented.

---

# Multiple Abstract Methods

```python
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def move(self):
        pass
```

Every child class must implement both methods.

---

# Abstraction vs Encapsulation

## Abstraction

Focus

```
What should the object do?
```

Example

ATM Machine

---

## Encapsulation

Focus

```
How is the data protected?
```

Example

Private variables

---

# Comparison

| Abstraction | Encapsulation |
|-------------|---------------|
| Hides implementation | Hides data |
| Uses abstract classes | Uses access modifiers |
| Focuses on behavior | Focuses on security |

---

# Advantages

✔ Reduces complexity

✔ Encourages code reuse

✔ Improves maintainability

✔ Makes APIs easier to understand

✔ Standardizes object behavior

---

# Best Practices

- Use abstraction for common interfaces.
- Keep abstract classes focused.
- Do not place unnecessary implementation inside abstract methods.
- Prefer meaningful method names.

---

# Key Takeaways

- Abstraction hides implementation details.
- Python uses the `abc` module.
- Abstract classes cannot be instantiated.
- Child classes must implement abstract methods.
- Abstraction defines **what** should happen, not **how**.