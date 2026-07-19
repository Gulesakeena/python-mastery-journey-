# 📘 for_loops.md

# Python `for` Loop

## What is a `for` Loop?

A `for` loop is used to iterate over a sequence such as:

- List
- Tuple
- String
- Dictionary
- Set
- Range

It repeats a block of code once for every item.

---

# Syntax

```python
for variable in sequence:
    # code
```

---

# Example 1

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

# Using `range()`

## range(stop)

```python
for i in range(5):
    print(i)
```

---

## range(start, stop)

```python
for i in range(2, 6):
    print(i)
```

Output

```text
2
3
4
5
```

---

## range(start, stop, step)

```python
for i in range(0, 11, 2):
    print(i)
```

Output

```text
0
2
4
6
8
10
```

---

# Loop Through a List

```python
fruits = ["Apple", "Banana", "Orange"]

for fruit in fruits:
    print(fruit)
```

---

# Loop Through a Tuple

```python
numbers = (1, 2, 3)

for num in numbers:
    print(num)
```

---

# Loop Through a String

```python
text = "Python"

for ch in text:
    print(ch)
```

---

# Loop Through a Set

```python
numbers = {1, 2, 3}

for num in numbers:
    print(num)
```

---

# Loop Through a Dictionary

## Keys

```python
student = {
    "name": "Ali",
    "age": 20
}

for key in student:
    print(key)
```

---

## Values

```python
for value in student.values():
    print(value)
```

---

## Keys and Values

```python
for key, value in student.items():
    print(key, value)
```

---

# Common Examples

## Print 1 to 10

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

## Sum of Numbers

```python
total = 0

for i in range(1, 6):
    total += i

print(total)
```

---

## Multiplication Table

```python
number = 5

for i in range(1, 11):
    print(number, "x", i, "=", number * i)
```

---

## Count Characters

```python
text = "Python"

count = 0

for ch in text:
    count += 1

print(count)
```

---

# Time Complexity

| Operation | Complexity |
|-----------|------------|
| Loop over n items | O(n) |
| range() iteration | O(n) |

---

# Summary

- Used to iterate over sequences.
- Cleaner than `while` when number of iterations is known.
- Works with lists, tuples, sets, dictionaries, strings, and ranges.