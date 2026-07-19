# 19 - Python Arrays

## Learning Objectives

After completing this topic, you should be able to:

- Understand what an array is.
- Know the difference between Python Lists and Arrays.
- Create arrays using the `array` module.
- Access, modify, insert, and delete elements.
- Use common array methods.
- Know when to use arrays instead of lists.

---

# What is an Array?

An array is a collection of elements stored in contiguous memory locations.

Unlike Python lists, arrays can only store elements of the **same data type**.

Example:

```
[10, 20, 30, 40, 50]
```

---

# Python Lists vs Arrays

| Feature | List | Array |
|---------|------|-------|
| Built-in | ✅ Yes | ❌ No (`array` module) |
| Mixed Data Types | ✅ Yes | ❌ No |
| Dynamic Size | ✅ Yes | ✅ Yes |
| Faster for Numeric Data | ❌ | ✅ |
| Most Common in Python | ✅ | ❌ |

---

# Importing the array Module

```python
from array import array
```

---

# Creating an Array

```python
numbers = array('i', [10, 20, 30])
```

The first argument is the **type code**.

---

# Common Type Codes

| Code | Type |
|------|------|
| i | Integer |
| f | Float |
| d | Double |
| b | Signed Integer |
| u | Unicode Character |

---

# Accessing Elements

```python
numbers[0]
numbers[1]
numbers[-1]
```

---

# Modifying Elements

```python
numbers[1] = 100
```

---

# Traversing an Array

```python
for num in numbers:
    print(num)
```

---

# Common Methods

- append()
- insert()
- pop()
- remove()
- reverse()
- extend()
- index()
- count()

---

# When Should You Use Arrays?

Use arrays when:

- All values have the same type.
- Working with numeric data.
- Memory efficiency matters.

Otherwise, use **lists**.

---

# Interview Questions

### Q1. Why are Python lists used more often than arrays?

Because lists are more flexible and can store multiple data types.

---

### Q2. Can an array store strings and integers together?

No.

---

### Q3. Which module provides arrays?

```
array
```

---

### Q4. Which data structure is preferred in Python?

Lists.

---

# Time Complexity

| Operation | Complexity |
|-----------|------------|
| Access | O(1) |
| Update | O(1) |
| Search | O(n) |
| Insert | O(n) |
| Delete | O(n) |

---

# Key Takeaways

- Arrays store one data type only.
- Lists are preferred in Python.
- Arrays come from the `array` module.
- Arrays are mainly used for numeric data.