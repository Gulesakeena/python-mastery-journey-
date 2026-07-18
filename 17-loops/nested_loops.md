# 📘 nested_loops.md

# Python Nested Loops

## What are Nested Loops?

A nested loop is a loop inside another loop.

---

# Syntax

```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

---

# Example 1

```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

Output

```text
0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2
```

---

# Multiplication Table

```python
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end=" ")
    print()
```

---

# Rectangle Pattern

```python
for i in range(3):
    for j in range(5):
        print("*", end=" ")
    print()
```

Output

```text
* * * * *
* * * * *
* * * * *
```

---

# Right Triangle

```python
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
```

Output

```text
*
**
***
****
*****
```

---

# Inverted Triangle

```python
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
```

Output

```text
*****
****
***
**
*
```

---

# Compare Every Pair

```python
numbers = [1, 2, 3]

for i in numbers:
    for j in numbers:
        print(i, j)
```

---

# Nested while Loop

```python
i = 1

while i <= 3:
    j = 1

    while j <= 3:
        print(i, j)
        j += 1

    i += 1
```

---

# Time Complexity

If

Outer loop = n

Inner loop = n

```
O(n × n)

=

O(n²)
```

Example

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

Time Complexity

```
O(n²)
```

---

# Common Uses

- Pattern printing
- Matrix operations
- Comparing every pair
- Searching in 2D arrays
- Multiplication tables

---

# Summary

- A nested loop is a loop inside another loop.
- The inner loop runs completely for every iteration of the outer loop.
- Commonly used for matrices, patterns, and pair comparisons.
- Usually has **O(n²)** time complexity.