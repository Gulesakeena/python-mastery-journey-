# 🐍 Python Tuples (`tuple`)

> Complete notes on Python Tuples for beginners and interview preparation.

---

# What is a Tuple?

A **tuple** is an ordered, immutable collection in Python.

- Ordered ✅
- Immutable (cannot be changed) ✅
- Allows duplicate values ✅
- Can store different data types ✅
- Supports indexing and slicing ✅

Example:

```python
fruits = ("apple", "banana", "mango")

print(fruits)
```

Output

```
('apple', 'banana', 'mango')
```

---

# Why Use Tuples?

Use tuples when:

- Data should never change.
- You want faster read operations.
- You want to use data as dictionary keys.
- You want to return multiple values from a function.

---

# Creating Tuples

## Empty Tuple

```python
t = ()

print(t)
```

Output

```
()
```

---

## Tuple with Values

```python
numbers = (1, 2, 3, 4)

print(numbers)
```

---

## Mixed Data Types

```python
data = ("Python", 3.14, True, 100)

print(data)
```

---

## Single Element Tuple

❌ Wrong

```python
t = (10)

print(type(t))
```

Output

```
<class 'int'>
```

✅ Correct

```python
t = (10,)

print(type(t))
```

Output

```
<class 'tuple'>
```

> **Remember:** A single-element tuple **must** have a trailing comma.

---

# Tuple Without Parentheses

```python
numbers = 1, 2, 3

print(numbers)
```

Output

```
(1, 2, 3)
```

---

# tuple() Constructor

```python
numbers = tuple([1, 2, 3])

print(numbers)
```

Output

```
(1, 2, 3)
```

---

# Accessing Elements

## Positive Indexing

```python
fruits = ("apple", "banana", "mango")

print(fruits[0])
```

Output

```
apple
```

---

## Negative Indexing

```python
print(fruits[-1])
```

Output

```
mango
```

---

# Slicing

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
```

Output

```
(20, 30, 40)
```

---

```python
print(numbers[:3])
```

Output

```
(10, 20, 30)
```

---

```python
print(numbers[2:])
```

Output

```
(30, 40, 50)
```

---

```python
print(numbers[::-1])
```

Output

```
(50, 40, 30, 20, 10)
```

---

# Tuple is Immutable

❌ Not Allowed

```python
numbers = (1, 2, 3)

numbers[0] = 10
```

Output

```
TypeError
```

Reason:

Tuples cannot be modified after creation.

---

# Loop Through Tuple

```python
numbers = (1, 2, 3)

for num in numbers:
    print(num)
```

---

Using index

```python
for i in range(len(numbers)):
    print(numbers[i])
```

---

# Membership

```python
fruits = ("apple", "banana")

print("apple" in fruits)
```

Output

```
True
```

---

```python
print("orange" not in fruits)
```

Output

```
True
```

---

# Tuple Length

```python
numbers = (1, 2, 3)

print(len(numbers))
```

Output

```
3
```

---

# Tuple Concatenation

```python
a = (1, 2)

b = (3, 4)

print(a + b)
```

Output

```
(1, 2, 3, 4)
```

---

# Tuple Repetition

```python
print((1, 2) * 3)
```

Output

```
(1, 2, 1, 2, 1, 2)
```

---

# Tuple Packing

```python
person = ("Ali", 21, "Lahore")
```

This is called **packing**.

---

# Tuple Unpacking

```python
person = ("Ali", 21, "Lahore")

name, age, city = person

print(name)
print(age)
print(city)
```

Output

```
Ali
21
Lahore
```

---

# Extended Unpacking

```python
numbers = (1, 2, 3, 4, 5)

first, *middle, last = numbers

print(first)
print(middle)
print(last)
```

Output

```
1
[2, 3, 4]
5
```

---

# Nested Tuples

```python
students = (
    ("Ali", 20),
    ("Sara", 21)
)

print(students[0])
```

Output

```
('Ali', 20)
```

---

Access nested value

```python
print(students[0][1])
```

Output

```
20
```

---

# Built-in Functions

```python
numbers = (5, 2, 8, 1)

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers))
```

Output

```
4
8
1
16
[1, 2, 5, 8]
```

> **Note:** `sorted()` returns a **list**, not a tuple.

---

# Tuple Methods

Tuples have only **two methods**.

---

## count()

Counts occurrences.

```python
numbers = (1, 2, 2, 3, 2)

print(numbers.count(2))
```

Output

```
3
```

Time Complexity

```
O(n)
```

---

## index()

Returns first occurrence index.

```python
numbers = (10, 20, 30)

print(numbers.index(20))
```

Output

```
1
```

Raises

```
ValueError
```

if not found.

Time Complexity

```
O(n)
```

---

# Converting Between List and Tuple

Tuple → List

```python
numbers = (1, 2, 3)

lst = list(numbers)

print(lst)
```

---

List → Tuple

```python
numbers = [1, 2, 3]

t = tuple(numbers)

print(t)
```

---

# Copying a Tuple

Tuples are immutable.

```python
t1 = (1, 2, 3)

t2 = t1
```

This is safe because the tuple cannot change.

---

# Deleting a Tuple

```python
numbers = (1, 2, 3)

del numbers
```

---

# Common Errors

## TypeError

```python
numbers = (1, 2, 3)

numbers[0] = 10
```

---

## ValueError

```python
numbers = (1, 2, 3)

numbers.index(100)
```

---

# Tuple vs List

| Feature | Tuple | List |
|---------|-------|------|
| Mutable | ❌ No | ✅ Yes |
| Ordered | ✅ Yes | ✅ Yes |
| Duplicates | ✅ Yes | ✅ Yes |
| Indexing | ✅ Yes | ✅ Yes |
| Slicing | ✅ Yes | ✅ Yes |
| Methods | 2 | Many |
| Faster | ✅ Yes | ❌ Slightly slower |
| Memory Efficient | ✅ Yes | ❌ Less efficient |

---

# Time Complexity

| Operation | Complexity |
|-----------|------------|
| Indexing | O(1) |
| Slicing | O(k) |
| Membership (`in`) | O(n) |
| Iteration | O(n) |
| count() | O(n) |
| index() | O(n) |
| Concatenation (`+`) | O(n) |
| Repetition (`*`) | O(n × k) |

---

# Best Practices

- Use tuples for fixed data.
- Use lists for data that changes.
- Use unpacking to make code more readable.
- Remember the comma for a single-element tuple.
- Use tuples when returning multiple values from functions.

---

# Interview Questions

### Difference between List and Tuple?

- Lists are mutable.
- Tuples are immutable.
- Tuples are faster and use less memory.

---

### Why are tuples immutable?

To protect data from accidental modification and make them hashable (usable as dictionary keys).

---

### Can a tuple contain a list?

Yes.

```python
data = (1, [2, 3], "Python")
```

But remember:

- The tuple itself cannot change.
- The list inside it **can** be modified.

Example

```python
data[1].append(4)

print(data)
```

Output

```
(1, [2, 3, 4], 'Python')
```

---

### Can tuples be dictionary keys?

Yes, if all their elements are immutable.

```python
student = {
    ("Ali", 101): "A"
}

print(student)
```

---

# Summary

- Tuple = Ordered + Immutable collection.
- Created using `()`.
- Supports indexing, slicing, iteration, packing, and unpacking.
- Only **2 methods**: `count()` and `index()`.
- Faster and more memory-efficient than lists.
- Ideal for fixed or read-only data.

---

# Official Documentation

- Python Docs (Built-in Types): https://docs.python.org/3/library/stdtypes.html#tuple
- Python Tutorial: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
- W3Schools: https://www.w3schools.com/python/python_tuples.asp