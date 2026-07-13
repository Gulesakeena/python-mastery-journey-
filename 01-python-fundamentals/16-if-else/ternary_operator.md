# 📘 Python Ternary Operator

## What is a Ternary Operator?

A **ternary operator** is a **one-line shortcut for an `if...else` statement**.

Instead of writing multiple lines, you can write the decision in a single line.

---

# Syntax

```python
value_if_true if condition else value_if_false
```

Read it as:

> "If the condition is True, return the first value; otherwise, return the second value."

---

# Basic Example

### Using if...else

```python
age = 20

if age >= 18:
    status = "Adult"
else:
    status = "Minor"

print(status)
```

Output

```text
Adult
```

---

### Using Ternary Operator

```python
age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)
```

Output

```text
Adult
```

---

# Check Even or Odd

```python
number = 8

result = "Even" if number % 2 == 0 else "Odd"

print(result)
```

Output

```text
Even
```

---

# Find Largest Number

```python
a = 10
b = 20

largest = a if a > b else b

print(largest)
```

Output

```text
20
```

---

# Find Smallest Number

```python
a = 10
b = 20

smallest = a if a < b else b

print(smallest)
```

Output

```text
10
```

---

# Check Positive or Negative

```python
number = -5

result = "Positive" if number > 0 else "Negative"

print(result)
```

Output

```text
Negative
```

---

# Check Leap Year

```python
year = 2024

result = "Leap Year" if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) else "Not Leap Year"

print(result)
```

---

# Check Empty String

```python
username = ""

result = "Empty" if username == "" else "Not Empty"

print(result)
```

Output

```text
Empty
```

---

# Check Voting Eligibility

```python
age = 19

print("Eligible" if age >= 18 else "Not Eligible")
```

Output

```text
Eligible
```

---

# Use with Function Return

```python
def is_even(number):
    return True if number % 2 == 0 else False

print(is_even(8))
```

Output

```text
True
```

---

# Nested Ternary Operator

```python
marks = 85

grade = (
    "A" if marks >= 90
    else "B" if marks >= 80
    else "C" if marks >= 70
    else "Fail"
)

print(grade)
```

Output

```text
B
```

---

# Ternary with Boolean Values

```python
is_logged_in = True

message = "Welcome" if is_logged_in else "Please Login"

print(message)
```

---

# Ternary with Input

```python
age = int(input("Enter age: "))

status = "Adult" if age >= 18 else "Minor"

print(status)
```

---

# Multiple Conditions

```python
age = 20
has_id = True

result = "Entry Allowed" if age >= 18 and has_id else "Entry Denied"

print(result)
```

---

# Ternary vs if...else

## Normal if...else

```python
number = 10

if number > 0:
    result = "Positive"
else:
    result = "Negative"

print(result)
```

---

## Ternary Operator

```python
number = 10

result = "Positive" if number > 0 else "Negative"

print(result)
```

---

# Advantages

- ✅ Shorter code
- ✅ Easy for simple decisions
- ✅ Improves readability for one-line conditions
- ✅ Common in interviews

---

# Disadvantages

- ❌ Hard to read if nested too much
- ❌ Avoid for complex logic

---

# Common Mistakes

## ❌ Wrong Order

Wrong

```python
condition if True else False
```

Correct

```python
True if condition else False
```

---

## ❌ Missing `else`

Wrong

```python
result = "Pass" if marks >= 40
```

Correct

```python
result = "Pass" if marks >= 40 else "Fail"
```

---

## ❌ Using for Complex Logic

Avoid writing very long nested ternary expressions.

Bad

```python
result = "A" if x > 90 else "B" if x > 80 else "C" if x > 70 else "D" if x > 60 else "Fail"
```

Better

```python
if x > 90:
    result = "A"
elif x > 80:
    result = "B"
elif x > 70:
    result = "C"
else:
    result = "Fail"
```

---

# Time Complexity

| Statement | Complexity |
|-----------|------------|
| Ternary Operator | O(1) |

The condition is evaluated once, so it takes constant time.

---

# Interview Questions

### What is a ternary operator?

A one-line shortcut for an `if...else` statement.

---

### Syntax?

```python
value_if_true if condition else value_if_false
```

---

### Can ternary operators be nested?

✅ Yes.

But too much nesting reduces readability.

---

### When should you use a ternary operator?

Use it for **simple decisions** that fit comfortably on one line.

---

# Summary

- Ternary operator is a **short form of `if...else`**.
- Syntax:

```python
value_if_true if condition else value_if_false
```

- Best for simple conditions.
- Returns one of two values based on a condition.
- Can be nested, but avoid excessive nesting.
- Runs in **O(1)** time.