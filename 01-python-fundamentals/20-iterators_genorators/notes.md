# 20 - Python Iterators

## What is an Iterator?

An **iterator** is an object that returns **one value at a time**.

Instead of loading all values into memory, an iterator produces values only when requested.

---

## Why are Iterators Important?

They are:

- Memory efficient
- Faster for large datasets
- Used by `for` loops
- Used in generators
- Used in file handling
- Used in NumPy and Pandas

---

## Iterable vs Iterator

### Iterable

An object that **can be looped over**.

Examples:

- list
- tuple
- string
- dictionary
- set

```python
numbers = [1, 2, 3]
```

`numbers` is **iterable**, but it is **not an iterator**.

---

### Iterator

An object that remembers its current position and returns one item at a time.

Create an iterator using:

```python
iter(iterable)
```

Example:

```python
numbers = [1, 2, 3]

it = iter(numbers)
```

Now `it` is an iterator.

---

## next()

`next()` returns the next element.

```python
next(it)
```

Every call moves the iterator forward.

---

## StopIteration

When there are no more items, Python raises:

```python
StopIteration
```

---

## Iterator Protocol

Every iterator has two methods:

- `__iter__()`
- `__next__()`

Python's `for` loop uses these internally.

---

## How a for Loop Works

```python
for item in numbers:
    print(item)
```

Python internally does something similar to:

```python
it = iter(numbers)

while True:
    try:
        item = next(it)
        print(item)
    except StopIteration:
        break
```

---

## Custom Iterator

A class becomes an iterator when it implements:

- `__iter__()`
- `__next__()`

---

## Infinite Iterator

An iterator can continue forever.

Example:

```
1
2
3
4
5
...
```

Always add a stopping condition when using one.

---

## Iterator vs Generator

| Iterator | Generator |
|----------|-----------|
| Class-based | Function-based |
| Uses `__next__()` | Uses `yield` |
| More code | Less code |
| Manual | Automatic |

---

## Real-World Uses

- Reading large files
- Streaming data
- Machine Learning datasets
- API pagination
- Log processing

---

## Interview Questions

### What is the difference between an iterable and an iterator?

An iterable can create an iterator. An iterator returns one item at a time.

---

### Which function creates an iterator?

```python
iter()
```

---

### Which function gets the next item?

```python
next()
```

---

### Which exception ends an iterator?

```
StopIteration
```

---

## Time Complexity

| Operation | Complexity |
|-----------|------------|
| next() | O(1) |
| iter() | O(1) |