# ⚡ Python Operator Precedence Cheat Sheet

> Python evaluates operators according to precedence (priority).

---

# Highest → Lowest Priority

| Priority | Operators |
|----------|-----------|
| 1 | `()` |
| 2 | `**` |
| 3 | `+x`, `-x`, `~x` |
| 4 | `*`, `/`, `//`, `%` |
| 5 | `+`, `-` |
| 6 | `<<`, `>>` |
| 7 | `&` |
| 8 | `^` |
| 9 | `|` |
| 10 | `==`, `!=`, `>`, `<`, `>=`, `<=`, `is`, `is not`, `in`, `not in` |
| 11 | `not` |
| 12 | `and` |
| 13 | `or` |

---

# Examples

## Parentheses First

```python
print((2 + 3) * 4)
```

Output

```python
20
```

---

Without Parentheses

```python
print(2 + 3 * 4)
```

Output

```python
14
```

---

## Exponent Before Multiplication

```python
print(2 * 3 ** 2)
```

Output

```python
18
```

Because

```python
3 ** 2 = 9
2 * 9 = 18
```

---

## Multiplication Before Addition

```python
print(10 + 2 * 5)
```

Output

```python
20
```

---

## Comparison Before Logical Operators

```python
print(10 > 5 and 8 < 20)
```

Output

```python
True
```

---

## not Before and

```python
print(not False and True)
```

Output

```python
True
```

---

## and Before or

```python
print(True or False and False)
```

Output

```python
True
```

Because Python evaluates

```python
False and False
```

first.

---

# Visual Order

```
()

↓

**

↓

*, /, //, %

↓

+, -

↓

<< >>

↓

&

↓

^

↓

|

↓

Comparisons

↓

not

↓

and

↓

or
```

---

# Easy Rule to Remember

```
PEMDAS

Parentheses
Exponent
Multiply / Divide
Add / Subtract
Comparisons
not
and
or
```

---

# Interview Examples

### Example 1

```python
print(5 + 2 * 3)
```

Output

```python
11
```

---

### Example 2

```python
print((5 + 2) * 3)
```

Output

```python
21
```

---

### Example 3

```python
print(True and False or True)
```

Output

```python
True
```

---

### Example 4

```python
print(not True or False)
```

Output

```python
False
```

---

# Common Mistakes

❌

```python
2 + 3 * 4
```

Expected

```
20
```

Actual

```
14
```

---

✅

```python
(2 + 3) * 4
```

Output

```
20
```

---

# Remember

- Use parentheses `()` to make expressions clear.
- `**` has higher priority than `*` and `/`.
- Arithmetic operators execute before comparisons.
- Comparisons execute before logical operators.
- `not` executes before `and`.
- `and` executes before `or`.