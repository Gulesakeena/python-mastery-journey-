# Python Data Types Notes

## What is a Data Type?

A **data type** defines the kind of value a variable can store. Every value in Python belongs to a specific data type, which determines what operations can be performed on it.

Example:

```python
name = "Gule"      # String
age = 21           # Integer
height = 5.8       # Float
is_student = True  # Boolean
```

---

# Why Are Data Types Important?

Data types help Python:

* Store data efficiently.
* Perform valid operations.
* Prevent invalid operations.
* Manage memory correctly.

---

# Built-in Python Data Types

Python provides several built-in data types.

| Data Type  | Description                   | Example                |
| ---------- | ----------------------------- | ---------------------- |
| int        | Whole numbers                 | `10`                   |
| float      | Decimal numbers               | `3.14`                 |
| complex    | Complex numbers               | `2 + 3j`               |
| str        | Text/String                   | `"Hello"`              |
| bool       | True or False                 | `True`                 |
| list       | Ordered, mutable collection   | `[1, 2, 3]`            |
| tuple      | Ordered, immutable collection | `(1, 2, 3)`            |
| range      | Sequence of numbers           | `range(5)`             |
| dict       | Key-value pairs               | `{"name": "Gule"}`     |
| set        | Unordered unique values       | `{1, 2, 3}`            |
| frozenset  | Immutable set                 | `frozenset({1,2,3})`   |
| bytes      | Immutable binary data         | `b"Hello"`             |
| bytearray  | Mutable binary data           | `bytearray(5)`         |
| memoryview | Memory view object            | `memoryview(bytes(5))` |
| NoneType   | Represents no value           | `None`                 |

---

# Numeric Data Types

## Integer (`int`)

Stores whole numbers.

```python
age = 21
marks = 95
temperature = -10
```

---

## Float (`float`)

Stores decimal numbers.

```python
price = 99.99
height = 5.8
pi = 3.14159
```

---

## Complex (`complex`)

Stores complex numbers.

```python
number = 2 + 3j
```

---

# String (`str`)

A **string** is a sequence of characters enclosed in single, double, or triple quotes.

```python
name = "Gule"
city = 'Sialkot'
message = """Hello World"""
```

---

# Boolean (`bool`)

Stores only two values:

* `True`
* `False`

```python
is_logged_in = True
is_admin = False
```

---

# Sequence Data Types

## List (`list`)

An ordered and **mutable** collection.

```python
fruits = ["Apple", "Banana", "Mango"]
```

Properties:

* Ordered
* Mutable
* Allows duplicates

---

## Tuple (`tuple`)

An ordered and **immutable** collection.

```python
coordinates = (10, 20)
```

Properties:

* Ordered
* Immutable
* Allows duplicates

---

## Range (`range`)

Represents a sequence of numbers.

```python
numbers = range(5)
```

Produces:

```text
0 1 2 3 4
```

---

# Mapping Data Type

## Dictionary (`dict`)

Stores data as **key-value pairs**.

```python
student = {
    "name": "Gule",
    "age": 21
}
```

Properties:

* Ordered
* Mutable
* Keys are unique

---

# Set Data Types

## Set (`set`)

An unordered collection of unique values.

```python
numbers = {1, 2, 3, 4}
```

Properties:

* Unordered
* Mutable
* No duplicate values

---

## Frozen Set (`frozenset`)

An immutable version of a set.

```python
numbers = frozenset({1, 2, 3})
```

---

# Binary Data Types

## Bytes

Immutable binary data.

```python
data = b"Hello"
```

---

## Bytearray

Mutable binary data.

```python
data = bytearray(5)
```

---

## Memoryview

Provides direct access to binary object's memory.

```python
data = memoryview(bytes(5))
```

---

# None Data Type

`None` represents the absence of a value.

```python
value = None
```

---

# Check the Data Type

Use the `type()` function.

```python
name = "Gule"
print(type(name))
```

Output:

```python
<class 'str'>
```

More examples:

```python
print(type(10))         # int
print(type(3.14))       # float
print(type(True))       # bool
print(type([1, 2]))     # list
print(type((1, 2)))     # tuple
print(type({"a": 1}))   # dict
print(type({1, 2}))     # set
print(type(None))       # NoneType
```

---

# Mutable vs Immutable

## Mutable Data Types

Their values **can be changed** after creation.

* list
* dict
* set
* bytearray

Example:

```python
numbers = [1, 2, 3]
numbers.append(4)
```

---

## Immutable Data Types

Their values **cannot be changed** after creation.

* int
* float
* complex
* bool
* str
* tuple
* bytes
* frozenset
* range
* NoneType

Example:

```python
name = "Gule"

# Creates a new string instead of modifying the old one
name = "Huzaifa"
```

---

# Type Conversion

Python allows conversion from one data type to another.

```python
age = "21"

print(int(age))
print(float(age))
print(str(21))
print(bool(1))
print(list((1, 2, 3)))
```


# Python Data Types Comparison

| Data Type    |            Mutable           |      Ordered      |       Allows Duplicates      |    Indexed   |
| ------------ | :--------------------------: | :---------------: | :--------------------------: | :----------: |
| `int`        |               ❌              |        N/A        |              N/A             |       ❌      |
| `float`      |               ❌              |        N/A        |              N/A             |       ❌      |
| `complex`    |               ❌              |        N/A        |              N/A             |       ❌      |
| `bool`       |               ❌              |        N/A        |              N/A             |       ❌      |
| `str`        |               ❌              |         ✅         |               ✅              |       ✅      |
| `list`       |               ✅              |         ✅         |               ✅              |       ✅      |
| `tuple`      |               ❌              |         ✅         |               ✅              |       ✅      |
| `range`      |               ❌              |         ✅         |               ❌              |       ✅      |
| `dict`       |               ✅              | ✅ *(Python 3.7+)* | **Keys:** ❌<br>**Values:** ✅ | ✅ *(by key)* |
| `set`        |               ✅              |         ❌         |               ❌              |       ❌      |
| `frozenset`  |               ❌              |         ❌         |               ❌              |       ❌      |
| `bytes`      |               ❌              |         ✅         |               ✅              |       ✅      |
| `bytearray`  |               ✅              |         ✅         |               ✅              |       ✅      |
| `memoryview` | Depends on underlying object |         ✅         |               ✅              |       ✅      |
| `NoneType`   |               ❌              |        N/A        |              N/A             |       ❌      |

---

## Legend

* ✅ = Yes
* ❌ = No
* N/A = Not Applicable

---

## Quick Summary

| Feature                     | Data Types                                                                                                            |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Mutable**                 | `list`, `dict`, `set`, `bytearray`                                                                                    |
| **Immutable**               | `int`, `float`, `complex`, `bool`, `str`, `tuple`, `range`, `bytes`, `frozenset`, `NoneType`                          |
| **Ordered**                 | `str`, `list`, `tuple`, `range`, `dict`, `bytes`, `bytearray`, `memoryview`                                           |
| **Unordered**               | `set`, `frozenset`                                                                                                    |
| **Allow Duplicates**        | `str`, `list`, `tuple`, `bytes`, `bytearray`, `memoryview`, `dict` *(values only)*                                    |
| **Do Not Allow Duplicates** | `set`, `frozenset`, `range`, `dict` *(keys only)*                                                                     |
| **Support Indexing**        | `str`, `list`, `tuple`, `range`, `bytes`, `bytearray`, `memoryview`                                                   |
| **Do Not Support Indexing** | `int`, `float`, `complex`, `bool`, `set`, `frozenset`, `NoneType` *(dictionary uses keys instead of numeric indexes)* |


---

# Best Practices

* Choose the appropriate data type for your data.
* Use `type()` to verify a variable's data type.
* Use meaningful variable names.
* Prefer immutable data types when values should not change.
* Use lists when data needs modification.
* Use tuples for fixed collections.
* Use dictionaries for key-value relationships.
* Use sets when unique values are required.

---

# Summary

* Python has **15 built-in data types**.
* Every value belongs to a specific data type.
* Data types determine how data is stored and manipulated.
* Use `type()` to check a value's data type.
* Understand the difference between **mutable** and **immutable** data types, as it is a common interview question.
