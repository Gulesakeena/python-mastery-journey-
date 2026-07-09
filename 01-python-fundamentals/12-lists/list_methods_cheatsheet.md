# 🐍 Python List Methods Cheat Sheet

> Quick reference for the most commonly used Python list methods.

---

# Creating a List

```python
numbers = [10, 20, 30]
fruits = ["apple", "banana", "mango"]
```

---

# append()

Adds a single element to the end.

```python
numbers.append(40)
```

Before

```python
[10, 20, 30]
```

After

```python
[10, 20, 30, 40]
```

Time Complexity: **O(1)**

---

# extend()

Adds multiple elements from another iterable.

```python
numbers.extend([40, 50, 60])
```

Before

```python
[10, 20, 30]
```

After

```python
[10, 20, 30, 40, 50, 60]
```

Time Complexity: **O(k)**

---

# insert()

Insert an element at a specific index.

```python
numbers.insert(1, 15)
```

Before

```python
[10, 20, 30]
```

After

```python
[10, 15, 20, 30]
```

Time Complexity: **O(n)**

---

# remove()

Removes the **first occurrence** of a value.

```python
numbers.remove(20)
```

Before

```python
[10, 20, 30]
```

After

```python
[10, 30]
```

Raises:

```python
ValueError
```

if the value is not found.

Time Complexity: **O(n)**

---

# pop()

Removes and returns an element.

Remove last element

```python
last = numbers.pop()
```

Remove by index

```python
item = numbers.pop(1)
```

Example

```python
numbers = [10,20,30]

print(numbers.pop())
```

Output

```python
30
```

Time Complexity

- Last element → **O(1)**
- By index → **O(n)**

---

# clear()

Removes all elements.

```python
numbers.clear()
```

Output

```python
[]
```

Time Complexity: **O(n)**

---

# index()

Returns the first index of a value.

```python
numbers.index(20)
```

Output

```python
1
```

Raises

```python
ValueError
```

if not found.

Time Complexity: **O(n)**

---

# count()

Counts occurrences.

```python
numbers = [1,2,2,3,2]

print(numbers.count(2))
```

Output

```python
3
```

Time Complexity: **O(n)**

---

# sort()

Sorts the list in ascending order.

```python
numbers.sort()
```

Descending

```python
numbers.sort(reverse=True)
```

Example

```python
numbers = [5,1,4,2]

numbers.sort()

print(numbers)
```

Output

```python
[1,2,4,5]
```

Time Complexity: **O(n log n)**

---

# reverse()

Reverses the list in-place.

```python
numbers.reverse()
```

Example

```python
numbers = [1,2,3]

numbers.reverse()

print(numbers)
```

Output

```python
[3,2,1]
```

Time Complexity: **O(n)**

---

# copy()

Creates a shallow copy.

```python
new_list = numbers.copy()
```

Example

```python
a = [1,2,3]

b = a.copy()
```

Changing

```python
b.append(4)
```

does not affect

```python
a
```

Time Complexity: **O(n)**

---

# Summary Table

| Method | Description | Returns | Complexity |
|---------|-------------|----------|------------|
| append() | Add one item | None | O(1) |
| extend() | Add multiple items | None | O(k) |
| insert() | Insert at index | None | O(n) |
| remove() | Remove by value | None | O(n) |
| pop() | Remove by index | Removed item | O(1) / O(n) |
| clear() | Remove all items | None | O(n) |
| index() | Find index | int | O(n) |
| count() | Count value | int | O(n) |
| sort() | Sort list | None | O(n log n) |
| reverse() | Reverse list | None | O(n) |
| copy() | Copy list | New list | O(n) |

---

# Common Interview Questions

## Difference between append() and extend()

```python
a = [1,2]

a.append([3,4])

print(a)
```

Output

```python
[1,2,[3,4]]
```

---

```python
a = [1,2]

a.extend([3,4])

print(a)
```

Output

```python
[1,2,3,4]
```

---

## Difference between remove() and pop()

### remove()

- Removes by **value**
- Returns **None**

```python
numbers.remove(20)
```

---

### pop()

- Removes by **index**
- Returns the removed item

```python
item = numbers.pop(1)
```

---

## Difference between sort() and sorted()

### sort()

- Changes the original list.

```python
numbers.sort()
```

---

### sorted()

- Returns a new sorted list.

```python
new_list = sorted(numbers)
```

---

## Difference between reverse() and slicing

```python
numbers.reverse()
```

Modifies the original list.

---

```python
numbers[::-1]
```

Returns a new reversed list.

---

# Built-in Functions (Not List Methods)

```python
len(numbers)
max(numbers)
min(numbers)
sum(numbers)
sorted(numbers)
```

---

# Common Errors

## ValueError

```python
numbers.remove(100)
```

---

## IndexError

```python
numbers.pop(10)
```

---

## AttributeError

```python
text = "Python"

text.append("A")
```

Strings don't have `append()`.

---

# Best Practices

- Use `append()` to add one item.
- Use `extend()` to merge lists.
- Use `pop()` when you need the removed value.
- Use `remove()` when you know the value.
- Use `copy()` instead of `=` when creating an independent copy.
- Use `sorted()` if you want to keep the original list unchanged.

---

# Official Documentation

- Python Docs: https://docs.python.org/3/tutorial/datastructures.html
- Python List Methods: https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types
- W3Schools Lists: https://www.w3schools.com/python/python_lists.asp