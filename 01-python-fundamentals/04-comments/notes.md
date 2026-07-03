# Python Comments Notes

## What is a Comment?

A comment is text written inside your code that Python ignores during execution.

Comments are written to explain code and improve readability.

---

## Single-Line Comment

A single-line comment starts with `#`.

Example:

```python
# This is a comment
print("Hello")
```

---

## Multi-Line Comment

Python does not have a special syntax for multi-line comments.

Developers usually use multiple `#` lines:

```python
# This program prints
# the user's name
# and age.
```

Sometimes triple quotes (`""" """`) are used as documentation strings (docstrings), but they are **not** true comments.

Example:

```python
"""
This is a docstring.
"""
```

---

## Why Use Comments?

- Explain complex logic.
- Make code easier to read.
- Help other developers.
- Help your future self understand the code.

---

## Best Practices

✅ Write comments that explain **why**, not obvious things.

Good:

```python
# Convert Celsius to Fahrenheit
```

Not useful:

```python
# Print hello
print("Hello")
```