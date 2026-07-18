# 📘 Python Loops Notes

## What are Loops?

A **loop** is used to execute a block of code **multiple times**.

Instead of writing the same code repeatedly, loops automate repetition.

Example:

Without loop

```python
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
```

With loop

```python
for i in range(5):
    print("Hello")
```

---

# Why Use Loops?

Loops help you:

- Repeat tasks
- Process lists and strings
- Reduce code duplication
- Iterate through collections
- Build efficient programs

---

# Types of Loops in Python

Python has **two** loops:

1. `for` loop
2. `while` loop

---

# for Loop

A `for` loop is used when you know **how many times** you want to repeat something or when iterating over a sequence.

## Syntax

```python
for variable in sequence:
    # code
```

Example

```python
for i in range(5):
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

# while Loop

A `while` loop runs **as long as a condition is True**.

## Syntax

```python
while condition:
    # code
```

Example

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

# Difference Between for and while

| for Loop | while Loop |
|----------|------------|
| Used when number of iterations is known | Used when number of iterations is unknown |
| Iterates over a sequence | Runs until condition becomes False |
| Simpler for collections | Better for user-controlled repetition |

---

# The `range()` Function

`range()` generates a sequence of numbers.

## range(stop)

```python
for i in range(5):
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

## range(start, stop)

```python
for i in range(2, 6):
    print(i)
```

Output

```text
2
3
4
5
```

---

## range(start, stop, step)

```python
for i in range(0, 10, 2):
    print(i)
```

Output

```text
0
2
4
6
8
```

---

# Loop Through a List

```python
fruits = ["Apple", "Banana", "Orange"]

for fruit in fruits:
    print(fruit)
```

---

# Loop Through a String

```python
text = "Python"

for ch in text:
    print(ch)
```

---

# Loop Through a Tuple

```python
numbers = (1, 2, 3)

for num in numbers:
    print(num)
```

---

# Loop Through a Dictionary

```python
student = {
    "name": "Ali",
    "age": 20
}

for key in student:
    print(key)
```

Output

```text
name
age
```

---

# Dictionary Values

```python
for value in student.values():
    print(value)
```

---

# Dictionary Items

```python
for key, value in student.items():
    print(key, value)
```

---

# Loop Through a Set

```python
numbers = {1, 2, 3}

for num in numbers:
    print(num)
```

---

# Nested Loops

A loop inside another loop.

```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

Output

```text
0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2
```

---

# break Statement

Stops the loop immediately.

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

# continue Statement

Skips the current iteration.

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

# pass Statement

Used as a placeholder.

```python
for i in range(5):
    pass
```

---

# else with Loops

The `else` block runs when the loop finishes normally.

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

# Infinite Loop

```python
while True:
    print("Hello")
```

Stop using **Ctrl + C**.

---

# Common Examples

## Print 1 to 10

```python
for i in range(1, 11):
    print(i)
```

---

## Sum of Numbers

```python
total = 0

for i in range(1, 6):
    total += i

print(total)
```

---

## Multiplication Table

```python
number = 5

for i in range(1, 11):
    print(number, "x", i, "=", number * i)
```

---

## Count Vowels

```python
text = "Python"

count = 0

for ch in text:
    if ch.lower() in "aeiou":
        count += 1

print(count)
```

---

## Find Largest Number

```python
numbers = [3, 7, 2, 9, 4]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(largest)
```

---

# Common Mistakes

## Forgetting to Update Variable in while

Wrong

```python
count = 1

while count <= 5:
    print(count)
```

Infinite loop.

Correct

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

## Wrong Indentation

Wrong

```python
for i in range(5):
print(i)
```

Correct

```python
for i in range(5):
    print(i)
```

---

## Using range Incorrectly

Wrong

```python
range(1, 10, 0)
```

Step cannot be `0`.

---

# Best Practices

- Use `for` when iterating over sequences.
- Use `while` when the number of iterations is unknown.
- Avoid infinite loops unless necessary.
- Use meaningful variable names.
- Keep nested loops simple.

---

# Time Complexity

| Operation | Complexity |
|-----------|------------|
| `for` loop over `n` items | O(n) |
| `while` loop (n iterations) | O(n) |
| Nested loops | O(n²) |
| `break` | O(1) |
| `continue` | O(1) |

---

# Interview Questions

### What are the two loops in Python?

- `for`
- `while`

---

### When should you use a `for` loop?

When the number of iterations is known or when iterating over a sequence.

---

### When should you use a `while` loop?

When repetition depends on a condition.

---

### What is `break`?

Stops the loop immediately.

---

### What is `continue`?

Skips the current iteration and moves to the next.

---

### What does `range()` do?

Generates a sequence of numbers.

---

### Can loops have an `else` block?

Yes. The `else` block runs if the loop completes normally without encountering a `break`.

---

# Summary

- Loops repeat code.
- Python provides **`for`** and **`while`** loops.
- Use `range()` to generate sequences.
- Use `break` to stop a loop.
- Use `continue` to skip an iteration.
- Use `pass` as a placeholder.
- Nested loops repeat loops inside loops.
- The complexity of a single loop is usually **O(n)**, while nested loops are typically **O(n²)**.