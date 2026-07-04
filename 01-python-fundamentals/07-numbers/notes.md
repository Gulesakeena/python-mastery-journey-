# Python Numbers Notes

## What are Python Numbers?

Python provides built-in numeric types for performing mathematical calculations.

According to the official Python documentation, there are **three primary numeric types**:

* `int` (Integer)
* `float` (Floating-point Number)
* `complex` (Complex Number)

Additionally, **Boolean (`bool`) is a subtype of `int`**, meaning `True` behaves like `1` and `False` behaves like `0`.

---

# Numeric Data Types

| Data Type | Description                           | Example                 |
| --------- | ------------------------------------- | ----------------------- |
| `int`     | Whole numbers                         | `10`, `-5`, `1000`      |
| `float`   | Decimal numbers                       | `3.14`, `10.0`, `-5.75` |
| `complex` | Numbers with real and imaginary parts | `2+3j`                  |

---

# Integer (`int`)

An **integer** is a whole number without a decimal point.

Examples:

```python
age = 21
marks = 95
temperature = -10
```

Output:

```python
print(type(age))
```

```text
<class 'int'>
```

### Features

* Stores positive and negative whole numbers.
* Supports unlimited precision (limited only by available memory).

---

# Float (`float`)

A **float** represents numbers with decimal points.

Examples:

```python
price = 99.99
height = 5.8
pi = 3.1415926535
```

Output:

```python
print(type(price))
```

```text
<class 'float'>
```

### Features

* Used for decimal values.
* Internally implemented using double-precision floating-point representation on most systems.

---

# Complex (`complex`)

A **complex number** has two parts:

* Real part
* Imaginary part

Syntax:

```python
real + imaginaryj
```

Example:

```python
number = 2 + 3j

print(number)
```

Output:

```text
(2+3j)
```

Access the real and imaginary parts:

```python
number = 2 + 3j

print(number.real)
print(number.imag)
```

Output:

```text
2.0
3.0
```

---

# Boolean is a Number

Python treats Boolean values as integers.

```python
print(True)
print(False)
```

Internally:

```python
True == 1
False == 0
```

Example:

```python
print(True + False)
print(True * 10)
```

Output:

```text
1
10
```

---

# Create Numbers

Using numeric literals:

```python
x = 10
y = 5.5
z = 2 + 4j
```

Or using constructors:

```python
a = int(10)
b = float(10)
c = complex(2, 3)
```

---

# Number Type Conversion

Python allows conversion between numeric types.

```python
age = 21

print(float(age))
print(complex(age))
```

Output:

```text
21.0
(21+0j)
```

Examples:

```python
print(int(5.9))
print(float(10))
print(complex(5))
```

Output:

```text
5
10.0
(5+0j)
```

---

# Mixed Arithmetic

Python automatically converts the smaller numeric type into the larger one when performing arithmetic.

Examples:

```python
print(10 + 5.5)
```

Output:

```text
15.5
```

```python
print(5 + (2 + 3j))
```

Output:

```text
(7+3j)
```

Conversion order:

```text
int → float → complex
```

---

# Arithmetic Operators

| Operator | Description    | Example  |
| -------- | -------------- | -------- |
| `+`      | Addition       | `5 + 2`  |
| `-`      | Subtraction    | `5 - 2`  |
| `*`      | Multiplication | `5 * 2`  |
| `/`      | Division       | `5 / 2`  |
| `//`     | Floor Division | `5 // 2` |
| `%`      | Modulus        | `5 % 2`  |
| `**`     | Exponent       | `5 ** 2` |

Examples:

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

Output:

```text
13
7
30
3.3333333333333335
3
1
1000
```

---

# Useful Built-in Functions

## abs()

Returns the absolute value.

```python
print(abs(-20))
```

Output:

```text
20
```

---

## round()

Rounds a floating-point number.

```python
print(round(3.14159, 2))
```

Output:

```text
3.14
```

---

## pow()

Raises a number to a power.

```python
print(pow(2, 5))
```

Output:

```text
32
```

---

## min() and max()

```python
print(min(10, 20, 30))
print(max(10, 20, 30))
```

Output:

```text
10
30
```

---

# Check the Data Type

Use the `type()` function.

```python
print(type(10))
print(type(3.14))
print(type(2 + 3j))
```

Output:

```text
<class 'int'>
<class 'float'>
<class 'complex'>
```

---

# Important Interview Questions

### Q1. How many built-in numeric types does Python have?

**Answer:**

Three:

* `int`
* `float`
* `complex`

---

### Q2. Is `bool` a numeric type?

Yes.

`bool` is a subclass of `int`.

```python
print(isinstance(True, int))
```

Output:

```text
True
```

---

### Q3. Which numeric type has unlimited precision?

**Answer:**

`int`

---

### Q4. Can Python perform arithmetic on different numeric types?

Yes.

Python automatically converts the smaller type to the larger one.

Example:

```python
print(5 + 5.5)
```

Output:

```text
10.5
```

---

# Best Practices

* Use `int` for whole numbers.
* Use `float` for decimal values.
* Use `complex` only when working with complex mathematics.
* Avoid comparing floating-point numbers for exact equality because of precision limitations.
* Use `type()` or `isinstance()` to verify numeric types when needed.

---

# Summary

* Python has **three primary built-in numeric types**: `int`, `float`, and `complex`.
* `bool` is a subtype of `int`.
* Integers support unlimited precision.
* Python automatically promotes numeric types during mixed arithmetic (`int → float → complex`).
* Use constructors (`int()`, `float()`, `complex()`) to convert between numeric types.
* Common arithmetic operators include `+`, `-`, `*`, `/`, `//`, `%`, and `**`.
