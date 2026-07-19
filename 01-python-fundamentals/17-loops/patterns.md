# 📘 patterns.md

# Python Pattern Printing

Pattern printing is one of the best ways to practice nested loops.

---

# Square Pattern

```python
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()
```

Output

```text
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
```

---

# Right Triangle

```python
for i in range(1,6):
    for j in range(i):
        print("*", end="")
    print()
```

Output

```text
*
**
***
****
*****
```

---

# Inverted Triangle

```python
for i in range(5,0,-1):
    for j in range(i):
        print("*", end="")
    print()
```

Output

```text
*****
****
***
**
*
```

---

# Number Triangle

```python
for i in range(1,6):
    for j in range(i):
        print(i, end=" ")
    print()
```

Output

```text
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
```

---

# Increasing Numbers

```python
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ")
    print()
```

Output

```text
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

---

# Floyd's Triangle

```python
num = 1

for i in range(1,6):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
```

---

# Pyramid

```python
rows = 5

for i in range(rows):
    print(" " * (rows-i-1), end="")
    print("* " * (i+1))
```

---

# Time Complexity

Most pattern problems use nested loops.

```
Outer Loop → n

Inner Loop → n

Total = O(n²)
```

---

# Summary

- Patterns improve loop logic.
- Most use nested loops.
- Frequently asked in interviews.