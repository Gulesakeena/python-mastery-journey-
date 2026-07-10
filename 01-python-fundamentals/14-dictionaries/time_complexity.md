# 📘 Dictionary Time Complexity

Python dictionaries use a **Hash Table**.

Average-case operations are very fast.

---

# Time Complexity Table

| Operation | Complexity |
|-----------|------------|
| Access `d[key]` | O(1) |
| Insert | O(1) |
| Update | O(1) |
| Delete | O(1) |
| Search Key | O(1) |
| Check `in` | O(1) |
| `get()` | O(1) |
| `pop()` | O(1) |
| `len()` | O(1) |
| Iterate | O(n) |
| Copy | O(n) |
| Clear | O(n) |
| `keys()` | O(1) |
| `values()` | O(1) |
| `items()` | O(1) |
| Sort Keys | O(n log n) |
| Sort Values | O(n log n) |

---

# Why O(1)?

Python computes the **hash** of a key and directly jumps to its memory location instead of checking every item one by one.

Example:

```python
student = {
    "name":"Ali",
    "age":20
}

print(student["age"])
```

Python:

1. Computes hash("age")
2. Finds the correct bucket
3. Returns the value

No full scan is required.

---

# Worst Case

Sometimes two keys produce the same hash value.

This is called a **Hash Collision**.

In rare cases:

| Operation | Worst Case |
|-----------|------------|
| Search | O(n) |
| Insert | O(n) |
| Delete | O(n) |

Python minimizes collisions, so average performance remains **O(1)**.

---

# Dictionary vs List

| Operation | List | Dictionary |
|-----------|------|------------|
| Search | O(n) | O(1) |
| Insert End | O(1) | O(1) |
| Delete by Key | ❌ | O(1) |
| Access by Index/Key | O(1) | O(1) |

---

# Interview Questions

### Why are dictionaries fast?

Because they use a **Hash Table**.

---

### Why are dictionary lookups approximately O(1)?

Python computes the hash of the key and directly accesses the corresponding memory location instead of scanning all elements.

---

### What is a Hash Collision?

A hash collision occurs when two different keys generate the same hash value.

---

# Memory Trick

| Data Structure | Search |
|---------------|--------|
| List | O(n) |
| Tuple | O(n) |
| Set | O(1) |
| Dictionary | O(1) |

**Remember:**

- **List → Linear Search → O(n)**
- **Dictionary → Hash Table → O(1)**
- **Set → Hash Table → O(1)**