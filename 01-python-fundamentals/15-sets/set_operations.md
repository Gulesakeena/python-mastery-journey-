# 📘 Python Set Operations

Set operations allow you to compare, combine, and manipulate sets just like in mathematics.

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```

---

# 1. Union ( | )

Returns **all unique elements** from both sets.

### Syntax

```python
A.union(B)
```

or

```python
A | B
```

### Example

```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))
print(A | B)
```

### Output

```text
{1, 2, 3, 4, 5}
```

### Time Complexity

```
O(len(A) + len(B))
```

---

# 2. Intersection ( & )

Returns **only common elements**.

### Syntax

```python
A.intersection(B)
```

or

```python
A & B
```

### Example

```python
A = {1, 2, 3}
B = {2, 3, 4}

print(A.intersection(B))
print(A & B)
```

### Output

```text
{2, 3}
```

### Time Complexity

```
O(min(len(A), len(B)))
```

---

# 3. Difference ( - )

Returns elements that are in the **first set but not in the second**.

### Syntax

```python
A.difference(B)
```

or

```python
A - B
```

### Example

```python
A = {1, 2, 3}
B = {2, 3, 4}

print(A.difference(B))
print(A - B)
```

### Output

```text
{1}
```

---

Difference in the opposite direction:

```python
print(B - A)
```

Output

```text
{4}
```

### Time Complexity

```
O(len(A))
```

---

# 4. Symmetric Difference ( ^ )

Returns elements that are in **either set but not in both**.

### Syntax

```python
A.symmetric_difference(B)
```

or

```python
A ^ B
```

### Example

```python
A = {1, 2, 3}
B = {2, 3, 4}

print(A.symmetric_difference(B))
print(A ^ B)
```

### Output

```text
{1, 4}
```

### Time Complexity

```
O(len(A) + len(B))
```

---

# 5. Subset

Checks whether every element of one set exists in another.

### Syntax

```python
A.issubset(B)
```

or

```python
A <= B
```

### Example

```python
A = {1, 2}
B = {1, 2, 3, 4}

print(A.issubset(B))
print(A <= B)
```

### Output

```text
True
```

---

# 6. Proper Subset

Checks if A is a subset of B **and not equal** to B.

### Syntax

```python
A < B
```

### Example

```python
A = {1, 2}
B = {1, 2, 3}

print(A < B)
```

### Output

```text
True
```

---

# 7. Superset

Checks whether a set contains all elements of another set.

### Syntax

```python
A.issuperset(B)
```

or

```python
A >= B
```

### Example

```python
A = {1, 2, 3, 4}
B = {1, 2}

print(A.issuperset(B))
print(A >= B)
```

### Output

```text
True
```

---

# 8. Proper Superset

Checks if A is a superset of B and they are not equal.

### Syntax

```python
A > B
```

### Example

```python
A = {1, 2, 3}

B = {1, 2}

print(A > B)
```

### Output

```text
True
```

---

# 9. Disjoint Sets

Returns **True** if two sets have **no common elements**.

### Syntax

```python
A.isdisjoint(B)
```

### Example

```python
A = {1, 2}
B = {3, 4}

print(A.isdisjoint(B))
```

### Output

```text
True
```

---

Example with common elements:

```python
A = {1, 2, 3}
B = {3, 4}

print(A.isdisjoint(B))
```

Output

```text
False
```

---

# 10. Intersection Update

Keeps only common elements in the original set.

### Example

```python
A = {1, 2, 3}
B = {2, 3, 4}

A.intersection_update(B)

print(A)
```

Output

```text
{2, 3}
```

---

# 11. Difference Update

Removes common elements from the original set.

### Example

```python
A = {1, 2, 3}
B = {2, 3}

A.difference_update(B)

print(A)
```

Output

```text
{1}
```

---

# 12. Symmetric Difference Update

Updates the original set with elements that are not common.

### Example

```python
A = {1, 2, 3}
B = {2, 3, 4}

A.symmetric_difference_update(B)

print(A)
```

Output

```text
{1, 4}
```

---

# Real-Life Examples

## Remove Duplicates

```python
numbers = [1, 2, 2, 3, 4, 4]

unique = set(numbers)

print(unique)
```

---

## Find Common Subjects

```python
student1 = {"Math", "Physics", "English"}
student2 = {"Physics", "Chemistry", "Math"}

print(student1 & student2)
```

Output

```text
{'Math', 'Physics'}
```

---

## Find Different Subjects

```python
print(student1 - student2)
```

Output

```text
{'English'}
```

---

## Merge Two Lists Without Duplicates

```python
list1 = [1, 2, 3]
list2 = [3, 4, 5]

result = list(set(list1) | set(list2))

print(result)
```

---

## Check Permissions

```python
required = {"read", "write"}
user = {"read", "write", "delete"}

print(required <= user)
```

Output

```text
True
```

---

# Mathematical Representation

```
Union                  A ∪ B

Intersection           A ∩ B

Difference             A − B

Symmetric Difference   A △ B

Subset                 A ⊆ B

Superset               A ⊇ B
```

---

# Time Complexity

| Operation | Method | Complexity |
|-----------|--------|------------|
| Union | `A | B` | O(n + m) |
| Intersection | `A & B` | O(min(n, m)) |
| Difference | `A - B` | O(n) |
| Symmetric Difference | `A ^ B` | O(n + m) |
| Subset | `A <= B` | O(len(A)) |
| Superset | `A >= B` | O(len(B)) |
| Disjoint | `isdisjoint()` | O(min(n, m)) |

---

# Quick Comparison

| Operator | Method | Meaning |
|----------|--------|---------|
| `|` | `union()` | All unique elements |
| `&` | `intersection()` | Common elements |
| `-` | `difference()` | Elements in first set only |
| `^` | `symmetric_difference()` | Elements not common |
| `<=` | `issubset()` | Is subset? |
| `>=` | `issuperset()` | Is superset? |
| `<` | Proper subset | Subset but not equal |
| `>` | Proper superset | Superset but not equal |

---

# Interview Tips

✅ Use **Union** to combine sets without duplicates.

✅ Use **Intersection** to find common elements.

✅ Use **Difference** to find missing elements.

✅ Use **Symmetric Difference** to find unique elements from both sets.

✅ Use **Subset/Superset** to compare relationships between sets.

✅ Sets use **hash tables**, making membership tests and most operations very fast.