# 📘 Dictionary Comprehension

Dictionary comprehension creates dictionaries in one line.

---

# Syntax

```python
{
    key: value
    for item in iterable
}
```

---

# Example 1

```python
numbers = {
    x: x*x
    for x in range(1,6)
}

print(numbers)
```

Output

```python
{
1:1,
2:4,
3:9,
4:16,
5:25
}
```

---

# Example 2

```python
square = {
    x:x**2
    for x in range(1,11)
}
```

---

# Example 3

Even Numbers

```python
even = {
    x:x
    for x in range(11)
    if x%2==0
}
```

---

# Example 4

Odd Numbers

```python
odd = {
    x:x
    for x in range(11)
    if x%2!=0
}
```

---

# Example 5

Convert List into Dictionary

```python
names = ["Ali","Sara","Ahmed"]

data = {
    name:len(name)
    for name in names
}
```

Output

```python
{
"Ali":3,
"Sara":4,
"Ahmed":5
}
```

---

# Example 6

Swap Keys and Values

```python
student = {
    "Ali":85,
    "Sara":90
}

new = {
    value:key
    for key,value in student.items()
}
```

---

# Example 7

Uppercase Keys

```python
student = {
    "ali":20,
    "sara":21
}

upper = {
    key.upper():value
    for key,value in student.items()
}
```

---

# Example 8

Multiply Values

```python
student = {
    "Ali":20,
    "Sara":30
}

double = {
    key:value*2
    for key,value in student.items()
}
```

---

# Traditional vs Comprehension

Traditional

```python
square = {}

for i in range(5):
    square[i] = i*i
```

Comprehension

```python
square = {
    i:i*i
    for i in range(5)
}
```

---

# When to Use

✅ Creating dictionaries

✅ Filtering data

✅ Transforming keys

✅ Transforming values

---

# Time Complexity

Usually **O(n)** because every item is processed once.