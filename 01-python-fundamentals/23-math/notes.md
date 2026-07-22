# 23 - Python Math

## What is the Math Module?

The `math` module is a built-in Python module that provides mathematical functions and constants.

Instead of writing complex mathematical formulas manually, Python provides ready-made functions.

---

# Importing the Module

```python
import math
```

---

# Mathematical Constants

## π (Pi)

```python
import math

print(math.pi)
```

Output

```
3.141592653589793
```

---

## Euler's Number (e)

```python
print(math.e)
```

Output

```
2.718281828459045
```

---

# Square Root

```python
math.sqrt(25)
```

Output

```
5.0
```

---

# Power

```python
math.pow(2,5)
```

Output

```
32.0
```

> **Note:** `math.pow()` always returns a float. The `**` operator usually returns an integer if both operands are integers.

```python
2 ** 5
```

Output

```
32
```

---

# Absolute Value

```python
abs(-25)
```

Output

```
25
```

---

# Ceiling

Rounds upward.

```python
math.ceil(4.2)
```

Output

```
5
```

---

# Floor

Rounds downward.

```python
math.floor(4.9)
```

Output

```
4
```

---

# Factorial

```python
math.factorial(5)
```

Output

```
120
```

---

# Greatest Common Divisor

```python
math.gcd(12,18)
```

Output

```
6
```

---

# Logarithm

Natural logarithm

```python
math.log(10)
```

Base 10

```python
math.log10(100)
```

---

# Exponential

```python
math.exp(2)
```

Returns

```
e²
```

---

# Trigonometric Functions

```python
math.sin()
math.cos()
math.tan()
```

These functions use **radians**, not degrees.

---

# Degree to Radian

```python
math.radians(90)
```

---

# Radian to Degree

```python
math.degrees(1.57)
```

---

# Infinity

```python
math.inf
```

---

# Not a Number

```python
math.nan
```

---

# Check Infinity

```python
math.isinf(math.inf)
```

---

# Check NaN

```python
math.isnan(math.nan)
```

---

# Difference Between Built-in and Math Functions

Built-in

```python
abs(-10)
round(3.7)
pow(2,5)
```

Math Module

```python
math.sqrt()
math.factorial()
math.ceil()
math.floor()
math.log()
```

---

# Real-Life Uses

- AI algorithms
- Machine Learning
- Physics simulations
- Financial calculations
- Data Science
- Game development
- Robotics
- Graphics programming

---

# Interview Questions

## Q1. Difference between `pow()` and `math.pow()`?

- `pow()` (built-in) may return an integer.
- `math.pow()` always returns a float.

---

## Q2. Difference between `round()`, `ceil()`, and `floor()`?

- `round()` → nearest value
- `ceil()` → always up
- `floor()` → always down

---

## Q3. Which module contains `sqrt()`?

```python
math
```

---

## Q4. Which function calculates factorial?

```python
math.factorial()
```

---

## Q5. Which constant stores π?

```python
math.pi
```

---

# Key Takeaways

- Import the module using `import math`.
- Use `sqrt()` for square roots.
- Use `factorial()` for factorial calculations.
- Use `ceil()` and `floor()` for rounding.
- Use `pi` and `e` for mathematical constants.
- Trigonometric functions work with radians.