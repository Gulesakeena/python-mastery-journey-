# 🐍 Python `namedtuple`

> Complete beginner-friendly notes on `namedtuple` with examples, interview tips, and best practices.

---

# What is a `namedtuple`?

A **namedtuple** is a special type of tuple that gives **names to each element**.

Instead of accessing values using indexes:

```python
student = ("Ali", 20, "CS")

print(student[0])
```

You can access them by name:

```python
print(student.name)
```

This makes your code much more readable.

---

# Why Use `namedtuple`?

Normal tuple:

```python
student = ("Ali", 20, "CS")

print(student[1])
```

Question:

What does index `1` represent?

- Name?
- Age?
- Department?

Not obvious.

---

Using `namedtuple`:

```python
print(student.age)
```

Now the code is much easier to understand.

---

# Import

```python
from collections import namedtuple
```

---

# Syntax

```python
namedtuple("ClassName", ["field1", "field2", "field3"])
```

Example

```python
from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "department"])
```

---

# Creating an Object

```python
from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "department"])

student = Student("Ali", 20, "CS")

print(student)
```

Output

```
Student(name='Ali', age=20, department='CS')
```

---

# Access by Name

```python
print(student.name)
print(student.age)
print(student.department)
```

Output

```
Ali
20
CS
```

---

# Access by Index

Just like a normal tuple.

```python
print(student[0])
print(student[1])
```

Output

```
Ali
20
```

---

# Unpacking

```python
name, age, department = student

print(name)
print(age)
print(department)
```

Output

```
Ali
20
CS
```

---

# Iterate

```python
for value in student:
    print(value)
```

Output

```
Ali
20
CS
```

---

# Example 1: Employee

```python
from collections import namedtuple

Employee = namedtuple("Employee", ["id", "name", "salary"])

emp = Employee(101, "Sara", 75000)

print(emp.name)
print(emp.salary)
```

---

# Example 2: Book

```python
from collections import namedtuple

Book = namedtuple("Book", ["title", "author", "price"])

book = Book("Python", "Eric", 999)

print(book.title)
print(book.author)
```

---

# Example 3: Flight Booking

```python
from collections import namedtuple

Booking = namedtuple(
    "Booking",
    ["passenger", "flight", "seat"]
)

booking = Booking(
    "Ali",
    "PK101",
    "A10"
)

print(booking.passenger)
print(booking.flight)
print(booking.seat)
```

Output

```
Ali
PK101
A10
```

---

# Useful Methods

## `_make()`

Creates a namedtuple from a list or tuple.

```python
Student = namedtuple(
    "Student",
    ["name", "age"]
)

data = ["Ali", 20]

student = Student._make(data)

print(student)
```

Output

```
Student(name='Ali', age=20)
```

---

## `_asdict()`

Converts a namedtuple into a dictionary.

```python
print(student._asdict())
```

Output

```
{
'name': 'Ali',
'age': 20
}
```

---

## `_replace()`

Creates a new object with updated values.

```python
student = student._replace(age=21)

print(student)
```

Output

```
Student(name='Ali', age=21)
```

> Remember:
>
> `namedtuple` is immutable.
>
> `_replace()` returns a **new object**.

---

## `_fields`

Returns field names.

```python
print(Student._fields)
```

Output

```
('name', 'age')
```

---

# Immutability

Like tuples, namedtuples are immutable.

This is **not allowed**:

```python
student.age = 30
```

Output

```
AttributeError
```

---

# Comparing Tuples and NamedTuples

Tuple

```python
student = ("Ali", 20)
```

Access

```python
student[0]
```

NamedTuple

```python
student.name
```

Much easier to read.

---

# Tuple vs NamedTuple

| Feature | Tuple | NamedTuple |
|----------|-------|------------|
| Ordered | ✅ | ✅ |
| Immutable | ✅ | ✅ |
| Access by Index | ✅ | ✅ |
| Access by Name | ❌ | ✅ |
| Readability | Low | High |

---

# Advantages

- More readable code
- Easy to understand
- Immutable
- Faster than dictionaries
- Uses less memory than dictionaries
- Works like a tuple

---

# Limitations

- Cannot modify values
- Fixed number of fields
- Less flexible than classes

---

# Time Complexity

| Operation | Complexity |
|------------|------------|
| Access by name | O(1) |
| Access by index | O(1) |
| Iteration | O(n) |
| Unpacking | O(n) |

---

# Best Practices

- Use `namedtuple` when your data is fixed.
- Give meaningful field names.
- Use it instead of plain tuples for better readability.
- Use `_replace()` instead of trying to modify values.

---

# Interview Questions

## Difference between tuple and namedtuple?

- Tuple values are accessed using indexes.
- Namedtuple values can be accessed using field names.

---

## Is namedtuple mutable?

No.

It is immutable, just like a normal tuple.

---

## Can namedtuple be used as a dictionary key?

Yes.

Because it is immutable and hashable.

---

## Why use namedtuple instead of a dictionary?

- Less memory
- Faster access
- Immutable
- Cleaner syntax

---

# Summary

- `namedtuple` is available in the `collections` module.
- It behaves like a tuple but allows access using field names.
- It is immutable.
- Supports indexing, unpacking, iteration, and useful helper methods.
- Common helper methods:
  - `_make()`
  - `_asdict()`
  - `_replace()`
  - `_fields`

---

# Official Documentation

- Python Docs: https://docs.python.org/3/library/collections.html#collections.namedtuple
- W3Schools (Collections): https://www.w3schools.com/python/python_ref_module_collections.asp