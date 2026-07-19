# 📘 range_function.md

# Python `range()` Function

## What is `range()`?

The `range()` function generates a sequence of numbers.

It is commonly used with `for` loops.

---

# Syntax

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

---

# range(stop)

Starts from **0** and ends before **stop**.

```python
for i in range(5):
    print(i)
```

Output

```text
0
1
2
3
4
```

---

# range(start, stop)

Starts from **start** and ends before **stop**.

```python
for i in range(2, 7):
    print(i)
```

Output

```text
2
3
4
5
6
```

---

# range(start, stop, step)

```python
for i in range(2, 11, 2):
    print(i)
```

Output

```text
2
4
6
8
10
```

---

# Negative Step

```python
for i in range(10, 0, -1):
    print(i)
```

Output

```text
10
9
8
7
6
5
4
3
2
1
```

---

# Convert to List

```python
numbers = list(range(5))

print(numbers)
```

Output

```text
[0, 1, 2, 3, 4]
```

---

# Common Examples

## Print 1–10

```python
for i in range(1, 11):
    print(i)
```

---

## Print Even Numbers

```python
for i in range(2, 21, 2):
    print(i)
```

---

## Print Odd Numbers

```python
for i in range(1, 20, 2):
    print(i)
```

---

## Countdown

```python
for i in range(5, 0, -1):
    print(i)
```

---

# Common Mistakes

❌

```python
range(1,10,0)
```

Step cannot be **0**.

---

# Time Complexity

| Operation | Complexity |
|-----------|------------|
| Iterate through range(n) | O(n) |
| Create range object | O(1) |

---

# Summary

- Generates a sequence of numbers.
- Stop value is **not included**.
- Mostly used with `for` loops.