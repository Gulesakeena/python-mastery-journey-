# 🐍 Python Tuple Methods Cheat Sheet

> Quick reference for all tuple methods and commonly used built-in functions.

---

# 📌 Tuple Facts

- Ordered ✅
- Immutable ✅
- Allows Duplicates ✅
- Indexed ✅
- Faster than lists ✅
- Hashable (if all elements are immutable) ✅

---

# Tuple Methods

Unlike lists, **tuples have only two built-in methods.**

| Method | Description | Time Complexity |
|---------|-------------|-----------------|
| `count(x)` | Counts occurrences of `x` | O(n) |
| `index(x)` | Returns first index of `x` | O(n) |

---

# 1. count()

Counts how many times a value appears.

### Syntax

```python
tuple.count(value)
```

### Example

```python
numbers = (1, 2, 3, 2, 2, 4)

print(numbers.count(2))
```

Output

```
3
```

---

### Value Not Present

```python
numbers = (1, 2, 3)

print(numbers.count(10))
```

Output

```
0
```

---

# 2. index()

Returns the index of the first occurrence.

### Syntax

```python
tuple.index(value)
```

### Example

```python
numbers = (10, 20, 30, 40)

print(numbers.index(30))
```

Output

```
2
```

---

### Duplicate Values

```python
numbers = (1, 2, 2, 2, 3)

print(numbers.index(2))
```

Output

```
1
```

Only the **first occurrence** is returned.

---

### Value Not Found

```python
numbers = (1, 2, 3)

print(numbers.index(10))
```

Output

```
ValueError
```

---

# Useful Built-in Functions

Although tuples have only two methods, many Python built-in functions work with tuples.

| Function | Description |
|----------|-------------|
| `len()` | Number of elements |
| `max()` | Largest element |
| `min()` | Smallest element |
| `sum()` | Sum of numeric elements |
| `sorted()` | Returns a sorted list |
| `tuple()` | Creates a tuple |
| `list()` | Converts tuple to list |
| `any()` | True if at least one element is truthy |
| `all()` | True if all elements are truthy |
| `enumerate()` | Returns index-value pairs |
| `reversed()` | Returns a reverse iterator |

---

# len()

```python
numbers = (1, 2, 3)

print(len(numbers))
```

Output

```
3
```

---

# max()

```python
numbers = (5, 10, 2)

print(max(numbers))
```

Output

```
10
```

---

# min()

```python
numbers = (5, 10, 2)

print(min(numbers))
```

Output

```
2
```

---

# sum()

```python
numbers = (1, 2, 3, 4)

print(sum(numbers))
```

Output

```
10
```

---

# sorted()

Returns a **list**, not a tuple.

```python
numbers = (4, 2, 1, 3)

print(sorted(numbers))
```

Output

```
[1, 2, 3, 4]
```

---

# tuple()

Convert another iterable into a tuple.

```python
letters = tuple("Python")

print(letters)
```

Output

```
('P', 'y', 't', 'h', 'o', 'n')
```

---

# list()

Convert a tuple into a list.

```python
numbers = (1, 2, 3)

print(list(numbers))
```

Output

```
[1, 2, 3]
```

---

# any()

Returns `True` if **at least one** element is truthy.

```python
values = (0, False, 5)

print(any(values))
```

Output

```
True
```

---

# all()

Returns `True` only if **all** elements are truthy.

```python
values = (1, True, 5)

print(all(values))
```

Output

```
True
```

---

# enumerate()

Returns index-value pairs.

```python
fruits = ("Apple", "Banana", "Mango")

for index, value in enumerate(fruits):
    print(index, value)
```

Output

```
0 Apple
1 Banana
2 Mango
```

---

# reversed()

Returns a reverse iterator.

```python
numbers = (1, 2, 3)

for num in reversed(numbers):
    print(num)
```

Output

```
3
2
1
```

---

# Membership Operators

## in

```python
fruits = ("Apple", "Banana")

print("Apple" in fruits)
```

Output

```
True
```

---

## not in

```python
print("Orange" not in fruits)
```

Output

```
True
```

---

# Operators

## Concatenation

```python
a = (1, 2)
b = (3, 4)

print(a + b)
```

Output

```
(1, 2, 3, 4)
```

---

## Repetition

```python
print((1, 2) * 3)
```

Output

```
(1, 2, 1, 2, 1, 2)
```

---

# Time Complexity

| Operation | Complexity |
|-----------|------------|
| Indexing | O(1) |
| Slicing | O(k) |
| `count()` | O(n) |
| `index()` | O(n) |
| Membership (`in`) | O(n) |
| Iteration | O(n) |
| Concatenation (`+`) | O(n) |
| Repetition (`*`) | O(n × k) |
| `len()` | O(1) |
| `max()` | O(n) |
| `min()` | O(n) |
| `sum()` | O(n) |
| `sorted()` | O(n log n) |

---

# Quick Interview Notes

### How many methods does a tuple have?

Only **2 methods**:

- `count()`
- `index()`

---

### Why so few methods?

Because tuples are **immutable**.

Their contents cannot be changed after creation.

---

### Can you append to a tuple?

❌ No

```python
numbers = (1, 2, 3)

numbers.append(4)
```

Output

```
AttributeError
```

---

### Can you remove elements?

❌ No

Tuples do not support:

- `append()`
- `extend()`
- `insert()`
- `remove()`
- `pop()`
- `clear()`
- `sort()`
- `reverse()`

Use a **list** if you need to modify elements.

---

# Summary

## Tuple Methods

| Method | Purpose |
|---------|---------|
| `count(x)` | Count occurrences |
| `index(x)` | Find first index |

---

## Most Used Built-in Functions

| Function | Purpose |
|----------|---------|
| `len()` | Length |
| `sum()` | Sum |
| `max()` | Largest value |
| `min()` | Smallest value |
| `sorted()` | Sorted list |
| `tuple()` | Create tuple |
| `list()` | Convert to list |
| `any()` | At least one truthy value |
| `all()` | All truthy values |
| `enumerate()` | Index-value pairs |
| `reversed()` | Reverse iterator |

---

> **Remember:** Tuples are immutable, so they have only **2 built-in methods**. For any modification (adding, removing, sorting, etc.), convert the tuple to a list first.