# 📘 loop_control.md

# Python Loop Control Statements

Loop control statements change the normal flow of a loop.

Python has three loop control statements:

- `break`
- `continue`
- `pass`

---

# break

Stops the loop immediately.

## Syntax

```python
break
```

Example

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

Output

```text
0
1
2
3
4
```

---

# continue

Skips the current iteration.

## Syntax

```python
continue
```

Example

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

Output

```text
0
1
3
4
```

---

# pass

Does nothing.

Used as a placeholder.

Example

```python
for i in range(5):
    pass
```

---

# break vs continue

| break | continue |
|--------|----------|
| Stops loop completely | Skips one iteration |
| Exits loop | Continues loop |

---

# Loop else

The `else` block executes if the loop finishes normally.

```python
for i in range(3):
    print(i)
else:
    print("Loop Finished")
```

Output

```text
0
1
2
Loop Finished
```

---

# Example

Search a number.

```python
numbers = [3, 5, 8, 10]

target = 8

for num in numbers:
    if num == target:
        print("Found")
        break
else:
    print("Not Found")
```

---

# Time Complexity

| Statement | Complexity |
|-----------|------------|
| break | O(1) |
| continue | O(1) |
| pass | O(1) |

---

# Summary

- `break` → stop loop.
- `continue` → skip current iteration.
- `pass` → placeholder.
- `else` executes only if the loop doesn't end with `break`.