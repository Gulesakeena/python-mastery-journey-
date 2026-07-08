# 🟢 Python Boolean Cheat Sheet

> A quick reference for Python Boolean values, comparison operators, logical operators, truthy/falsy values, and common interview patterns.

---

# Boolean Values

```python
True
False
```

```python
print(type(True))   # <class 'bool'>
print(type(False))  # <class 'bool'>
```

---

# bool() Function

Converts any value into a Boolean.

```python
bool(value)
```

### Examples

```python
bool(10)        # True
bool(0)         # False
bool(-5)        # True
bool("Python")  # True
bool("")        # False
bool([])        # False
bool([1, 2])    # True
bool({})        # False
bool(None)      # False
```

---

# Truthy vs Falsy

## ✅ Truthy Values

```python
1
-5
3.14
"Hello"
" "
[1]
(1,)
{"a": 1}
{1, 2}
True
```

---

## ❌ Falsy Values

```python
0
0.0
""
[]
()
{}
set()
None
False
```

---

# Comparison Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal | `5 == 5` |
| `!=` | Not Equal | `5 != 3` |
| `>` | Greater Than | `10 > 5` |
| `<` | Less Than | `5 < 10` |
| `>=` | Greater Than or Equal | `5 >= 5` |
| `<=` | Less Than or Equal | `5 <= 8` |

Examples

```python
10 == 10      # True
10 != 5       # True
5 < 10        # True
7 >= 9        # False
```

---

# Assignment vs Comparison

Assignment

```python
x = 10
```

Comparison

```python
x == 10
```

Remember

- `=` → Assign value
- `==` → Compare values

---

# Logical Operators

## AND

Returns `True` only if **both** conditions are `True`.

```python
True and True     # True
True and False    # False
```

Truth Table

| A | B | A and B |
|---|---|----------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

---

## OR

Returns `True` if **at least one** condition is `True`.

```python
True or False     # True
False or False    # False
```

Truth Table

| A | B | A or B |
|---|---|---------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

---

## NOT

Reverses a Boolean value.

```python
not True     # False
not False    # True
```

Truth Table

| A | not A |
|---|-------|
| True | False |
| False | True |

---

# Membership Operators

```python
"a" in "Python"
```

```python
"Py" in "Python"      # True
"Java" in "Python"    # False
```

---

# Identity Operators

```python
is
is not
```

Example

```python
a = [1, 2]
b = a

a is b        # True
```

```python
a = [1, 2]
b = [1, 2]

a == b        # True
a is b        # False
```

---

# Boolean Expressions

```python
age >= 18

marks >= 50

password == "Python123"

number % 2 == 0

number > 0

10 <= age <= 60
```

All return `True` or `False`.

---

# Short-Circuit Evaluation

```python
False and print("Hello")
```

Output

```python
False
```

`print()` is never executed.

---

```python
True or print("Hello")
```

Output

```python
True
```

Again, `print()` is skipped.

---

# Common Patterns

## Positive Number

```python
number > 0
```

---

## Negative Number

```python
number < 0
```

---

## Even Number

```python
number % 2 == 0
```

---

## Odd Number

```python
number % 2 != 0
```

---

## Empty String

```python
text == ""
```

or

```python
not text
```

---

## Empty List

```python
not numbers
```

---

## Username Exists

```python
bool(username)
```

---

## Password Length

```python
len(password) >= 8
```

---

## Number Between 10 and 100

```python
10 <= number <= 100
```

---

# Boolean Functions

```python
def is_even(number):
    return number % 2 == 0
```

---

```python
def is_positive(number):
    return number > 0
```

---

```python
def is_adult(age):
    return age >= 18
```

---

# if Statements

```python
if age >= 18:
    print("Adult")
```

---

```python
if password:
    print("Password entered")
```

---

# Boolean from User Input

```python
age = int(input("Enter age:"))

print(age >= 18)
```

---

# Common Interview Questions

### Check Positive Number

```python
return number > 0
```

---

### Check Even Number

```python
return number % 2 == 0
```

---

### Check Empty String

```python
return text == ""
```

or

```python
return not text
```

---

### Check Password Length

```python
return len(password) >= 8
```

---

### Check Two Numbers are Equal

```python
return a == b
```

---

### Prime Number

```python
return False
return True
```

(Inside a function after checking divisibility.)

---

# Common Mistakes

❌

```python
if x = 5:
```

✅

```python
if x == 5:
```

---

❌

```python
number = input()

if number > 0:
```

✅

```python
number = int(input())

if number > 0:
```

---

❌

```python
if password == "":
```

✅

```python
if not password:
```

---

# Operator Precedence

Highest → Lowest

```
()
not
and
or
```

Example

```python
True and False or True
```

Evaluates as

```python
(True and False) or True
```

↓

```python
False or True
```

↓

```python
True
```

---

# Quick Cheat Sheet

```python
True
False

bool(value)

==
!=
>
<
>=
<=

and
or
not

is
is not

in
not in

number > 0

number % 2 == 0

10 <= number <= 100

not text

len(password) >= 8
```

---

# Remember

- `True` behaves like `1`
- `False` behaves like `0`
- Empty objects are `False`
- Non-empty objects are `True`
- `=` assigns a value
- `==` compares values
- `is` compares object identity
- `and` → All conditions must be `True`
- `or` → At least one condition must be `True`
- `not` → Reverses the Boolean value

---

## 📚 References

- Python Official Documentation: https://docs.python.org/3/library/stdtypes.html#boolean-type-bool
- Truth Value Testing: https://docs.python.org/3/library/stdtypes.html#truth-value-testing
- W3Schools: https://www.w3schools.com/python/python_booleans.asp