# Python Lists

## Introduction

A **list** is a built-in Python data structure used to store multiple items in a single variable.

- Ordered
- Mutable (can be changed)
- Allows duplicate values
- Can store different data types

Example

```python
fruits = ["apple", "banana", "mango"]

print(fruits)
```

Output

```
['apple', 'banana', 'mango']
```

---

# Creating Lists

### Empty List

```python
numbers = []
```

or

```python
numbers = list()
```

---

### List of Integers

```python
numbers = [10, 20, 30]
```

---

### List of Strings

```python
fruits = ["apple", "banana", "orange"]
```

---

### Mixed Data Types

```python
data = [10, "Python", True, 3.14]
```

---

### Nested List

```python
matrix = [
    [1, 2],
    [3, 4]
]
```

---

# List Characteristics

```python
numbers = [1, 2, 3]
```

- Ordered ✅
- Mutable ✅
- Allows duplicates ✅
- Indexed ✅

---

# Accessing Elements

## Positive Index

```python
fruits = ["apple", "banana", "mango"]

print(fruits[0])
print(fruits[1])
print(fruits[2])
```

Output

```
apple
banana
mango
```

---

## Negative Index

```python
print(fruits[-1])
print(fruits[-2])
```

Output

```
mango
banana
```

---

# Slicing

```python
numbers = [10,20,30,40,50]
```

```python
print(numbers[1:4])
```

Output

```
[20, 30, 40]
```

---

```python
print(numbers[:3])
```

Output

```
[10,20,30]
```

---

```python
print(numbers[2:])
```

Output

```
[30,40,50]
```

---

```python
print(numbers[::-1])
```

Output

```
[50,40,30,20,10]
```

---

# Change List Items

```python
fruits = ["apple", "banana", "mango"]

fruits[1] = "orange"

print(fruits)
```

Output

```
['apple', 'orange', 'mango']
```

---

# Add Items

## append()

Adds one item at the end.

```python
fruits.append("grapes")
```

---

## insert()

```python
fruits.insert(1, "kiwi")
```

---

## extend()

Adds another iterable.

```python
fruits.extend(["pear", "melon"])
```

---

# Remove Items

## remove()

Removes first matching value.

```python
fruits.remove("banana")
```

---

## pop()

Remove last item.

```python
fruits.pop()
```

Remove by index.

```python
fruits.pop(2)
```

---

## del

```python
del fruits[1]
```

Delete entire list.

```python
del fruits
```

---

## clear()

```python
fruits.clear()
```

Output

```
[]
```

---

# List Methods

| Method | Description |
|---------|-------------|
| append() | Add one item |
| insert() | Insert item |
| extend() | Add multiple items |
| remove() | Remove value |
| pop() | Remove by index |
| clear() | Remove all items |
| index() | Find index |
| count() | Count occurrences |
| sort() | Sort list |
| reverse() | Reverse list |
| copy() | Copy list |

---

# index()

```python
numbers = [10,20,30]

print(numbers.index(20))
```

Output

```
1
```

---

# count()

```python
numbers = [1,2,2,3,2]

print(numbers.count(2))
```

Output

```
3
```

---

# sort()

Ascending

```python
numbers = [5,2,8,1]

numbers.sort()

print(numbers)
```

Output

```
[1,2,5,8]
```

---

Descending

```python
numbers.sort(reverse=True)
```

Output

```
[8,5,2,1]
```

---

# reverse()

```python
numbers.reverse()
```

---

# copy()

```python
new_list = numbers.copy()
```

---

# len()

```python
print(len(numbers))
```

---

# Membership

```python
"apple" in fruits
```

```python
"kiwi" not in fruits
```

---

# Iterating Through List

## for loop

```python
for item in fruits:
    print(item)
```

---

## Using Index

```python
for i in range(len(fruits)):
    print(fruits[i])
```

---

## while loop

```python
i = 0

while i < len(fruits):
    print(fruits[i])
    i += 1
```

---

# List Concatenation

```python
a = [1,2]

b = [3,4]

print(a + b)
```

Output

```
[1,2,3,4]
```

---

# List Repetition

```python
print([1] * 5)
```

Output

```
[1,1,1,1,1]
```

---

# Nested Lists

```python
matrix = [
    [1,2],
    [3,4]
]

print(matrix[1][0])
```

Output

```
3
```

---

# List Comprehension

Basic

```python
numbers = [x for x in range(5)]
```

Output

```
[0,1,2,3,4]
```

---

Squares

```python
squares = [x*x for x in range(5)]
```

Output

```
[0,1,4,9,16]
```

---

Even Numbers

```python
evens = [x for x in range(10) if x % 2 == 0]
```

Output

```
[0,2,4,6,8]
```

---

# Built-in Functions

```python
numbers = [10,20,30]

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers))
```

---

# Packing & Unpacking

```python
numbers = [10,20,30]

a,b,c = numbers

print(a,b,c)
```

---

# Copy vs Assignment

Assignment

```python
a = [1,2]

b = a
```

Both refer to the same list.

---

Copy

```python
a = [1,2]

b = a.copy()
```

Independent lists.

---

# Common Errors

IndexError

```python
numbers = [1,2]

print(numbers[5])
```

---

ValueError

```python
numbers.remove(100)
```

---

# Common Interview Questions

## Largest Number

```python
print(max(numbers))
```

---

## Smallest Number

```python
print(min(numbers))
```

---

## Sum

```python
print(sum(numbers))
```

---

## Reverse List

```python
numbers.reverse()
```

or

```python
numbers[::-1]
```

---

## Check Element Exists

```python
if 10 in numbers:
    print("Found")
```

---

## Count Frequency

```python
numbers.count(5)
```

---

## Copy List

```python
new = old.copy()
```

---

## Sort List

```python
numbers.sort()
```

---

# Time Complexity (Common Operations)

| Operation | Complexity |
|-----------|------------|
| Access by index | O(1) |
| Update by index | O(1) |
| Append | O(1) (amortized) |
| Insert at beginning | O(n) |
| Remove by value | O(n) |
| Search (`in`) | O(n) |
| Pop last | O(1) |
| Pop by index | O(n) |
| Sort | O(n log n) |
| Reverse | O(n) |

---

# Best Practices

- Use meaningful variable names.
- Use `append()` to add one item.
- Use `extend()` to merge lists.
- Use `copy()` instead of assignment when you need an independent copy.
- Prefer list comprehensions for simple transformations.
- Check list length before accessing indexes if unsure.

---

# Summary

- Lists are **ordered, mutable, and allow duplicates**.
- Access items using indexes.
- Modify items directly.
- Use list methods like `append()`, `remove()`, `pop()`, and `sort()`.
- Iterate using `for` or `while`.
- Use list comprehensions for concise code.
- Lists are one of the most commonly used data structures in Python.

---

# References

- Python Official Documentation: https://docs.python.org/3/tutorial/datastructures.html
- Python Standard Types: https://docs.python.org/3/library/stdtypes.html#list
- W3Schools Python Lists: https://www.w3schools.com/python/python_lists.asps