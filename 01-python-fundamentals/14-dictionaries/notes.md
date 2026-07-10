# 📘 Python Dictionaries (`dict`) - Complete Notes

> Beginner to Advanced Notes on Python Dictionaries with examples, best practices, interview tips, and time complexity.

---

# What is a Dictionary?

A **dictionary** is a built-in Python data type used to store data in **key-value pairs**.

Think of it like a real dictionary:

```
Word  → Meaning
```

Python Dictionary:

```
Key → Value
```

Example:

```python
student = {
    "name": "Ali",
    "age": 20,
    "department": "CS"
}
```

Here:

- `"name"` is the key
- `"Ali"` is the value

---

# Why Use Dictionaries?

Suppose you store student information in a tuple.

```python
student = ("Ali", 20, "CS")
```

To get the age:

```python
print(student[1])
```

You must remember index `1`.

With a dictionary:

```python
student = {
    "name": "Ali",
    "age": 20
}

print(student["age"])
```

Much easier to read.

---

# Creating a Dictionary

```python
student = {
    "name": "Ali",
    "age": 20,
    "city": "Lahore"
}

print(student)
```

Output

```
{'name': 'Ali', 'age': 20, 'city': 'Lahore'}
```

---

# Dictionary Properties

- Mutable ✅
- Ordered (Python 3.7+) ✅
- Stores key-value pairs ✅
- No duplicate keys ✅
- Values can be duplicated ✅

---

# Accessing Values

```python
student = {
    "name": "Ali",
    "age": 20
}

print(student["name"])
```

Output

```
Ali
```

---

# Using get()

```python
print(student.get("age"))
```

Output

```
20
```

If key does not exist:

```python
print(student.get("marks"))
```

Output

```
None
```

With default value:

```python
print(student.get("marks", 0))
```

Output

```
0
```

---

# Adding New Items

```python
student["city"] = "Karachi"

print(student)
```

---

# Updating Values

```python
student["age"] = 21

print(student)
```

---

# Removing Items

## pop()

```python
student.pop("age")
```

Removes the given key.

---

## popitem()

```python
student.popitem()
```

Removes the last inserted key-value pair.

---

## del

```python
del student["city"]
```

---

## clear()

```python
student.clear()
```

Removes all items.

---

# Looping Through Dictionary

## Keys

```python
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

# Dictionary Length

```python
print(len(student))
```

---

# Membership

```python
print("name" in student)
```

Output

```
True
```

---

# Copy Dictionary

```python
new_student = student.copy()
```

---

# Nested Dictionary

```python
students = {
    "student1": {
        "name": "Ali",
        "age": 20
    },
    "student2": {
        "name": "Sara",
        "age": 21
    }
}
```

Access

```python
print(students["student1"]["name"])
```

Output

```
Ali
```

---

# Dictionary with Different Data Types

```python
person = {
    "name": "Ali",
    "age": 20,
    "is_student": True,
    "marks": [80, 90, 85]
}
```

---

# Dictionary Comprehension

```python
squares = {
    x: x*x
    for x in range(1,6)
}

print(squares)
```

Output

```
{1:1, 2:4, 3:9, 4:16, 5:25}
```

---

# Common Dictionary Methods

| Method | Description |
|---------|-------------|
| `get()` | Returns value of key |
| `keys()` | Returns all keys |
| `values()` | Returns all values |
| `items()` | Returns key-value pairs |
| `update()` | Updates dictionary |
| `pop()` | Removes a key |
| `popitem()` | Removes last item |
| `clear()` | Removes all items |
| `copy()` | Copies dictionary |
| `setdefault()` | Returns value or inserts default |

---

# keys()

```python
student.keys()
```

Output

```
dict_keys(['name', 'age'])
```

---

# values()

```python
student.values()
```

Output

```
dict_values(['Ali', 20])
```

---

# items()

```python
student.items()
```

Output

```
dict_items([('name', 'Ali'), ('age', 20)])
```

---

# update()

```python
student.update({
    "age": 21,
    "city": "Lahore"
})
```

---

# setdefault()

If key exists:

```python
student.setdefault("age", 18)
```

Returns existing value.

If key does not exist:

```python
student.setdefault("marks", 0)
```

Adds new key.

---

# Difference Between [] and get()

Using `[]`

```python
student["marks"]
```

If key doesn't exist:

```
KeyError
```

Using `get()`

```python
student.get("marks")
```

Output

```
None
```

---

# Dictionary vs List

| List | Dictionary |
|------|------------|
| Uses indexes | Uses keys |
| Ordered | Ordered |
| Duplicate values | Duplicate values |
| Slower search | Faster search |

---

# Dictionary vs Tuple

| Tuple | Dictionary |
|--------|------------|
| Uses indexes | Uses keys |
| Immutable | Mutable |
| Ordered | Ordered |

---

# Time Complexity

| Operation | Complexity |
|------------|------------|
| Access by key | O(1) |
| Insert | O(1) |
| Update | O(1) |
| Delete | O(1) |
| Search key | O(1) |
| Iterate | O(n) |
| Copy | O(n) |
| clear() | O(n) |

> **Note:** These are average-case complexities. In rare cases with many hash collisions, operations can be slower.

---

# Interview Questions

## Why are dictionary keys unique?

Because each key must uniquely identify one value.

---

## Can dictionary values be duplicated?

Yes.

```python
{
    "a": 10,
    "b": 10
}
```

Valid.

---

## Can dictionary keys be duplicated?

No.

```python
{
    "age": 20,
    "age": 30
}
```

Output

```
{'age': 30}
```

The last value overwrites the previous one.

---

## Can a list be a dictionary key?

❌ No

Lists are mutable.

---

## Can a tuple be a dictionary key?

✅ Yes

If the tuple contains only immutable elements.

---

## Why are dictionaries fast?

Because they use a **hash table**, allowing average O(1) access, insertion, and deletion.

---

# Best Practices

- Use meaningful keys.
- Prefer `get()` when a key may not exist.
- Use `items()` when you need both keys and values.
- Use dictionary comprehension for concise code.
- Avoid duplicate keys.

---

# Summary

- Dictionary stores **key-value pairs**.
- Keys are unique.
- Values can repeat.
- Dictionaries are mutable.
- Access values using keys.
- Average lookup, insertion, and deletion are **O(1)**.
- One of the most commonly used data structures in Python.