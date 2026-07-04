# Common Mistakes in Python Numbers

This document lists the most common mistakes beginners make while working with Python numbers. Understanding these mistakes will help you write cleaner code and avoid common interview pitfalls.

---

# 1. Forgetting to Convert `input()`

## ❌ Wrong

```python
age = input("Enter your age: ")

result = age + 5
```

### Error

```
TypeError
```

## ✅ Correct

```python
age = int(input("Enter your age: "))

result = age + 5
```

### Why?

`input()` always returns a **string**, even if the user enters a number.

---

# 2. Using `/` Instead of `//`

## ❌ Wrong

```python
print(15 / 2)
```

Output

```
7.5
```

If you need a whole number, this is incorrect.

## ✅ Correct

```python
print(15 // 2)
```

Output

```
7
```

---

# 3. Confusing `%` with Division

## ❌ Wrong

```python
print(15 % 2)
```

Expected

```
7.5
```

Actual

```
1
```

## Why?

The `%` operator returns the **remainder**, not the quotient.

---

# 4. Forgetting Operator Precedence

## ❌ Wrong

```python
result = 10 + 5 * 2
```

Many beginners expect:

```
30
```

Actual Output

```
20
```

## ✅ Correct

```python
result = (10 + 5) * 2
```

Output

```
30
```

---

# 5. Using `=` Instead of `==`

## ❌ Wrong

```python
if age = 18:
```

## ✅ Correct

```python
if age == 18:
```

### Why?

* `=` assigns a value.
* `==` compares two values.

---

# 6. Forgetting Parentheses in Functions

## ❌ Wrong

```python
print
```

## ✅ Correct

```python
print("Hello")
```

Functions must be called using parentheses.

---

# 7. Using `len()` on an Integer

## ❌ Wrong

```python
number = 12345

print(len(number))
```

### Error

```
TypeError
```

## ✅ Correct

```python
print(len(str(number)))
```

or count digits using a loop.

---

# 8. Comparing Numbers with Strings

## ❌ Wrong

```python
age = "21"

if age == 21:
    print("Equal")
```

Output

```
False
```

## ✅ Correct

```python
age = int(age)

if age == 21:
    print("Equal")
```

---

# 9. Forgetting to Store the Original Number

## ❌ Wrong

```python
number = 123

while number > 0:
    number //= 10

print(number)
```

Output

```
0
```

The original value is lost.

## ✅ Correct

```python
number = 123
original = number
```

Always save the original value before modifying it.

---

# 10. Using `&` Instead of `and`

## ❌ Wrong

```python
if a > b & a > c:
```

## ✅ Correct

```python
if a > b and a > c:
```

`and` is the logical operator.

`&` is a bitwise operator.

---

# 11. Confusing `round()` with `int()`

## ❌ Wrong

```python
print(int(3.9))
```

Output

```
3
```

Some beginners expect:

```
4
```

## ✅ Correct

```python
print(round(3.9))
```

Output

```
4
```

---

# 12. Forgetting That `bool` is a Subclass of `int`

```python
print(True + True)
```

Output

```
2
```

Why?

```
True = 1
False = 0
```

---

# 13. Division by Zero

## ❌ Wrong

```python
print(10 / 0)
```

### Error

```
ZeroDivisionError
```

Always ensure the denominator is not zero.

---

# 14. Using `^` for Power

## ❌ Wrong

```python
print(2 ^ 3)
```

Output

```
1
```

`^` is the **bitwise XOR** operator.

## ✅ Correct

```python
print(2 ** 3)
```

Output

```
8
```

---

# 15. Assuming Floating-Point Numbers Are Always Exact

## ❌ Example

```python
print(0.1 + 0.2)
```

Output

```
0.30000000000000004
```

This happens because floating-point numbers are stored in binary and cannot exactly represent some decimal fractions.

---

# Interview Tips

* Convert user input using `int()` or `float()` before calculations.
* Use `//` for floor division and `%` for the remainder.
* Use `**` instead of `^` for exponents.
* Save the original number before modifying it.
* Use `and`, `or`, and `not` for logical conditions.
* Remember that `True` behaves like `1` and `False` behaves like `0`.
* Be careful when comparing numbers with strings.
* Understand the difference between `int()`, `float()`, and `round()`.

---

# Summary

Avoiding these common mistakes will help you:

* Write cleaner Python code.
* Debug programs more quickly.
* Build a strong understanding of numeric operations.
* Perform better in coding interviews.
