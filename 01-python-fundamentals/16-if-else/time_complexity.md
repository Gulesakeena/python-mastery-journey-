# 📘 Time Complexity of Python if...else

## What is Time Complexity?

**Time Complexity** measures how the running time of an algorithm grows as the input size (`n`) increases.

It is represented using **Big O Notation**.

---

# Common Big O Notations

| Big O | Name | Performance |
|-------|------|-------------|
| **O(1)** | Constant | ⭐⭐⭐⭐⭐ Fastest |
| **O(log n)** | Logarithmic | ⭐⭐⭐⭐ |
| **O(n)** | Linear | ⭐⭐⭐ |
| **O(n log n)** | Linearithmic | ⭐⭐ |
| **O(n²)** | Quadratic | ⭐ |
| **O(2ⁿ)** | Exponential | Very Slow |
| **O(n!)** | Factorial | Worst |

---

# Does an if Statement Increase Time Complexity?

**No.**

An `if` statement only checks a condition.

Checking a condition takes **constant time**.

Example:

```python
age = 20

if age >= 18:
    print("Adult")
```

Time Complexity

```
O(1)
```

---

# if...else

```python
number = 10

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Time Complexity

```
O(1)
```

Only one condition is checked.

---

# if...elif...else

```python
marks = 80

if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
else:
    print("Fail")
```

Worst-case Time Complexity

```
O(1)
```

Although Python may check multiple conditions, the number of conditions is fixed.

---

# Nested if

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Allowed")
```

Time Complexity

```
O(1)
```

Two conditions are checked.

Still constant time.

---

# Using Logical Operators

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Allowed")
```

Time Complexity

```
O(1)
```

---

# Condition Inside a Loop

```python
numbers = [10, 20, 30, 40, 50]

for num in numbers:
    if num > 25:
        print(num)
```

Time Complexity

```
O(n)
```

Why?

- Loop runs **n** times.
- Each `if` check is **O(1)**.

Therefore,

```
O(n × 1)

=

O(n)
```

---

# Nested if Inside a Loop

```python
numbers = [10, 20, 30]

for num in numbers:
    if num > 10:
        if num % 2 == 0:
            print(num)
```

Time Complexity

```
O(n)
```

Reason:

- Loop → **O(n)**
- Each `if` → **O(1)**

Overall

```
O(n)
```

---

# Nested Loops with if

```python
numbers = [1,2,3]

for i in numbers:
    for j in numbers:
        if i == j:
            print(i)
```

Time Complexity

```
O(n²)
```

Reason:

Outer loop

↓

Inner loop

↓

if statement

```
O(n × n × 1)

=

O(n²)
```

---

# Searching Using if

```python
numbers = [1,2,3,4,5]

target = 4

for num in numbers:
    if num == target:
        print("Found")
        break
```

Best Case

```
O(1)
```

(Target found immediately.)

Worst Case

```
O(n)
```

(Target at the end or not present.)

---

# Multiple Independent if Statements

```python
if a > 10:
    print(a)

if b > 10:
    print(b)

if c > 10:
    print(c)
```

Time Complexity

```
O(1)
```

Only a fixed number of conditions are checked.

---

# if with Dictionary Lookup

```python
student = {
    "name": "Ali",
    "age": 20
}

if "name" in student:
    print(student["name"])
```

Time Complexity

```
O(1)
```

Dictionary lookup is approximately constant time.

---

# if with Set Lookup

```python
numbers = {1,2,3,4}

if 3 in numbers:
    print("Found")
```

Time Complexity

```
O(1)
```

Sets use hash tables.

---

# if with List Lookup

```python
numbers = [1,2,3,4]

if 3 in numbers:
    print("Found")
```

Time Complexity

```
O(n)
```

Python searches the list one element at a time.

---

# Summary Examples

### Example 1

```python
if x > 0:
    print(x)
```

Complexity

```
O(1)
```

---

### Example 2

```python
for i in range(n):
    if i % 2 == 0:
        print(i)
```

Complexity

```
O(n)
```

---

### Example 3

```python
for i in range(n):
    for j in range(n):
        if i == j:
            print(i)
```

Complexity

```
O(n²)
```

---

### Example 4

```python
if key in dictionary:
    print(dictionary[key])
```

Complexity

```
O(1)
```

---

### Example 5

```python
if value in my_list:
    print(value)
```

Complexity

```
O(n)
```

---

# Important Rule

The `if` statement **does not determine the overall time complexity**.

The complexity depends on the operations performed **inside** the `if`.

For example:

```python
if condition:
    for i in range(n):
        print(i)
```

Time Complexity

```
O(n)
```

The loop dominates the runtime.

---

# Interview Questions

### Is an `if` statement O(1)?

✅ Yes.

Checking a condition takes constant time.

---

### Does adding more `if` statements increase complexity?

Only if the number of conditions grows with the input size (`n`).

A fixed number of `if` statements is still **O(1)**.

---

### What is the complexity of an `if` inside a loop?

```
Loop → O(n)

if → O(1)

Overall → O(n)
```

---

### What is the complexity of nested loops with an `if`?

```
Outer Loop → O(n)

Inner Loop → O(n)

if → O(1)

Overall → O(n²)
```

---

# Memory Trick

```
if

↓

Only checks a condition

↓

O(1)

Loop + if

↓

O(n)

Nested Loops + if

↓

O(n²)
```

---

# Summary Table

| Code | Time Complexity |
|------|-----------------|
| `if` | O(1) |
| `if...else` | O(1) |
| `if...elif...else` | O(1) |
| Nested `if` | O(1) |
| `if` inside one loop | O(n) |
| `if` inside nested loops | O(n²) |
| `if` with dictionary lookup | O(1) |
| `if` with set lookup | O(1) |
| `if` with list lookup | O(n) |

---

# Key Takeaways

- ✅ An `if` statement itself is **O(1)**.
- ✅ `if`, `if...else`, and `if...elif...else` all have constant-time condition checks.
- ✅ The overall complexity depends on the code executed inside the condition.
- ✅ A loop with an `if` is usually **O(n)**.
- ✅ Nested loops with an `if` are usually **O(n²)**.
- ✅ Dictionary and set lookups inside an `if` are approximately **O(1)**, while list lookups are **O(n)**.