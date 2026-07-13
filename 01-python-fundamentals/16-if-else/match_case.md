# 📘 Python `match...case` Statement

## What is `match...case`?

The `match...case` statement is Python's version of a **switch-case** statement.

It is used to compare a value against multiple patterns and execute the matching block of code.

> **Introduced in Python 3.10**

---

# Why Use `match...case`?

Without `match...case`, you would write:

```python
day = 2

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
else:
    print("Invalid Day")
```

Using `match...case`, the same code becomes cleaner:

```python
day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid Day")
```

---

# Syntax

```python
match expression:
    case pattern1:
        # code

    case pattern2:
        # code

    case _:
        # default code
```

- `match` → checks the value.
- `case` → possible matches.
- `_` → default case (like `else`).

---

# Simple Example

```python
number = 3

match number:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Unknown")
```

Output

```text
Three
```

---

# Match Strings

```python
color = "red"

match color:
    case "red":
        print("Stop")
    case "green":
        print("Go")
    case "yellow":
        print("Wait")
    case _:
        print("Invalid Color")
```

Output

```text
Stop
```

---

# Match Characters

```python
grade = "A"

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Average")
    case _:
        print("Invalid Grade")
```

---

# Multiple Cases (OR)

Use `|` to match multiple values.

```python
day = 6

match day:
    case 1 | 7:
        print("Weekend")
    case 2 | 3 | 4 | 5 | 6:
        print("Weekday")
```

Output

```text
Weekday
```

---

# Default Case

The `_` matches everything if no other case matches.

```python
number = 10

match number:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Other Number")
```

Output

```text
Other Number
```

---

# Match User Input

```python
choice = int(input("Enter a number (1-3): "))

match choice:
    case 1:
        print("Add")
    case 2:
        print("Delete")
    case 3:
        print("Exit")
    case _:
        print("Invalid Choice")
```

---

# Match Months

```python
month = 4

match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case _:
        print("Invalid Month")
```

---

# Match Boolean Values

```python
status = True

match status:
    case True:
        print("Logged In")
    case False:
        print("Logged Out")
```

---

# Match with Guard (`if`)

You can add a condition after a pattern.

```python
age = 20

match age:
    case x if x >= 18:
        print("Adult")
    case _:
        print("Minor")
```

Output

```text
Adult
```

---

# Match Lists (Sequence Pattern)

```python
data = [10, 20]

match data:
    case [a, b]:
        print(a)
        print(b)
```

Output

```text
10
20
```

---

# Match Tuples

```python
point = (5, 10)

match point:
    case (x, y):
        print(x)
        print(y)
```

Output

```text
5
10
```

---

# Nested Match

```python
command = ("move", "left")

match command:
    case ("move", direction):
        print("Move", direction)
    case ("stop",):
        print("Stop")
```

Output

```text
Move left
```

---

# `if...elif...else` vs `match...case`

### Using if...elif

```python
day = 2

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
else:
    print("Invalid")
```

---

### Using match...case

```python
day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case _:
        print("Invalid")
```

---

# When to Use

✅ Use `match...case` when:

- Checking many fixed values.
- Building menu-driven programs.
- Replacing long `if...elif...else` chains.
- Pattern matching (lists, tuples, etc.).

---

# Common Mistakes

## ❌ Forgetting `_`

Wrong

```python
match x:
    case 1:
        print("One")
```

If `x` is not `1`, nothing happens.

Better

```python
match x:
    case 1:
        print("One")
    case _:
        print("Invalid")
```

---

## ❌ Using `=` Instead of `:`

Wrong

```python
case 1 =
```

Correct

```python
case 1:
```

---

## ❌ Using Python < 3.10

`match...case` only works in **Python 3.10 or later**.

Older versions will raise:

```text
SyntaxError
```

---

# Time Complexity

| Statement | Complexity |
|-----------|------------|
| match...case | O(1) (small fixed cases) |
| Many cases | O(n) (worst case, checks sequentially) |

---

# Interview Questions

### What is `match...case`?

A control flow statement introduced in **Python 3.10** that compares a value against multiple patterns.

---

### What does `_` mean?

It is the **default case**, similar to `else`.

---

### Can multiple values be matched in one case?

✅ Yes.

```python
case 1 | 2 | 3:
```

---

### Can `match` work with strings?

✅ Yes.

---

### Can `match` work with lists and tuples?

✅ Yes.

This feature is called **Pattern Matching**.

---

# Summary

- `match...case` is Python's switch-case alternative.
- Introduced in **Python 3.10**.
- `match` checks a value.
- `case` defines possible matches.
- `_` acts as the default (`else`) case.
- `|` matches multiple values.
- Supports pattern matching with lists, tuples, and more.
- Makes code cleaner than long `if...elif...else` chains.