# 📘 Time Complexity of Python Sets

## What is Time Complexity?

Time Complexity tells us **how the running time of an operation grows as the input size (`n`) increases**.

It is represented using **Big O Notation**.

---

# Common Big O Notations

| Big O | Name | Performance |
|-------|------|-------------|
| **O(1)** | Constant | ⭐⭐⭐⭐⭐ Fastest |
| **O(log n)** | Logarithmic | ⭐⭐⭐⭐ |
| **O(n)** | Linear | ⭐⭐⭐ |
| **O(n log n)** | Linearithmic | ⭐⭐ |
| **O(n²)** | Quadratic | ⭐ |
| **O(2ⁿ)** | Exponential | Very Slow |
| **O(n!)** | Factorial | Worst |

---

# Why Are Sets Fast?

Python sets are implemented using a **Hash Table**.

When you:

- add an element
- search for an element
- remove an element

Python computes the **hash** of the element and directly jumps to its memory location instead of checking every element one by one.

That's why most set operations are **O(1)** on average.

---

# Set Operation Complexities

| Operation | Average Complexity | Worst Case |
|-----------|--------------------|------------|
| Create Set | O(n) | O(n) |
| Search (`in`) | O(1) | O(n) |
| Add | O(1) | O(n) |
| Remove | O(1) | O(n) |
| Discard | O(1) | O(n) |
| Pop | O(1) | O(n) |
| Clear | O(n) | O(n) |
| Copy | O(n) | O(n) |
| Iterate | O(n) | O(n) |
| Length (`len`) | O(1) | O(1) |

---

# Membership Test

```python
numbers = {1, 2, 3, 4, 5}

print(3 in numbers)
```

Time Complexity

```
O(1)
```

Reason:

Python calculates the hash of `3` and directly checks its location.

---

# Add Element

```python
numbers = {1, 2, 3}

numbers.add(4)
```

Time Complexity

```
O(1)
```

---

# Remove Element

```python
numbers.remove(2)
```

Time Complexity

```
O(1)
```

---

# Discard Element

```python
numbers.discard(10)
```

Time Complexity

```
O(1)
```

---

# Pop Element

```python
numbers.pop()
```

Time Complexity

```
O(1)
```

---

# Clear Set

```python
numbers.clear()
```

Time Complexity

```
O(n)
```

Reason:

Every element must be removed.

---

# Copy Set

```python
copy_set = numbers.copy()
```

Time Complexity

```
O(n)
```

Reason:

Every element is copied.

---

# Union

```python
A = {1, 2, 3}
B = {3, 4, 5}

A | B
```

Time Complexity

```
O(len(A) + len(B))
```

Reason:

Python visits every element from both sets.

---

# Intersection

```python
A & B
```

Time Complexity

```
O(min(len(A), len(B)))
```

Reason:

Python loops through the smaller set and checks membership in the larger set.

---

# Difference

```python
A - B
```

Time Complexity

```
O(len(A))
```

Reason:

Each element of `A` is checked once.

---

# Symmetric Difference

```python
A ^ B
```

Time Complexity

```
O(len(A) + len(B))
```

---

# Subset

```python
A <= B
```

Time Complexity

```
O(len(A))
```

---

# Superset

```python
A >= B
```

Time Complexity

```
O(len(B))
```

---

# Disjoint

```python
A.isdisjoint(B)
```

Time Complexity

```
O(min(len(A), len(B)))
```

---

# Convert List to Set

```python
numbers = [1, 2, 3, 4]

s = set(numbers)
```

Time Complexity

```
O(n)
```

---

# Convert Set to List

```python
numbers = {1, 2, 3}

lst = list(numbers)
```

Time Complexity

```
O(n)
```

---

# Why Lookup is O(1)?

Example:

```python
numbers = {10, 20, 30, 40}

print(30 in numbers)
```

Python **does not** check:

```
10
20
30
40
```

Instead, it:

1. Computes the hash of `30`.
2. Finds the memory location.
3. Checks that location directly.

So the lookup takes approximately **constant time (O(1))**.

---

# Worst Case

Sometimes two different elements produce the same hash value (**hash collision**).

Then Python may need to check multiple elements.

Example:

```
Hash Collision

50 ---> Bucket A

150 ---> Bucket A

250 ---> Bucket A
```

Searching may become slower.

Worst case:

```
O(n)
```

However, Python's hash table implementation makes collisions rare, so average performance remains **O(1)**.

---

# Memory Trick

```
Set
↓

Hash Table

↓

Hash Value

↓

Direct Memory Location

↓

Fast Search (O(1))
```

---

# Comparison with Lists

| Operation | List | Set |
|-----------|------|-----|
| Search | O(n) | O(1) |
| Add | O(1) (append) | O(1) |
| Remove by Value | O(n) | O(1) |
| Membership (`in`) | O(n) | O(1) |
| Remove Duplicates | O(n²) (manual) | O(n) |

---

# Interview Questions

## Why are set lookups approximately O(1)?

Because Python sets use a **hash table**. The hash of an element is calculated, allowing Python to jump directly to the element's location instead of scanning every item.

---

## Why is the worst-case complexity O(n)?

Because hash collisions can force Python to check multiple elements in the same bucket.

---

## Which is faster for searching: List or Set?

✅ **Set**

- List Search → **O(n)**
- Set Search → **O(1)**

---

# Summary Table

| Operation | Time Complexity |
|-----------|-----------------|
| Create | O(n) |
| Add | O(1) |
| Search | O(1) |
| Remove | O(1) |
| Discard | O(1) |
| Pop | O(1) |
| Clear | O(n) |
| Copy | O(n) |
| Union | O(n + m) |
| Intersection | O(min(n, m)) |
| Difference | O(n) |
| Symmetric Difference | O(n + m) |
| Subset | O(n) |
| Superset | O(n) |
| Iterate | O(n) |
| Convert List → Set | O(n) |
| Convert Set → List | O(n) |

---

# Key Takeaways

- ✅ Sets use a **Hash Table** internally.
- ✅ Most operations (`add`, `remove`, `search`) are **O(1)** on average.
- ✅ Set operations like **union**, **intersection**, and **difference** are highly efficient.
- ✅ Sets are much faster than lists for membership testing and duplicate removal.
- ⚠️ Worst-case performance can be **O(n)** due to hash collisions, but this is uncommon.