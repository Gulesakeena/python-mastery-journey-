# 25 - Python Regular Expressions (RegEx)

## What is RegEx?

Regular Expression (RegEx) is a sequence of characters used to search, match, validate, replace, and extract text.

Python provides the built-in `re` module.

---

# Why Learn RegEx?

RegEx is used in:

- Email validation
- Password validation
- Phone number validation
- Web scraping
- Data cleaning
- AI/NLP preprocessing
- Log analysis
- Search functionality

---

# Import

```python
import re
```

---

# search()

Searches for the first occurrence anywhere in the string.

```python
import re

text = "I love Python"

match = re.search("Python", text)

print(match)
```

---

# match()

Checks only from the beginning of the string.

```python
re.match("Python", "Python is awesome")
```

---

# fullmatch()

The entire string must match.

```python
re.fullmatch(r"\d+", "12345")
```

---

# findall()

Returns all matches.

```python
text = "cat bat rat"

print(re.findall("at", text))
```

Output

```
['at', 'at', 'at']
```

---

# finditer()

Returns match objects.

```python
for match in re.finditer(r"\d+", "A12 B45"):
    print(match.group())
```

---

# split()

```python
re.split(",", "A,B,C,D")
```

---

# sub()

Replace text.

```python
re.sub("Python", "Java", text)
```

---

# Metacharacters

| Symbol | Meaning |
|---------|----------|
| . | Any character |
| ^ | Start |
| $ | End |
| * | 0 or more |
| + | 1 or more |
| ? | Optional |
| [] | Character class |
| () | Group |
| {} | Repetition |
| \| | OR |
| \ | Escape |

---

# Character Classes

```python
\d
```

Digit

```python
\D
```

Not Digit

```python
\w
```

Letter, digit, underscore

```python
\W
```

Non-word

```python
\s
```

Whitespace

```python
\S
```

Non-whitespace

---

# Quantifiers

Exactly 3 digits

```python
\d{3}
```

2–5 digits

```python
\d{2,5}
```

One or more

```python
+
```

Zero or more

```python
*
```

Optional

```python
?
```

---

# Groups

```python
match = re.search(r"(\d+)-(\d+)", "123-456")

print(match.group(1))
print(match.group(2))
```

---

# Common Patterns

Email

```python
r'^[\w\.-]+@[\w\.-]+\.\w+$'
```

Phone Number

```python
r'^\d{11}$'
```

Password (Minimum 8 characters)

```python
r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$'
```

CNIC (Pakistan)

```python
r'^\d{5}-\d{7}-\d$'
```

ZIP Code

```python
r'^\d{5}$'
```

---

# Best Practices

- Use raw strings (`r""`) for regex patterns.
- Test patterns before deployment.
- Keep patterns readable.
- Use `fullmatch()` for validation.

---

# Interview Questions

## Difference between search() and match()?

- `search()` looks anywhere.
- `match()` checks only from the start.

---

## Difference between match() and fullmatch()?

- `match()` checks the beginning.
- `fullmatch()` checks the entire string.

---

## Which function replaces text?

```python
re.sub()
```

---

## Which function returns all matches?

```python
re.findall()
```

---

# Key Takeaways

- Import using `import re`.
- Use `search()` for searching.
- Use `fullmatch()` for validation.
- Use `findall()` to collect all matches.
- Use `sub()` to replace text.