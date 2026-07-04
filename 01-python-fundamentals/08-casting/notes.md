# Python Type Casting Notes

## What is Type Casting?

**Type Casting** is the process of converting a value from one data type to another.

Python provides built-in functions to perform type conversion.

Common type casting functions:

* `int()`
* `float()`
* `str()`
* `bool()`
* `complex()`
* `list()`
* `tuple()`
* `set()`
* `dict()` (for compatible data)

---

# Why Do We Need Type Casting?

Type casting is useful when:

* Taking user input.
* Performing mathematical operations.
* Converting numbers into strings for display.
* Changing one collection type into another.
* Preparing data for processing.

Example:

```python
age = input("Enter your age: ")

print(age + 5)
```

Output:

```text
TypeError
```

Reason:

`input()` always returns a **string**.

Correct:

```python
age = int(input("Enter your age: "))

print(age + 5)
```

Output:

```text
26
```

---

# Implicit Type Casting

Python automatically converts one numeric type into another when needed.

Example:

```python
a = 10
b = 5.5

result = a + b

print(result)
print(type(result))
```

Output:

```text
15.5
<class 'float'>
```

Python converted the integer into a float automatically.

---

# Explicit Type Casting

Explicit type casting means the programmer converts the data type manually.

Example:

```python
age = "21"

age = int(age)

print(age)
print(type(age))
```

Output:

```text
21
<class 'int'>
```

---

# int()

Converts a value into an integer.

Examples:

```python
print(int(3.9))
print(int("100"))
print(int(True))
```

Output:

```text
3
100
1
```

### Invalid Example

```python
print(int("Hello"))
```

Output:

```text
ValueError
```

---

# float()

Converts a value into a floating-point number.

Examples:

```python
print(float(10))
print(float("3.14"))
print(float(True))
```

Output:

```text
10.0
3.14
1.0
```

---

# str()

Converts any object into a string.

Examples:

```python
age = 21

print(str(age))
```

Output:

```text
'21'
```

Example:

```python
price = 99.9

print(str(price))
```

Output:

```text
'99.9'
```

---

# bool()

Converts a value into either `True` or `False`.

## Values That Become False

```python
False
0
0.0
0j
''
""
[]
()
{}
set()
None
```

Everything else becomes `True`.

Examples:

```python
print(bool(0))
print(bool(10))
print(bool(""))
print(bool("Python"))
```

Output:

```text
False
True
False
True
```

---

# complex()

Creates a complex number.

Examples:

```python
print(complex(10))
print(complex(5, 3))
```

Output:

```text
(10+0j)
(5+3j)
```

---

# list()

Converts an iterable into a list.

Example:

```python
text = "Python"

print(list(text))
```

Output:

```text
['P', 'y', 't', 'h', 'o', 'n']
```

---

# tuple()

Converts an iterable into a tuple.

Example:

```python
numbers = [1, 2, 3]

print(tuple(numbers))
```

Output:

```text
(1, 2, 3)
```

---

# set()

Converts an iterable into a set.

Example:

```python
numbers = [1, 2, 2, 3]

print(set(numbers))
```

Output:

```text
{1, 2, 3}
```

Duplicate values are automatically removed.

---

# Dictionary Type Casting

A dictionary can be created from key-value pairs.

Example:

```python
pairs = [
    ("name", "Ali"),
    ("age", 21)
]

print(dict(pairs))
```

Output:

```text
{'name': 'Ali', 'age': 21}
```

---

# Common Type Conversion Table

| Function    | Converts To                       |
| ----------- | --------------------------------- |
| `int()`     | Integer                           |
| `float()`   | Float                             |
| `str()`     | String                            |
| `bool()`    | Boolean                           |
| `complex()` | Complex Number                    |
| `list()`    | List                              |
| `tuple()`   | Tuple                             |
| `set()`     | Set                               |
| `dict()`    | Dictionary (compatible data only) |

---

# Examples

### String → Integer

```python
age = "25"

print(int(age))
```

---

### Integer → Float

```python
marks = 90

print(float(marks))
```

---

### Integer → String

```python
number = 100

print(str(number))
```

---

### List → Tuple

```python
numbers = [1, 2, 3]

print(tuple(numbers))
```

---

### Tuple → List

```python
numbers = (1, 2, 3)

print(list(numbers))
```

---

### List → Set

```python
numbers = [1, 2, 2, 3]

print(set(numbers))
```

---

# Common Errors

## Error 1

```python
int("Hello")
```

Output:

```text
ValueError
```

Reason:

"Hello" is not a valid integer.

---

## Error 2

```python
int(3 + 4j)
```

Output:

```text
TypeError
```

Reason:

Complex numbers cannot be directly converted to integers.

---

## Error 3

```python
list(10)
```

Output:

```text
TypeError
```

Reason:

An integer is not iterable.

---

# Best Practices

* Convert `input()` to the required numeric type before calculations.
* Use `float()` when working with decimal values.
* Use `int()` only for whole numbers.
* Convert to `str()` before concatenating numbers with strings.
* Be careful when converting strings to numbers—invalid values raise `ValueError`.
* Use `bool()` to understand Python's truthy and falsy values.

---

# Interview Questions

### Q1. What is the difference between implicit and explicit type casting?

**Answer**

* Implicit type casting is performed automatically by Python.
* Explicit type casting is performed manually by the programmer using functions like `int()`, `float()`, and `str()`.

---

### Q2. Does `input()` return an integer?

No.

`input()` always returns a string.

---

### Q3. What is the difference between `int(3.9)` and `round(3.9)`?

```python
int(3.9)
```

Output:

```text
3
```

```python
round(3.9)
```

Output:

```text
4
```

`int()` truncates the decimal part.

`round()` rounds the value to the nearest integer.

---

### Q4. What values become `False` when passed to `bool()`?

* `False`
* `0`
* `0.0`
* `0j`
* Empty string
* Empty list
* Empty tuple
* Empty dictionary
* Empty set
* `None`

Everything else becomes `True`.

---

# Summary

* Type casting converts one data type into another.
* Python supports both implicit and explicit type casting.
* Common casting functions include `int()`, `float()`, `str()`, `bool()`, `complex()`, `list()`, `tuple()`, `set()`, and `dict()`.
* `input()` always returns a string.
* Invalid conversions raise exceptions such as `ValueError` or `TypeError`.
* Understanding type casting is essential for handling user input, calculations, and data manipulation.
