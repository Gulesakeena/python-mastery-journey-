# Python Booleans

## 1. Introduction

A Boolean is a data type that represents one of two values:

- `True`
- `False`

Booleans are commonly used in:

- Decision making
- Conditions
- Loops
- Comparisons
- Logical operations

---

# 2. Boolean Values

```python
print(True)
print(False)
```

Output

```
True
False
```

---

# 3. Boolean Data Type

Use the `type()` function to check the data type.

```python
x = True
y = False

print(type(x))
print(type(y))
```

Output

```
<class 'bool'>
<class 'bool'>
```

---

# 4. Creating Boolean Variables

```python
is_logged_in = True
is_admin = False

print(is_logged_in)
print(is_admin)
```

Output

```
True
False
```

---

# 5. Boolean from Comparison Operators

Comparison operators always return a Boolean value.

```python
print(10 > 5)
print(10 < 5)
print(10 == 10)
print(10 != 10)
```

Output

```
True
False
True
False
```

---

# 6. Comparison Operators

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `10 > 5` | `True` |
| `<` | Less than | `2 < 1` | `False` |
| `>=` | Greater than or equal | `5 >= 5` | `True` |
| `<=` | Less than or equal | `5 <= 4` | `False` |

---

# 7. Boolean in if Statements

```python
age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Output

```
Adult
```

---

# 8. The bool() Function

The `bool()` function converts a value into either `True` or `False`.

Syntax

```python
bool(value)
```

Example

```python
print(bool(1))
print(bool(0))
```

Output

```
True
False
```

---

# 9. Values That Return False

The following values evaluate to `False`.

## Numbers

```python
print(bool(0))
print(bool(0.0))
```

Output

```
False
False
```

---

## Empty String

```python
print(bool(""))
```

Output

```
False
```

---

## Empty List

```python
print(bool([]))
```

Output

```
False
```

---

## Empty Tuple

```python
print(bool(()))
```

Output

```
False
```

---

## Empty Dictionary

```python
print(bool({}))
```

Output

```
False
```

---

## Empty Set

```python
print(bool(set()))
```

Output

```
False
```

---

## None

```python
print(bool(None))
```

Output

```
False
```

---

# 10. Values That Return True

Everything else is generally considered `True`.

```python
print(bool(10))
print(bool(-5))
print(bool("Python"))
print(bool([1,2,3]))
print(bool({"name":"Ali"}))
```

Output

```
True
True
True
True
True
```

---

# 11. Boolean Operators

## AND

Returns `True` only if both conditions are `True`.

```python
print(True and True)
print(True and False)
```

Output

```
True
False
```

Truth Table

| A | B | A and B |
|---|---|----------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

---

## OR

Returns `True` if at least one condition is `True`.

```python
print(True or False)
print(False or False)
```

Output

```
True
False
```

Truth Table

| A | B | A or B |
|---|---|---------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

---

## NOT

Reverses the Boolean value.

```python
print(not True)
print(not False)
```

Output

```
False
True
```

Truth Table

| A | not A |
|---|-------|
| True | False |
| False | True |

---

# 12. Boolean with Strings

```python
name = "Python"

if name:
    print("String is not empty")
```

Output

```
String is not empty
```

---

# 13. Boolean with Lists

```python
numbers = []

if numbers:
    print("Not Empty")
else:
    print("Empty")
```

Output

```
Empty
```

---

# 14. Boolean with Numbers

```python
number = 0

if number:
    print("True")
else:
    print("False")
```

Output

```
False
```

---

# 15. Membership Operators

Returns a Boolean value.

```python
text = "Python"

print("P" in text)
print("Java" in text)
```

Output

```
True
False
```

---

# 16. Identity Operators

## is

Checks whether two variables refer to the same object.

```python
a = [1,2]
b = a

print(a is b)
```

Output

```
True
```

---

## is not

```python
a = [1]
b = [1]

print(a is not b)
```

Output

```
True
```

---

# 17. Equality vs Identity

Equality (`==`)

Checks values.

```python
a = [1,2]
b = [1,2]

print(a == b)
```

Output

```
True
```

Identity (`is`)

Checks memory location.

```python
print(a is b)
```

Output

```
False
```

---

# 18. Functions Returning Boolean

```python
def is_even(number):
    return number % 2 == 0

print(is_even(10))
print(is_even(7))
```

Output

```
True
False
```

---

# 19. Practical Examples

## Check Adult

```python
age = 18

print(age >= 18)
```

Output

```
True
```

---

## Check Password Length

```python
password = "Python@123"

print(len(password) >= 8)
```

Output

```
True
```

---

## Check Positive Number

```python
number = 5

print(number > 0)
```

Output

```
True
```

---

# 20. Short-Circuit Evaluation

Python stops evaluating as soon as the result is known.

```python
False and print("Hello")
```

Output

```
False
```

`print("Hello")` is never executed.

---

# 21. Common Interview Questions

### Check if a number is even

```python
number = 10

print(number % 2 == 0)
```

---

### Check if a string is empty

```python
text = ""

print(bool(text))
```

---

### Check if a list is empty

```python
numbers = []

if numbers:
    print("Not Empty")
else:
    print("Empty")
```

---

### Check username

```python
username = input("Enter username: ")

if username:
    print("Valid")
else:
    print("Username cannot be empty")
```

---

# 22. Boolean Best Practices

✅ Use meaningful Boolean variable names.

```python
is_logged_in = True
has_permission = False
is_student = True
```

❌ Avoid names like:

```python
flag = True
x = False
```

---

# 23. Summary

- A Boolean has only two values: `True` and `False`.
- Comparison operators return Boolean values.
- `bool()` converts values to `True` or `False`.
- Empty objects (`""`, `[]`, `{}`, `()`, `set()`) are `False`.
- `0` and `None` are `False`.
- Everything else is usually `True`.
- Logical operators:
  - `and`
  - `or`
  - `not`
- Use `==` to compare values.
- Use `is` to compare object identity.

---


# References

- Python Official Documentation:
  https://docs.python.org/3/library/stdtypes.html#boolean-type-bool

- Python Official Truth Value Testing:
  https://docs.python.org/3/library/stdtypes.html#truth-value-testing

- W3Schools Python Booleans:
  https://www.w3schools.com/python/python_booleans.asp