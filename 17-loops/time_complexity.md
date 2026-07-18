# 📘 time_complexity.md

# Time Complexity of Python Loops

## Single Loop

```python
for i in range(n):
    print(i)
```

Complexity

```
O(n)
```

---

## While Loop

```python
i = 0

while i < n:
    print(i)
    i += 1
```

Complexity

```
O(n)
```

---

## Nested Loops

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

Complexity

```
O(n²)
```

---

## Triple Nested Loop

```python
for i in range(n):
    for j in range(n):
        for k in range(n):
            print(i, j, k)
```

Complexity

```
O(n³)
```

---

## Loop with break

```python
for i in range(n):
    if i == 5:
        break
```

Best Case

```
O(1)
```

Worst Case

```
O(n)
```

---

## Loop with continue

```python
for i in range(n):
    if i % 2 == 0:
        continue
```

Complexity

```
O(n)
```

---

# Summary Table

| Code | Complexity |
|------|------------|
| Single `for` loop | O(n) |
| Single `while` loop | O(n) |
| Nested loops | O(n²) |
| Triple nested loops | O(n³) |
| `break` | O(1) (best), O(n) (worst) |
| `continue` | O(n) |

---

# Memory Trick

```
1 Loop

↓

O(n)

2 Loops

↓

O(n²)

3 Loops

↓

O(n³)
```