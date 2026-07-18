# 📘 while_loops.md

# Python `while` Loop

## What is a `while` Loop?

A `while` loop repeatedly executes a block of code **as long as a condition is `True`**.

Unlike a `for` loop, a `while` loop is used when **you don't know in advance how many times the loop should run**.

---

# Syntax

```python
while condition:
    # code
```

---

# Flowchart

```text
        Start
          │
          ▼
   Check Condition
      │       │
   True      False
      │         │
      ▼         ▼
 Execute Code   End
      │
      └──────────┘
```

---

# Example 1

Print numbers from 1 to 5.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output

```text
1
2
3
4
5
```

---

# Example 2

Print "Hello" five times.

```python
count = 1

while count <= 5:
    print("Hello")
    count += 1
```

---

# Example 3

Print even numbers.

```python
num = 2

while num <= 20:
    print(num)
    num += 2
```

Output

```text
2
4
6
8
10
12
14
16
18
20
```

---

# Example 4

Print odd numbers.

```python
num = 1

while num <= 19:
    print(num)
    num += 2
```

---

# Example 5

Countdown

```python
num = 10

while num >= 1:
    print(num)
    num -= 1
```

Output

```text
10
9
8
7
6
5
4
3
2
1
```

---

# Example 6

Sum of first N numbers.

```python
n = 5

count = 1
total = 0

while count <= n:
    total += count
    count += 1

print(total)
```

Output

```text
15
```

---

# Example 7

Factorial

```python
number = 5

fact = 1

while number > 0:
    fact *= number
    number -= 1

print(fact)
```

Output

```text
120
```

---

# Example 8

Multiplication Table

```python
number = 7

i = 1

while i <= 10:
    print(number, "x", i, "=", number * i)
    i += 1
```

---

# Example 9

Reverse a Number

```python
number = 1234

while number > 0:
    digit = number % 10
    print(digit, end="")
    number //= 10
```

Output

```text
4321
```

---

# Infinite Loop

A loop that never stops.

```python
while True:
    print("Hello")
```

Stop it using:

```
Ctrl + C
```

---

# Taking Input Until User Stops

```python
while True:

    name = input("Enter name (exit to stop): ")

    if name == "exit":
        break

    print(name)
```

---

# while with break

```python
count = 1

while True:

    print(count)

    if count == 5:
        break

    count += 1
```

---

# while with continue

```python
count = 0

while count < 5:

    count += 1

    if count == 3:
        continue

    print(count)
```

Output

```text
1
2
4
5
```

---

# while with else

The `else` block executes if the loop finishes normally (without `break`).

```python
count = 1

while count <= 3:
    print(count)
    count += 1
else:
    print("Loop Finished")
```

Output

```text
1
2
3
Loop Finished
```

---

# Common Mistakes

## Forgetting to Update the Variable

Wrong

```python
count = 1

while count <= 5:
    print(count)
```

This creates an **infinite loop**.

Correct

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

## Wrong Condition

Wrong

```python
count = 5

while count <= 1:
    print(count)
```

The loop never executes.

---

## Using Assignment Instead of Comparison

Wrong

```python
while count = 5:
```

Correct

```python
while count == 5:
```

---

# When to Use `while`

Use `while` when:

- Number of iterations is unknown.
- Waiting for user input.
- Menu-driven programs.
- Login authentication.
- ATM systems.
- Games.
- Password validation.
- Repeat until a condition changes.

---

# while vs for

| for Loop | while Loop |
|----------|------------|
| Number of iterations is known | Number of iterations is unknown |
| Uses `range()` or sequences | Uses a condition |
| Easier for collections | Better for user-controlled repetition |

---

# Time Complexity

| Code | Complexity |
|------|------------|
| Simple while loop | O(n) |
| Nested while loops | O(n²) |
| Infinite loop | Infinite (until stopped) |
| break | O(1) |
| continue | O(1) |

---

# Interview Questions

### What is a `while` loop?

A loop that runs as long as its condition is `True`.

---

### When should you use a `while` loop?

When the number of iterations is unknown.

---

### What causes an infinite loop?

When the loop condition never becomes `False`.

---

### Can a `while` loop have an `else` block?

Yes. The `else` block executes if the loop ends normally without encountering a `break`.

---

### Difference between `for` and `while`?

- `for` → Known number of iterations.
- `while` → Unknown number of iterations.

---

# Real-Life Examples

- ATM Machine
- Login Authentication
- Banking System
- Menu-Driven Programs
- Password Checking
- Guess the Number Game
- Chat Applications
- Online Shopping Menu

---

# Summary

- `while` repeats code while a condition is `True`.
- Best for situations where the number of iterations is not known beforehand.
- Always update the loop variable to avoid infinite loops.
- Supports `break`, `continue`, and `else`.
- A single `while` loop usually has **O(n)** time complexity.