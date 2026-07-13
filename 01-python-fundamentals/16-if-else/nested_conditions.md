# 📘 Python Nested Conditions

## What are Nested Conditions?

A **nested condition** means placing one `if` statement **inside another `if` statement**.

It is used when you want to check **multiple levels of conditions**.

---

# Syntax

```python
if condition1:
    if condition2:
        # Code
    else:
        # Code
else:
    # Code
```

---

# Flow Diagram

```text
           Condition 1
                │
         ┌──────┴──────┐
         │             │
      True          False
         │             │
   Condition 2      else block
         │
    ┌────┴────┐
    │         │
  True      False
    │         │
 if block  else block
```

---

# Basic Example

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

Output

```text
Entry Allowed
```

---

# Example 2: Student Result

```python
marks = 85
attendance = 90

if marks >= 40:
    if attendance >= 75:
        print("Pass")
    else:
        print("Low Attendance")
else:
    print("Fail")
```

Output

```text
Pass
```

---

# Example 3: Login System

```python
username = "admin"
password = "12345678"

if username == "admin":
    if password == "12345678":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")
```

---

# Example 4: ATM System

```python
balance = 5000
pin = 1234

entered_pin = 1234
amount = 2000

if entered_pin == pin:
    if amount <= balance:
        print("Transaction Successful")
    else:
        print("Insufficient Balance")
else:
    print("Invalid PIN")
```

---

# Example 5: Voting System

```python
age = 20
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to Vote")
    else:
        print("Not a Citizen")
else:
    print("Under Age")
```

---

# Example 6: Scholarship

```python
cgpa = 3.8
income = 30000

if cgpa >= 3.5:
    if income < 50000:
        print("Scholarship Approved")
    else:
        print("Income Too High")
else:
    print("CGPA Too Low")
```

---

# Example 7: Number Check

```python
number = 12

if number > 0:
    if number % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    print("Negative Number")
```

---

# Example 8: File Permission

```python
logged_in = True
is_admin = False

if logged_in:
    if is_admin:
        print("Access Granted")
    else:
        print("Admin Permission Required")
else:
    print("Please Login")
```

---

# Nested `if` vs `and`

## Nested `if`

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Allowed")
```

---

## Using `and`

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Allowed")
```

Both produce the same result.

For simple conditions, `and` is usually shorter and easier to read.

---

# Nested `if` with `elif`

```python
marks = 72

if marks >= 40:
    if marks >= 90:
        print("A Grade")
    elif marks >= 80:
        print("B Grade")
    elif marks >= 70:
        print("C Grade")
    else:
        print("Pass")
else:
    print("Fail")
```

---

# Multiple Levels

```python
age = 22
has_id = True
ticket = True

if age >= 18:
    if has_id:
        if ticket:
            print("Entry Allowed")
        else:
            print("Ticket Required")
    else:
        print("ID Required")
else:
    print("Under Age")
```

---

# Common Mistakes

## ❌ Wrong Indentation

Wrong

```python
if age >= 18:
if has_id:
    print("Allowed")
```

Correct

```python
if age >= 18:
    if has_id:
        print("Allowed")
```

---

## ❌ Unnecessary Nesting

Bad

```python
if age >= 18:
    if has_id:
        print("Allowed")
```

Better

```python
if age >= 18 and has_id:
    print("Allowed")
```

---

## ❌ Forgetting `else`

```python
if age >= 18:
    if has_id:
        print("Allowed")
```

If `has_id` is `False`, nothing happens.

Better

```python
if age >= 18:
    if has_id:
        print("Allowed")
    else:
        print("ID Required")
```

---

# When to Use Nested Conditions

Use nested conditions when:

- One condition depends on another.
- Building login systems.
- ATM applications.
- Student management systems.
- Role-based access control.
- Menu-driven programs.

---

# Time Complexity

The `if` statements themselves take constant time. The total complexity depends on the operations inside them.

| Statement | Complexity |
|-----------|------------|
| Single `if` | O(1) |
| Nested `if` | O(1) (for condition checks) |

Example:

```python
if a:
    if b:
        print("Hello")
```

Only two conditions are checked, so the condition checking is **O(1)**.

---

# Interview Questions

### What is a nested `if`?

A nested `if` is an `if` statement placed inside another `if` statement.

---

### When should you use nested conditions?

When the second condition should only be checked if the first condition is `True`.

---

### Can nested `if` statements have `elif` and `else`?

✅ Yes.

---

### Is `and` better than nested `if`?

- For simple conditions, **yes**.
- For dependent or multi-level logic, nested `if` is often clearer.

---

# Real-Life Examples

| Situation | First Condition | Second Condition |
|-----------|-----------------|------------------|
| ATM | Correct PIN | Enough Balance |
| Login | Username Correct | Password Correct |
| Voting | Age ≥ 18 | Citizen |
| Scholarship | CGPA Requirement | Income Requirement |
| Cinema | Age Allowed | Ticket Purchased |

---

# Summary

- A **nested condition** is an `if` inside another `if`.
- It is used for **multi-level decision making**.
- Python uses **indentation** to define nested blocks.
- Avoid unnecessary nesting; use `and` when conditions are simple.
- Nested conditions are common in real-world programs such as login systems, ATMs, and student management systems.