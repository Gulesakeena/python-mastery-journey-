# 📘 Python Dictionary Methods Cheatsheet

A dictionary stores data in **key:value** pairs.

```python
student = {
    "id": 101,
    "name": "Ali",
    "cgpa": 3.8
}
```

---

# Create Dictionary

```python
student = {
    "id": 101,
    "name": "Ali"
}
```

---

# Access Value

```python
print(student["name"])
print(student.get("name"))
```

Output

```
Ali
Ali
```

---

# Add New Key

```python
student["department"] = "CS"
```

---

# Update Value

```python
student["cgpa"] = 3.9
```

---

# Remove Item

## pop()

```python
student.pop("cgpa")
```

Removes the key and returns its value.

---

## popitem()

```python
student.popitem()
```

Removes the last inserted item.

---

## del

```python
del student["name"]
```

Delete a specific key.

---

## clear()

```python
student.clear()
```

Removes all items.

---

# Copy Dictionary

```python
new_student = student.copy()
```

---

# Get Value

```python
student.get("name")
student.get("age")
student.get("age", 18)
```

---

# Get All Keys

```python
student.keys()
```

Output

```
dict_keys(['id', 'name'])
```

---

# Get All Values

```python
student.values()
```

---

# Get All Items

```python
student.items()
```

Output

```
dict_items([
('id',101),
('name','Ali')
])
```

---

# Update Dictionary

```python
student.update({"cgpa":3.8})
```

---

# Check Key

```python
print("name" in student)
print("age" not in student)
```

---

# Length

```python
len(student)
```

---

# Iterate Keys

```python
for key in student:
    print(key)
```

---

# Iterate Values

```python
for value in student.values():
    print(value)
```

---

# Iterate Keys & Values

```python
for key, value in student.items():
    print(key, value)
```

---

# Create From Keys

```python
keys = ["name", "age", "cgpa"]

student = dict.fromkeys(keys, None)

print(student)
```

Output

```python
{
'name':None,
'age':None,
'cgpa':None
}
```

---

# setdefault()

```python
student.setdefault("department", "CS")
```

Adds the key only if it does not already exist.

---

# Dictionary Constructor

```python
student = dict(
    name="Ali",
    age=20
)
```

---

# Common Operations

| Operation | Example |
|-----------|----------|
| Add | `d["city"]="Lahore"` |
| Update | `d["age"]=21` |
| Delete | `del d["age"]` |
| Search | `"name" in d` |
| Length | `len(d)` |
| Copy | `d.copy()` |
| Clear | `d.clear()` |

---

# Time Complexity

| Operation | Complexity |
|-----------|------------|
| Access | O(1) |
| Insert | O(1) |
| Update | O(1) |
| Delete | O(1) |
| Search Key | O(1) |
| Iterate | O(n) |

---

# Quick Tips

✅ Keys must be immutable.

✅ Values can be any data type.

✅ Duplicate keys are not allowed.

✅ Dictionaries preserve insertion order (Python 3.7+).

✅ Dictionary uses a Hash Table.