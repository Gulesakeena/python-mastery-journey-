# 🐍 Packing & Unpacking in Python

> Complete guide to Packing and Unpacking in Python.

---

# What is Packing?

Packing means storing multiple values into a single variable.

Example:

```python
numbers = 1, 2, 3, 4
```

Python automatically packs these values into a tuple.

Output

```python
print(numbers)
```

```
(1, 2, 3, 4)
```

Type

```python
print(type(numbers))
```

```
<class 'tuple'>
```

---

# Packing with Parentheses

```python
numbers = (1, 2, 3)
```

---

# Packing Different Data Types

```python
person = ("Ali", 20, True, 95.5)
```

---

# What is Unpacking?

Unpacking means assigning each element of a tuple (or list) to separate variables.

```python
person = ("Ali", 20, "CS")

name, age, department = person

print(name)
print(age)
print(department)
```

Output

```
Ali
20
CS
```

---

# Unpacking a List

```python
numbers = [1, 2, 3]

a, b, c = numbers

print(a)
print(b)
print(c)
```

---

# Number of Variables Must Match

Correct

```python
numbers = (1, 2, 3)

a, b, c = numbers
```

Incorrect

```python
numbers = (1, 2, 3)

a, b = numbers
```

Output

```
ValueError
```

---

# Extended Unpacking (*)

Python allows one variable to collect multiple values.

```python
numbers = (1,2,3,4,5)

a, *b = numbers

print(a)
print(b)
```

Output

```
1
[2,3,4,5]
```

---

## Middle

```python
numbers = (1,2,3,4,5)

a, *b, c = numbers

print(a)
print(b)
print(c)
```

Output

```
1
[2,3,4]
5
```

---

## Beginning

```python
numbers = (1,2,3,4,5)

*a, b = numbers

print(a)
print(b)
```

Output

```
[1,2,3,4]
5
```

---

# Swapping Variables

Python uses tuple unpacking.

```python
a = 10
b = 20

a, b = b, a

print(a)
print(b)
```

Output

```
20
10
```

---

# Returning Multiple Values

```python
def calculate():
    return 10, 20

a, b = calculate()

print(a)
print(b)
```

---

# Ignoring Values

Use `_`.

```python
student = ("Ali",20,"CS")

name, _, department = student

print(name)
print(department)
```

---

# Nested Unpacking

```python
data = ("Ali",(20,"CS"))

name, (age, department) = data

print(name)
print(age)
print(department)
```

---

# Packing Function Arguments

```python
def show(*numbers):
    print(numbers)

show(1,2,3,4)
```

Output

```
(1,2,3,4)
```

---

# Unpacking Function Arguments

```python
def add(a,b):
    print(a+b)

numbers = (10,20)

add(*numbers)
```

---

# Packing vs Unpacking

| Packing | Unpacking |
|----------|-----------|
| Many values → One variable | One tuple/list → Many variables |
| Creates tuple | Extracts values |

---

# Time Complexity

| Operation | Complexity |
|-----------|------------|
| Packing | O(n) |
| Unpacking | O(n) |

---

# Interview Questions

### What is packing?

Storing multiple values into one tuple.

### What is unpacking?

Extracting tuple/list elements into separate variables.

### What is extended unpacking?

Using `*` to collect remaining values.

---

# Summary

- Packing → Many values into one tuple.
- Unpacking → Tuple values into variables.
- `*` performs extended unpacking.
- Commonly used in functions and variable swapping.