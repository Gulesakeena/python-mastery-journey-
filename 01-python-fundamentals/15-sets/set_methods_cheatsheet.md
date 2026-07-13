# 📘 Python Set Methods Cheatsheet

A **set** is an unordered collection of **unique** elements.

```python
fruits = {"apple", "banana", "orange"}
```

---

# add()

Adds a single element.

### Syntax

```python
set.add(element)
```

### Example

```python
fruits = {"apple", "banana"}

fruits.add("orange")

print(fruits)
```

---

# update()

Adds multiple elements from another iterable.

### Syntax

```python
set.update(iterable)
```

### Example

```python
fruits = {"apple"}

fruits.update(["banana", "orange"])

print(fruits)
```

Output

```text
{'apple', 'banana', 'orange'}
```

---

# remove()

Removes an element.

Raises **KeyError** if the element does not exist.

### Syntax

```python
set.remove(element)
```

### Example

```python
fruits = {"apple", "banana"}

fruits.remove("banana")

print(fruits)
```

---

# discard()

Removes an element if it exists.

Does **not** raise an error if the element is missing.

### Syntax

```python
set.discard(element)
```

### Example

```python
fruits = {"apple", "banana"}

fruits.discard("orange")

print(fruits)
```

---

# pop()

Removes and returns a random element.

Since sets are unordered, you cannot predict which element is removed.

### Syntax

```python
set.pop()
```

### Example

```python
fruits = {"apple", "banana", "orange"}

item = fruits.pop()

print(item)
print(fruits)
```

---

# clear()

Removes all elements.

### Syntax

```python
set.clear()
```

### Example

```python
fruits = {"apple", "banana"}

fruits.clear()

print(fruits)
```

Output

```text
set()
```

---

# copy()

Creates a shallow copy of the set.

### Syntax

```python
new_set = set.copy()
```

### Example

```python
fruits = {"apple", "banana"}

new_fruits = fruits.copy()

print(new_fruits)
```

---

# union()

Returns a new set containing all unique elements.

### Syntax

```python
set1.union(set2)
```

### Example

```python
A = {1,2,3}
B = {3,4,5}

print(A.union(B))
```

Output

```text
{1,2,3,4,5}
```

---

# intersection()

Returns common elements.

### Syntax

```python
set1.intersection(set2)
```

### Example

```python
A = {1,2,3}
B = {2,3,4}

print(A.intersection(B))
```

Output

```text
{2,3}
```

---

# difference()

Returns elements present in the first set but not the second.

### Syntax

```python
set1.difference(set2)
```

### Example

```python
A = {1,2,3}
B = {2,3,4}

print(A.difference(B))
```

Output

```text
{1}
```

---

# symmetric_difference()

Returns elements that exist in only one set.

### Syntax

```python
set1.symmetric_difference(set2)
```

### Example

```python
A = {1,2,3}
B = {2,3,4}

print(A.symmetric_difference(B))
```

Output

```text
{1,4}
```

---

# intersection_update()

Updates the original set with common elements.

### Syntax

```python
set1.intersection_update(set2)
```

### Example

```python
A = {1,2,3}
B = {2,3,4}

A.intersection_update(B)

print(A)
```

Output

```text
{2,3}
```

---

# difference_update()

Removes common elements from the original set.

### Syntax

```python
set1.difference_update(set2)
```

### Example

```python
A = {1,2,3}
B = {2,3}

A.difference_update(B)

print(A)
```

Output

```text
{1}
```

---

# symmetric_difference_update()

Updates the original set with symmetric difference.

### Syntax

```python
set1.symmetric_difference_update(set2)
```

### Example

```python
A = {1,2,3}
B = {2,3,4}

A.symmetric_difference_update(B)

print(A)
```

Output

```text
{1,4}
```

---

# issubset()

Checks whether every element of one set exists in another.

### Syntax

```python
set1.issubset(set2)
```

### Example

```python
A = {1,2}
B = {1,2,3}

print(A.issubset(B))
```

Output

```text
True
```

---

# issuperset()

Checks whether a set contains all elements of another set.

### Syntax

```python
set1.issuperset(set2)
```

### Example

```python
A = {1,2,3}
B = {1,2}

print(A.issuperset(B))
```

Output

```text
True
```

---

# isdisjoint()

Returns True if two sets have no common elements.

### Syntax

```python
set1.isdisjoint(set2)
```

### Example

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

# len()

Returns the number of elements.

```python
numbers = {1,2,3}

print(len(numbers))
```

Output

```text
3
```

---

# Membership

```python
fruits = {"apple", "banana"}

print("apple" in fruits)

print("orange" not in fruits)
```

Output

```text
True
True
```

---

# Loop Through a Set

```python
fruits = {"apple", "banana", "orange"}

for fruit in fruits:
    print(fruit)
```

---

# Convert List to Set

```python
numbers = [1,2,2,3,4,4]

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

# Quick Reference

| Method | Description |
|---------|-------------|
| `add()` | Add one element |
| `update()` | Add multiple elements |
| `remove()` | Remove element (error if missing) |
| `discard()` | Remove element (no error) |
| `pop()` | Remove random element |
| `clear()` | Remove all elements |
| `copy()` | Copy the set |
| `union()` | Combine sets |
| `intersection()` | Common elements |
| `difference()` | Elements only in first set |
| `symmetric_difference()` | Elements not common |
| `intersection_update()` | Update with common elements |
| `difference_update()` | Remove common elements |
| `symmetric_difference_update()` | Update with symmetric difference |
| `issubset()` | Check subset |
| `issuperset()` | Check superset |
| `isdisjoint()` | Check no common elements |

---

# Time Complexity

| Operation | Complexity |
|-----------|------------|
| Add | O(1) |
| Remove | O(1) |
| Search (`in`) | O(1) |
| Union | O(n + m) |
| Intersection | O(min(n, m)) |
| Difference | O(n) |
| Symmetric Difference | O(n + m) |
| Iterate | O(n) |

---

# Tips

- ✅ Sets store **unique values only**.
- ✅ Sets are **unordered**, so no indexing or slicing.
- ✅ Membership testing (`in`) is very fast.
- ✅ Best for removing duplicates and performing mathematical set operations.
- ✅ Most set operations are based on **hash tables**, making them efficient.