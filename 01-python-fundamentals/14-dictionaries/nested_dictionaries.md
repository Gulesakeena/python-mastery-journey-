# 📘 Nested Dictionaries in Python

A nested dictionary is a dictionary inside another dictionary.

---

# Syntax

```python
students = {
    101: {
        "name": "Ali",
        "cgpa": 3.8
    },
    102: {
        "name": "Sara",
        "cgpa": 3.9
    }
}
```

---

# Access Data

```python
print(students[101]["name"])
```

Output

```
Ali
```

---

# Access CGPA

```python
print(students[102]["cgpa"])
```

---

# Add New Student

```python
students[103] = {
    "name":"Ahmed",
    "cgpa":3.6
}
```

---

# Update

```python
students[101]["cgpa"] = 4.0
```

---

# Delete Student

```python
del students[102]
```

---

# Loop Through Nested Dictionary

```python
for id, info in students.items():
    print(id, info)
```

---

# Access Every Value

```python
for id, info in students.items():
    print(info["name"])
    print(info["cgpa"])
```

---

# Real Example

```python
library = {
    1:{
        "title":"Python",
        "author":"ABC"
    },
    2:{
        "title":"AI",
        "author":"XYZ"
    }
}
```

---

# Common Use Cases

- Student Management System
- Library Management System
- Employee Records
- Hospital Records
- Banking System
- Product Inventory

---

# Complexity

| Operation | Complexity |
|-----------|------------|
| Access | O(1) |
| Insert | O(1) |
| Update | O(1) |
| Delete | O(1) |
| Traversal | O(n) |

---

# Tips

- Outer dictionary stores records.
- Inner dictionary stores details.
- Access using multiple keys.