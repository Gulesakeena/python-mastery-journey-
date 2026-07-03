# Python Variables Notes

## What is a Variable?

A **variable** is a named container (or memory location) used to store data. The value stored in a variable can be changed during program execution.

Example:

```python
name = "Gule"
age = 21
```

---

# Variable Naming Rules

**Variable naming rules** are the rules that define how variable names must be written in Python.

## Rules

### ✅ A variable name can contain:

* Letters (A–Z, a–z)
* Numbers (0–9)
* Underscore (_)

Examples:

```python
name
student_name
_marks
user1
age2
```

---

### ✅ A variable name must start with:

* A letter
* An underscore (_)

Examples:

```python
name
_age
student
```

---

### ❌ A variable name cannot start with a number

Wrong:

```python
1name
2student
```

Correct:

```python
name1
student2
```

---

### ❌ Spaces are not allowed

Wrong:

```python
my name
student age
```

Correct:

```python
my_name
student_age
```

---

### ❌ Special characters are not allowed

Wrong:

```python
my-name
price$
user@email
```

Correct:

```python
my_name
price
user_email
```

---

### ❌ Python keywords cannot be used as variable names

Wrong:

```python
class = "Python"
for = 10
if = 5
```

Correct:

```python
class_name = "Python"
total_for = 10
condition = 5
```

---

# Variable Naming Convention

A **naming convention** is a recommended style for writing variable names. It improves code readability and consistency.

Python follows the **snake_case** naming convention.

## What is snake_case?

**snake_case** is a naming style where:

* All letters are lowercase.
* Words are separated using an underscore (_).

Examples:

```python
student_name
total_marks
first_name
last_name
phone_number
user_age
```

### ❌ Not snake_case

```python
StudentName
studentName
student-name
student name
```

### ✅ Snake_case

```python
student_name
total_marks
user_email
```

---

# Assign One Value

Assign a single value to a variable.

```python
city = "Sialkot"
```

---

# Assign Multiple Values

Assign multiple values to multiple variables in one line.

```python
name, age, city = "Gule", 21, "Sialkot"
```

---

# Assign the Same Value to Multiple Variables

Assign one value to multiple variables at once.

```python
x = y = z = 100
```

---

# Output Variables

Use the `print()` function to display variable values.

```python
name = "Gule"
print(name)

age = 21
print(age)

print(name, age)
```

Output:

```text
Gule
21
Gule 21
```

---

# Global Variables

A **global variable** is a variable created outside a function. It can be accessed from anywhere in the program.

```python
name = "Gule"

def show():
    print(name)

show()
```

Output:

```text
Gule
```

---

# Best Practices

* Use meaningful and descriptive variable names.
* Follow the **snake_case** naming convention.
* Keep variable names short but clear.
* Avoid single-letter variable names except in loops (such as `i`, `j`, or `k`).
* Do not use Python keywords as variable names.
* Choose names that make your code easy to read and understand.
