# 🐍 Python List Comprehension

> A quick and powerful way to create new lists in Python using a single line of code.

---

# What is List Comprehension?

List comprehension provides a concise syntax for creating lists.

Instead of writing a loop and using `append()`, you can write everything in one line.

Traditional way:

```python
numbers = []

for i in range(5):
    numbers.append(i)

print(numbers)
```

Output

```
[0, 1, 2, 3, 4]
```

Using list comprehension:

```python
numbers = [i for i in range(5)]

print(numbers)
```

Output

```
[0, 1, 2, 3, 4]
```

---

# Syntax

```python
new_list = [expression for item in iterable]
```

or

```python
new_list = [expression for item in iterable if condition]
```

---

# Components

```python
[x * 2 for x in numbers]
```

| Part | Meaning |
|------|---------|
| `x * 2` | Expression |
| `x` | Variable |
| `numbers` | Iterable |

---

# Basic Examples

## Create Numbers

```python
numbers = [x for x in range(5)]

print(numbers)
```

Output

```
[0, 1, 2, 3, 4]
```

---

## Squares

```python
squares = [x ** 2 for x in range(6)]

print(squares)
```

Output

```
[0, 1, 4, 9, 16, 25]
```

---

## Cubes

```python
cubes = [x ** 3 for x in range(5)]

print(cubes)
```

Output

```
[0, 1, 8, 27, 64]
```

---

# Using Conditions

## Even Numbers

```python
evens = [x for x in range(11) if x % 2 == 0]

print(evens)
```

Output

```
[0, 2, 4, 6, 8, 10]
```

---

## Odd Numbers

```python
odds = [x for x in range(10) if x % 2 != 0]

print(odds)
```

Output

```
[1, 3, 5, 7, 9]
```

---

## Numbers Greater Than 10

```python
numbers = [5, 12, 8, 20, 15]

result = [x for x in numbers if x > 10]

print(result)
```

Output

```
[12, 20, 15]
```

---

# Strings

## Uppercase

```python
words = ["python", "java", "c++"]

result = [word.upper() for word in words]

print(result)
```

Output

```
['PYTHON', 'JAVA', 'C++']
```

---

## Lowercase

```python
words = ["AI", "ML", "Python"]

result = [word.lower() for word in words]

print(result)
```

Output

```
['ai', 'ml', 'python']
```

---

## String Length

```python
words = ["Python", "Java", "AI"]

lengths = [len(word) for word in words]

print(lengths)
```

Output

```
[6, 4, 2]
```

---

# Using if-else

Syntax

```python
[expression_if_true if condition else expression_if_false for item in iterable]
```

Example

```python
numbers = [1, 2, 3, 4, 5]

result = ["Even" if x % 2 == 0 else "Odd" for x in numbers]

print(result)
```

Output

```
['Odd', 'Even', 'Odd', 'Even', 'Odd']
```

---

# Nested List Comprehension

Create a multiplication table.

```python
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]

print(table)
```

Output

```
[
 [1,2,3,4,5],
 [2,4,6,8,10],
 [3,6,9,12,15],
 [4,8,12,16,20],
 [5,10,15,20,25]
]
```

---

# Flatten a Nested List

```python
matrix = [
    [1,2],
    [3,4],
    [5,6]
]

flat = [item for row in matrix for item in row]

print(flat)
```

Output

```
[1, 2, 3, 4, 5, 6]
```

---

# Copy a List

```python
numbers = [1,2,3]

copy = [x for x in numbers]

print(copy)
```

---

# Create Characters

```python
letters = [char for char in "Python"]

print(letters)
```

Output

```
['P', 'y', 't', 'h', 'o', 'n']
```

---

# Remove Empty Strings

```python
words = ["AI", "", "Python", "", "ML"]

result = [word for word in words if word != ""]

print(result)
```

Output

```
['AI', 'Python', 'ML']
```

---

# Numbers Divisible by 5

```python
numbers = [x for x in range(1, 51) if x % 5 == 0]

print(numbers)
```

Output

```
[5,10,15,20,25,30,35,40,45,50]
```

---

# Common Interview Examples

## Square Every Number

```python
numbers = [1,2,3,4]

result = [x * x for x in numbers]
```

---

## Double Every Number

```python
result = [x * 2 for x in numbers]
```

---

## Filter Positive Numbers

```python
numbers = [-3,5,-2,8,-1]

positive = [x for x in numbers if x > 0]
```

---

## Remove Duplicates (with set)

```python
numbers = [1,2,2,3,3,4]

unique = list(set(numbers))
```

---

# List Comprehension vs Loop

Traditional

```python
result = []

for x in range(5):
    result.append(x)
```

List Comprehension

```python
result = [x for x in range(5)]
```

---

# Advantages

- Less code
- More readable
- Faster than using `append()` in many cases
- Pythonic style

---

# Limitations

Avoid list comprehensions when:

- Logic is very complex.
- Multiple nested conditions reduce readability.
- You need many statements inside the loop.

In such cases, use a normal `for` loop.

---

# Time Complexity

| Operation | Complexity |
|-----------|------------|
| Basic list comprehension | O(n) |
| With filtering | O(n) |
| Nested list comprehension | O(n²) (depends on nesting) |

---

# Best Practices

- Keep list comprehensions short and readable.
- Use them for simple transformations and filtering.
- Prefer a normal loop when the logic becomes complicated.
- Avoid deeply nested comprehensions unless necessary.

---

# Summary

- List comprehension creates lists in one line.
- Basic syntax:

```python
[expression for item in iterable]
```

- With condition:

```python
[expression for item in iterable if condition]
```

- With if-else:

```python
[true_value if condition else false_value for item in iterable]
```

- Common uses:
  - Creating lists
  - Filtering elements
  - Transforming values
  - Processing strings
  - Flattening nested lists

---

# Official Documentation

- Python Tutorial: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
- Python Language Reference: https://docs.python.org/3/reference/expressions.html#displays-for-lists-sets-and-dictionaries
- W3Schools: https://www.w3schools.com/python/python_lists_comprehension.asp