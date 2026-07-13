# 📘 Python Sets Notes

## What is a Set?

A **set** is an unordered, mutable collection of **unique** elements.

- Unordered (no indexing)
- Mutable (can add/remove items)
- No duplicate values
- Defined using `{}` or `set()`

---

# Creating Sets

```python
fruits = {"apple", "banana", "orange"}

print(fruits)
```

Output

```text
{'banana', 'apple', 'orange'}
```

> The order may be different every time because sets are unordered.

---

## Empty Set

```python
empty_set = set()
print(type(empty_set))
```

Output

```text
<class 'set'>
```

❌ Wrong

```python
empty = {}
```

Output

```text
<class 'dict'>
```

Because `{}` creates an empty dictionary, not a set.

---

# Duplicate Values

```python
numbers = {1, 2, 3, 2, 1, 4}

print(numbers)
```

Output

```text
{1, 2, 3, 4}
```

Duplicates are removed automatically.

---

# Different Data Types

```python
data = {1, "Python", 3.5, True}

print(data)
```

---

# Length

```python
fruits = {"apple", "banana", "orange"}

print(len(fruits))
```

Output

```text
3
```

---

# Accessing Elements

Sets do **not** support indexing.

❌ Wrong

```python
fruits = {"apple", "banana", "orange"}

print(fruits[0])
```

Output

```text
TypeError
```

---

## Iterate Through a Set

```python
fruits = {"apple", "banana", "orange"}

for fruit in fruits:
    print(fruit)
```

---

# Membership Operators

```python
fruits = {"apple", "banana", "orange"}

print("banana" in fruits)
print("grapes" not in fruits)
```

Output

```text
True
True
```

---

# Add Elements

```python
fruits = {"apple", "banana"}

fruits.add("orange")

print(fruits)
```

---

# Add Multiple Elements

```python
fruits = {"apple"}

fruits.update({"banana", "orange", "grapes"})

print(fruits)
```

---

# Remove Element

## remove()

```python
fruits.remove("banana")
```

Raises **KeyError** if element does not exist.

---

## discard()

```python
fruits.discard("banana")
```

Does **not** raise an error if element does not exist.

---

## pop()

```python
fruits.pop()
```

Removes a random element because sets are unordered.

---

## clear()

```python
fruits.clear()
```

Removes all elements.

---

# Delete Set

```python
del fruits
```

Deletes the entire set.

---

# Copy Set

```python
new_set = fruits.copy()
```

---

# Set Operations

Suppose

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```

---

## Union

Returns all unique elements.

```python
print(A | B)
print(A.union(B))
```

Output

```text
{1,2,3,4,5,6}
```

---

## Intersection

Returns common elements.

```python
print(A & B)
print(A.intersection(B))
```

Output

```text
{3,4}
```

---

## Difference

Elements in A but not in B.

```python
print(A - B)
print(A.difference(B))
```

Output

```text
{1,2}
```

---

## Symmetric Difference

Elements present in either set but not both.

```python
print(A ^ B)
print(A.symmetric_difference(B))
```

Output

```text
{1,2,5,6}
```

---

# Subset

```python
A = {1,2}
B = {1,2,3,4}

print(A.issubset(B))
```

Output

```text
True
```

---

# Superset

```python
B = {1,2,3,4}
A = {1,2}

print(B.issuperset(A))
```

Output

```text
True
```

---

# Disjoint Sets

```python
A = {1,2}
B = {3,4}

print(A.isdisjoint(B))
```

Output

```text
True
```

---

# Convert List to Set

```python
numbers = [1,2,2,3,3,4]

unique = set(numbers)

print(unique)
```

Output

```text
{1,2,3,4}
```

---

# Convert Set to List

```python
numbers = {1,2,3}

lst = list(numbers)

print(lst)
```

---

# Frozen Set

A **frozenset** is an immutable version of a set.

```python
numbers = frozenset({1,2,3})

print(numbers)
```

You cannot add or remove elements from a frozenset.

---

# Set Comprehension

```python
square = {x*x for x in range(1,6)}

print(square)
```

Output

```text
{1,4,9,16,25}
```

---

# Common Uses of Sets

- Remove duplicates
- Fast searching
- Membership testing
- Mathematical set operations
- Finding common elements
- Finding unique elements

---

# Time Complexity

| Operation | Complexity |
|-----------|------------|
| Add | O(1) |
| Remove | O(1) |
| Search (`in`) | O(1) |
| Delete | O(1) |
| Union | O(len(A)+len(B)) |
| Intersection | O(min(len(A), len(B))) |
| Difference | O(len(A)) |
| Symmetric Difference | O(len(A)+len(B)) |
| Iterate | O(n) |

---

# List vs Tuple vs Set vs Dictionary

| Feature | List | Tuple | Set | Dictionary |
|---------|------|-------|-----|------------|
| Ordered | ✅ | ✅ | ❌ | ✅ |
| Mutable | ✅ | ❌ | ✅ | ✅ |
| Duplicates | ✅ | ✅ | ❌ | Keys ❌ |
| Indexing | ✅ | ✅ | ❌ | By Key |
| Syntax | `[]` | `()` | `{}` | `{key:value}` |

---

# Summary

- Set stores **unique values only**.
- Sets are **unordered**.
- No indexing or slicing.
- Fast membership testing (`in`).
- Best for removing duplicates.
- Uses a **Hash Table**, so most operations are **O(1)**.
```