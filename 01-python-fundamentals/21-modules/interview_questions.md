# Python Modules - Interview Questions

## Theory

1. What is a module?
2. Why do we use modules?
3. Difference between a module and a package?
4. Explain `import`.
5. Explain `from module import ...`.
6. Why avoid `from module import *`?
7. What is `__name__`?
8. What is `__main__`?
9. How does Python find imported modules?
10. What are built-in modules?

---

## Coding Questions

1. Create your own calculator module.
2. Create a geometry module with area functions.
3. Create a temperature converter module.
4. Import a module using an alias.
5. Import only one function from a module.

---

## Output Prediction

### Question 1

```python
# file1.py
print(__name__)
```

Run directly.

What will be printed?

---

### Question 2

```python
# file1.py
print(__name__)

# file2.py
import file1
```

What will `file1.py` print when imported?

---

## Common Interview Mistakes

- Confusing modules with packages.
- Using wildcard imports everywhere.
- Forgetting the purpose of `if __name__ == "__main__":`.