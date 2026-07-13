# 📘 Python Frozenset

## What is a Frozenset?

A **frozenset** is an **immutable (read-only)** version of a set.

- Stores **unique elements**
- Unordered
- No duplicate values
- Cannot be modified after creation
- Hashable (can be used as a dictionary key or inside another set)

---

# Syntax

```python
frozenset(iterable)
```

---

# Create a Frozenset

```python
numbers = frozenset([1, 2, 3, 4, 5])

print(numbers)
```

Output

```text
frozenset({1, 2, 3, 4, 5})
```

---

# Create from a Set

```python
numbers = {1, 2, 3}

frozen = frozenset(numbers)

print(frozen)
```

---

# Create an Empty Frozenset

```python
empty = frozenset()

print(empty)
```

Output

```text
frozenset()
```

---

# Remove Duplicates

```python
numbers = frozenset([1, 2, 2, 3, 4, 4])

print(numbers)
```

Output

```text
frozenset({1, 2, 3, 4})
```

---

# Access Elements

Frozensets are **unordered**, so indexing is not supported.

❌ Wrong

```python
numbers = frozenset({1, 2, 3})

print(numbers[0])
```

Output

```text
TypeError
```

---

# Iterate Through a Frozenset

```python
numbers = frozenset({1, 2, 3})

for num in numbers:
    print(num)
```

---

# Membership Testing

```python
numbers = frozenset({1, 2, 3})

print(2 in numbers)

print(5 not in numbers)
```

Output

```text
True
True
```

---

# Length

```python
numbers = frozenset({1, 2, 3})

print(len(numbers))
```

Output

```text
3
```

---

# Copy

```python
numbers = frozenset({1, 2, 3})

copy_numbers = numbers.copy()

print(copy_numbers)
```

Since frozensets are immutable, `copy()` simply returns the same frozenset.

---

# Supported Operations

Assume

```python
A = frozenset({1, 2, 3})

B = frozenset({3, 4, 5})
```

---

## Union

```python
print(A.union(B))
```

or

```python
print(A | B)
```

Output

```text
frozenset({1, 2, 3, 4, 5})
```

---

## Intersection

```python
print(A.intersection(B))
```

or

```python
print(A & B)
```

Output

```text
frozenset({3})
```

---

## Difference

```python
print(A.difference(B))
```

or

```python
print(A - B)
```

Output

```text
frozenset({1, 2})
```

---

## Symmetric Difference

```python
print(A.symmetric_difference(B))
```

or

```python
print(A ^ B)
```

Output

```text
frozenset({1, 2, 4, 5})
```

---

# Subset

```python
A = frozenset({1, 2})

B = frozenset({1, 2, 3})

print(A.issubset(B))
```

Output

```text
True
```

---

# Superset

```python
A = frozenset({1, 2, 3})

B = frozenset({1, 2})

print(A.issuperset(B))
```

Output

```text
True
```

---

# Disjoint

```python
A = frozenset({1, 2})

B = frozenset({3, 4})

print(A.isdisjoint(B))
```

Output

```text
True
```

---

# Methods NOT Supported

Since frozensets are immutable, these methods do **not** exist.

❌ `add()`

```python
numbers.add(5)
```

❌ `remove()`

```python
numbers.remove(2)
```

❌ `discard()`

```python
numbers.discard(2)
```

❌ `update()`

```python
numbers.update({4,5})
```

❌ `clear()`

```python
numbers.clear()
```

❌ `pop()`

```python
numbers.pop()
```

All of these will raise an **AttributeError**.

---

# Set vs Frozenset

| Feature | Set | Frozenset |
|---------|-----|-----------|
| Mutable | ✅ Yes | ❌ No |
| Ordered | ❌ No | ❌ No |
| Duplicate Values | ❌ No | ❌ No |
| Indexing | ❌ No | ❌ No |
| Hashable | ❌ No | ✅ Yes |
| Can be Dictionary Key | ❌ No | ✅ Yes |
| Can be Element of Another Set | ❌ No | ✅ Yes |

---

# When to Use Frozenset

Use a frozenset when:

- Data should never change.
- You need an immutable collection.
- You want to use a set as a dictionary key.
- You want to store a set inside another set.

---

# Example: Dictionary Key

```python
courses = {
    frozenset({"Python", "AI"}): "Semester 1"
}

print(courses)
```

Normal sets cannot be used as dictionary keys because they are mutable.

---

# Example: Set of Sets

❌ Wrong

```python
s = {
    {1, 2},
    {3, 4}
}
```

Output

```text
TypeError: unhashable type: 'set'
```

✅ Correct

```python
s = {
    frozenset({1, 2}),
    frozenset({3, 4})
}

print(s)
```

---

# Time Complexity

| Operation | Complexity |
|-----------|------------|
| Search (`in`) | O(1) |
| Union | O(n + m) |
| Intersection | O(min(n, m)) |
| Difference | O(n) |
| Symmetric Difference | O(n + m) |
| Subset | O(n) |
| Superset | O(n) |
| Iterate | O(n) |
| Length | O(1) |

---

# Interview Questions

### What is a frozenset?

A frozenset is an immutable version of a set.

---

### Can you modify a frozenset?

❌ No.

Once created, elements cannot be added, removed, or updated.

---

### Why use a frozenset?

Because it is **hashable**, so it can be used as:

- A dictionary key
- An element inside another set

---

# Memory Trick

```
Set
↓
Mutable
Can Add
Can Remove

Frozenset
↓
Immutable
Read Only
Hashable
```

---

# Summary

- ✅ Immutable version of a set.
- ✅ Stores unique values only.
- ✅ Unordered.
- ✅ No indexing.
- ✅ Supports union, intersection, difference, and subset operations.
- ❌ Cannot add, remove, or update elements.
- ✅ Hashable, so it can be used as a dictionary key or inside another set.