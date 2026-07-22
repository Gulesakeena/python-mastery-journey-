# 27 - Python Exception Handling

## What is an Exception?

An exception is a runtime error that interrupts the normal flow of a program.

Examples:

- Division by zero
- File not found
- Invalid user input
- Index out of range
- Key not found
- Type mismatch

Instead of crashing, Python allows us to handle these errors using exception handling.

---

# Basic Syntax

```python
try:
    # risky code
except:
    # handle error
```

---

# Example

```python
try:
    num = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

# Catch Multiple Exceptions

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
```

---

# Using else

The `else` block runs only if no exception occurs.

```python
try:
    num = int(input("Enter: "))
except ValueError:
    print("Invalid Input")
else:
    print("You entered:", num)
```

---

# Using finally

The `finally` block always executes.

```python
try:
    file = open("data.txt")
except FileNotFoundError:
    print("File not found.")
finally:
    print("Program Finished")
```

Use `finally` for cleanup tasks like:

- Closing files
- Closing database connections
- Releasing resources

---

# Catching Multiple Exceptions Together

```python
try:
    value = int(input())
except (ValueError, TypeError):
    print("Invalid input.")
```

---

# Generic Exception

```python
try:
    ...
except Exception as e:
    print(e)
```

Use this only when necessary. Prefer catching specific exceptions.

---

# Raising Exceptions

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative.")
```

---

# Custom Exceptions

```python
class InvalidAgeError(Exception):
    pass

age = -1

if age < 0:
    raise InvalidAgeError("Invalid age.")
```

---

# Common Exceptions

| Exception | Description |
|-----------|-------------|
| ValueError | Wrong value |
| TypeError | Wrong data type |
| ZeroDivisionError | Division by zero |
| IndexError | Invalid list index |
| KeyError | Missing dictionary key |
| FileNotFoundError | File does not exist |
| NameError | Variable not defined |
| AttributeError | Missing attribute |
| ImportError | Import failed |

---

# Best Practices

- Catch specific exceptions.
- Avoid using bare `except:`.
- Use `finally` for cleanup.
- Don't hide errors silently.
- Raise meaningful exceptions.

---

# Interview Questions

## Difference between SyntaxError and Exception?

- SyntaxError → Before execution.
- Exception → During execution.

---

## When is finally executed?

Always, whether an exception occurs or not.

---

## Why use else?

To execute code only when no exception occurs.

---

## Why create custom exceptions?

To represent application-specific errors clearly.

---

# Key Takeaways

- `try` → Risky code
- `except` → Handle error
- `else` → Runs if no error
- `finally` → Always runs
- `raise` → Manually throw an exception