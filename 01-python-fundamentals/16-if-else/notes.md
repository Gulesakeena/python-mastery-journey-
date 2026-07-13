# 📘 Python if...else Notes

## What is if...else?

`if...else` is used to make **decisions** in a program.

It allows your program to execute different blocks of code depending on whether a condition is **True** or **False**.

---

# Syntax

```python
if condition:
    # code if condition is True
else:
    # code if condition is False
```

---

# Flow Diagram

```text
          Condition
              │
        ┌─────┴─────┐
        │           │
      True        False
        │           │
   if block    else block
```

---

# Simple Example

```python
age = 20

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")
```

Output

```text
Eligible to vote
```

---

# if Statement

Use `if` when you only want to execute code if the condition is **True**.

```python
temperature = 35

if temperature > 30:
    print("It's hot today.")
```

Output

```text
It's hot today.
```

---

# if...else Statement

```python
number = 10

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Output

```text
Even
```

---

# if...elif...else

Use `elif` to check multiple conditions.

```python
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Fail")
```

Output

```text
Grade C
```

---

# Multiple elif Example

```python
day = 3

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
else:
    print("Invalid Day")
```

---

# Nested if

An `if` statement inside another `if`.

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry Allowed")
    else:
        print("ID Required")
else:
    print("Under Age")
```

---

# Using Logical Operators

## and

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Allowed")
```

---

## or

```python
age = 16
has_permission = True

if age >= 18 or has_permission:
    print("Allowed")
```

---

## not

```python
is_logged_in = False

if not is_logged_in:
    print("Please Login")
```

---

# Comparison Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal | `a == b` |
| `!=` | Not Equal | `a != b` |
| `>` | Greater Than | `a > b` |
| `<` | Less Than | `a < b` |
| `>=` | Greater or Equal | `a >= b` |
| `<=` | Less or Equal | `a <= b` |

---

# Truthy and Falsy Values

Python automatically converts values to Boolean.

## False Values

```python
False
None
0
0.0
''
[]
()
{}
set()
```

Everything else is considered **True**.

---

Example

```python
text = ""

if text:
    print("Not Empty")
else:
    print("Empty")
```

Output

```text
Empty
```

---

# Short-Hand if

```python
age = 20

if age >= 18: print("Adult")
```

---

# Short-Hand if...else (Ternary Operator)

```python
age = 18

result = "Adult" if age >= 18 else "Minor"

print(result)
```

Output

```text
Adult
```

---

# Pass Statement

If you don't want to write code yet.

```python
age = 18

if age >= 18:
    pass
```

---

# Membership in Conditions

```python
letter = "a"

if letter in "apple":
    print("Found")
```

---

# Identity in Conditions

```python
x = None

if x is None:
    print("No Value")
```

---

# Common Beginner Examples

## Check Positive or Negative

```python
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

---

## Check Even or Odd

```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

## Largest of Two Numbers

```python
a = 10
b = 20

if a > b:
    print(a)
else:
    print(b)
```

---

## Leap Year

```python
year = int(input("Enter year: "))

if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not Leap Year")
```

---

## Password Length

```python
password = input("Enter Password: ")

if len(password) >= 8:
    print("Valid Password")
else:
    print("Password Too Short")
```

---

# Common Mistakes

## ❌ Using = instead of ==

Wrong

```python
if age = 18:
```

Correct

```python
if age == 18:
```

---

## ❌ Missing Colon

Wrong

```python
if age > 18
```

Correct

```python
if age > 18:
```

---

## ❌ Wrong Indentation

Wrong

```python
if age > 18:
print("Adult")
```

Correct

```python
if age > 18:
    print("Adult")
```

---

## ❌ Comparing input() Without Conversion

Wrong

```python
age = input("Enter age: ")

if age >= 18:
```

Correct

```python
age = int(input("Enter age: "))

if age >= 18:
```

---

# Best Practices

- Use meaningful variable names.
- Keep conditions simple.
- Use `elif` instead of multiple `if` statements when checking related conditions.
- Avoid deeply nested `if` statements.
- Convert user input to the correct data type before comparison.

---

# Time Complexity

| Statement | Complexity |
|-----------|------------|
| if | O(1) |
| if...else | O(1) |
| if...elif...else | O(1) (single decision) |
| Nested if | Depends on nested operations |

> The `if` statement itself is **O(1)** because checking a condition takes constant time. The overall complexity depends on the code executed inside the block.

---

# Interview Questions

### What is the difference between `if` and `elif`?

- `if` starts the condition.
- `elif` checks another condition only if the previous one was False.

---

### Can an `if` statement exist without `else`?

✅ Yes.

---

### Can there be multiple `elif` statements?

✅ Yes.

---

### Is `else` mandatory?

❌ No.

---

### What is indentation?

Indentation is the spaces before a block of code. Python uses indentation to define code blocks.

---

# Summary

- `if` executes code when a condition is **True**.
- `else` executes when the condition is **False**.
- `elif` checks multiple conditions.
- Use comparison operators (`==`, `>`, `<`, etc.) to create conditions.
- Combine conditions using `and`, `or`, and `not`.
- Proper indentation is required.
- Convert user input to the correct type before comparing.