# Python Operators

## Introduction

Operators are special symbols that perform operations on variables and values.

Example:

```python
a = 10
b = 5

print(a + b)
```

Output

```
15
```

---

# Types of Operators

Python has the following types of operators:

- Arithmetic Operators
- Assignment Operators
- Comparison Operators
- Logical Operators
- Identity Operators
- Membership Operators
- Bitwise Operators

---

# 1. Arithmetic Operators

Used to perform mathematical operations.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `10 + 5` | `15` |
| `-` | Subtraction | `10 - 5` | `5` |
| `*` | Multiplication | `10 * 5` | `50` |
| `/` | Division | `10 / 5` | `2.0` |
| `//` | Floor Division | `10 // 3` | `3` |
| `%` | Modulus | `10 % 3` | `1` |
| `**` | Exponent | `2 ** 3` | `8` |

Example

```python
a = 20
b = 6

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** 2)
```

Output

```
26
14
120
3.3333333333333335
3
2
400
```

---

# 2. Assignment Operators

Used to assign values to variables.

| Operator | Example | Same As |
|----------|---------|---------|
| `=` | `x = 5` | Assign value |
| `+=` | `x += 3` | `x = x + 3` |
| `-=` | `x -= 3` | `x = x - 3` |
| `*=` | `x *= 3` | `x = x * 3` |
| `/=` | `x /= 3` | `x = x / 3` |
| `//=` | `x //= 3` | `x = x // 3` |
| `%=` | `x %= 3` | `x = x % 3` |
| `**=` | `x **= 3` | `x = x ** 3` |

Example

```python
x = 10

x += 5
print(x)

x *= 2
print(x)
```

Output

```
15
30
```

---

# 3. Comparison Operators

Return `True` or `False`.

| Operator | Description | Example |
|----------|-------------|---------|
| `==` | Equal | `5 == 5` |
| `!=` | Not Equal | `5 != 3` |
| `>` | Greater Than | `10 > 5` |
| `<` | Less Than | `5 < 10` |
| `>=` | Greater Than or Equal | `5 >= 5` |
| `<=` | Less Than or Equal | `5 <= 8` |

Example

```python
print(10 == 10)
print(10 != 5)
print(5 < 10)
print(10 >= 20)
```

Output

```
True
True
True
False
```

---

# 4. Logical Operators

Used to combine conditions.

## and

Returns `True` if both conditions are `True`.

```python
print(True and True)
print(True and False)
```

Output

```
True
False
```

---

## or

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

---

## not

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

---

# 5. Identity Operators

Compare whether two variables refer to the same object.

| Operator | Description |
|----------|-------------|
| `is` | Same object |
| `is not` | Different objects |

Example

```python
a = [1, 2]
b = a

print(a is b)
print(a is not b)
```

Output

```
True
False
```

Example

```python
x = [1, 2]
y = [1, 2]

print(x == y)
print(x is y)
```

Output

```
True
False
```

---

# 6. Membership Operators

Used to test membership in a sequence.

| Operator | Description |
|----------|-------------|
| `in` | Value exists |
| `not in` | Value does not exist |

Example

```python
text = "Python"

print("P" in text)
print("Java" in text)
print("Java" not in text)
```

Output

```
True
False
True
```

---

# 7. Bitwise Operators

Operate on binary numbers.

| Operator | Name | Example |
|----------|------|---------|
| `&` | AND | `5 & 3` |
| `|` | OR | `5 | 3` |
| `^` | XOR | `5 ^ 3` |
| `~` | NOT | `~5` |
| `<<` | Left Shift | `5 << 1` |
| `>>` | Right Shift | `5 >> 1` |

Example

```python
print(5 & 3)
print(5 | 3)
print(5 ^ 3)
print(~5)
print(5 << 1)
print(5 >> 1)
```

Output

```
1
7
6
-6
10
2
```

---

# Operator Precedence

Order in which Python evaluates operators.

Highest → Lowest

1. `()`
2. `**`
3. `+x`, `-x`, `~x`
4. `*`, `/`, `//`, `%`
5. `+`, `-`
6. `<<`, `>>`
7. `&`
8. `^`
9. `|`
10. `==`, `!=`, `>`, `<`, `>=`, `<=`, `is`, `is not`, `in`, `not in`
11. `not`
12. `and`
13. `or`

Example

```python
print(2 + 3 * 4)
```

Output

```
14
```

Example

```python
print((2 + 3) * 4)
```

Output

```
20
```

---

# Common Interview Examples

## Check Even Number

```python
number = 10

print(number % 2 == 0)
```

---

## Swap Variables

```python
a = 10
b = 20

a, b = b, a

print(a, b)
```

Output

```
20 10
```

---

## Check Positive Number

```python
number = 5

print(number > 0)
```

---

## Check Password Length

```python
password = "Python@123"

print(len(password) >= 8)
```

---

## Check Character Exists

```python
text = "Python"

print("P" in text)
```

---

# Common Mistakes

## Assignment vs Comparison

❌ Wrong

```python
if x = 5:
```

✅ Correct

```python
if x == 5:
```

---

## Identity vs Equality

❌

```python
a is b
```

Checks memory location.

✅

```python
a == b
```

Checks values.

---

## Integer Division

```python
10 / 3
```

Output

```
3.3333333333333335
```

```python
10 // 3
```

Output

```
3
```

---

# Quick Cheat Sheet

```python
# Arithmetic
+
-
*
/
//
%
**

# Assignment
=
+=
-=
*=
/=
//=
%=
**=

# Comparison
==
!=
>
<
>=
<=

# Logical
and
or
not

# Identity
is
is not

# Membership
in
not in

# Bitwise
&
|
^
~
<<
>>
```

---

# Summary

- Arithmetic operators perform mathematical calculations.
- Assignment operators assign and update values.
- Comparison operators return Boolean values.
- Logical operators combine conditions.
- Identity operators compare object identity.
- Membership operators check whether a value exists in a sequence.
- Bitwise operators work with binary numbers.
- Use parentheses `()` to make expressions clear and control evaluation order.

---

# References

- Python Official Documentation: https://docs.python.org/3/reference/expressions.html#operator-precedence
- Python Standard Library: https://docs.python.org/3/library/operator.html
- W3Schools Python Operators: https://www.w3schools.com/python/python_operators.asp