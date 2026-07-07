# Python String Methods Cheat Sheet

A quick reference for the most commonly used Python string methods.

---

# Case Conversion

| Method | Description | Example | Output |
|---------|-------------|---------|--------|
| `upper()` | Converts all letters to uppercase | `"python".upper()` | `"PYTHON"` |
| `lower()` | Converts all letters to lowercase | `"PYTHON".lower()` | `"python"` |
| `capitalize()` | Capitalizes the first letter | `"python".capitalize()` | `"Python"` |
| `title()` | Capitalizes the first letter of each word | `"hello world".title()` | `"Hello World"` |
| `swapcase()` | Swaps uppercase and lowercase letters | `"PyThOn".swapcase()` | `"pYtHoN"` |
| `casefold()` | Aggressive lowercase conversion (best for comparisons) | `"Straße".casefold()` | `"strasse"` |

---

# Whitespace Removal

| Method | Description | Example | Output |
|---------|-------------|---------|--------|
| `strip()` | Removes spaces from both sides | `"  Python  ".strip()` | `"Python"` |
| `lstrip()` | Removes spaces from the left | `"  Python".lstrip()` | `"Python"` |
| `rstrip()` | Removes spaces from the right | `"Python  ".rstrip()` | `"Python"` |

---

# Searching

| Method | Description | Example | Output |
|---------|-------------|---------|--------|
| `find()` | Returns first index, `-1` if not found | `"Python".find("t")` | `2` |
| `rfind()` | Finds last occurrence | `"banana".rfind("a")` | `5` |
| `index()` | Same as `find()`, but raises an error if not found | `"Python".index("t")` | `2` |
| `rindex()` | Last index, raises error if not found | `"banana".rindex("a")` | `5` |
| `count()` | Counts occurrences | `"banana".count("a")` | `3` |
| `startswith()` | Checks beginning | `"Python".startswith("Py")` | `True` |
| `endswith()` | Checks ending | `"Python".endswith("on")` | `True` |

---

# Replace & Split

| Method | Description | Example | Output |
|---------|-------------|---------|--------|
| `replace()` | Replaces text | `"I like Java".replace("Java","Python")` | `"I like Python"` |
| `split()` | Splits into a list | `"a,b,c".split(",")` | `['a','b','c']` |
| `rsplit()` | Splits from the right | `"a,b,c".rsplit(",",1)` | `['a,b','c']` |
| `splitlines()` | Splits at new lines | `"a\nb".splitlines()` | `['a','b']` |
| `partition()` | Splits into 3 parts | `"apple-banana".partition("-")` | `('apple','-','banana')` |
| `rpartition()` | Partitions from the right | `"a-b-c".rpartition("-")` | `('a-b','-','c')` |
| `join()` | Joins iterable into one string | `" ".join(["Hello","World"])` | `"Hello World"` |

---

# Character Checking

| Method | Description | Example | Output |
|---------|-------------|---------|--------|
| `isalpha()` | Only letters | `"Python".isalpha()` | `True` |
| `isdigit()` | Only digits | `"123".isdigit()` | `True` |
| `isdecimal()` | Decimal digits only | `"123".isdecimal()` | `True` |
| `isnumeric()` | Numeric characters | `"½".isnumeric()` | `True` |
| `isalnum()` | Letters or digits | `"Python123".isalnum()` | `True` |
| `isspace()` | Only whitespace | `"   ".isspace()` | `True` |
| `islower()` | All lowercase | `"python".islower()` | `True` |
| `isupper()` | All uppercase | `"PYTHON".isupper()` | `True` |
| `istitle()` | Title case | `"Hello World".istitle()` | `True` |
| `isidentifier()` | Valid Python identifier | `"my_var".isidentifier()` | `True` |
| `isprintable()` | Printable characters only | `"Hello".isprintable()` | `True` |
| `isascii()` | ASCII characters only | `"Python".isascii()` | `True` |

---

# Alignment & Padding

| Method | Description | Example | Output |
|---------|-------------|---------|--------|
| `center()` | Centers text | `"Python".center(10)` | `"  Python  "` |
| `ljust()` | Left aligns | `"Python".ljust(10)` | `"Python    "` |
| `rjust()` | Right aligns | `"Python".rjust(10)` | `"    Python"` |
| `zfill()` | Pads with zeros | `"42".zfill(5)` | `"00042"` |

---

# Formatting

| Method | Description | Example | Output |
|---------|-------------|---------|--------|
| `format()` | Formats string | `"Hello {}".format("Ali")` | `"Hello Ali"` |
| `format_map()` | Formats using a mapping | `"{name}".format_map({"name":"Ali"})` | `"Ali"` |

---

# Encoding

| Method | Description | Example |
|---------|-------------|---------|
| `encode()` | Converts string to bytes | `"Python".encode()` |

---

# Tabs

| Method | Description | Example |
|---------|-------------|---------|
| `expandtabs()` | Replaces `\t` with spaces | `"A\tB".expandtabs(4)` |

---

# Translation

| Method | Description |
|---------|-------------|
| `maketrans()` | Creates translation table |
| `translate()` | Replaces characters using translation table |

Example:

```python
table = str.maketrans("ae", "12")
text = "apple"

print(text.translate(table))
```

Output:

```
1ppl2
```

---

# Useful Operators

| Operator | Description |
|----------|-------------|
| `+` | Concatenate strings |
| `*` | Repeat string |
| `in` | Membership test |
| `not in` | Not a member |
| `==` | Equal |
| `!=` | Not equal |
| `<` | Less than |
| `>` | Greater than |

---

# Useful Built-in Functions

| Function | Description |
|----------|-------------|
| `len()` | Returns string length |
| `ord()` | Returns Unicode code point |
| `chr()` | Returns character from Unicode |
| `sorted()` | Returns sorted characters |
| `reversed()` | Returns reverse iterator |

---

# Escape Characters

| Escape | Meaning |
|---------|---------|
| `\n` | New line |
| `\t` | Tab |
| `\\` | Backslash |
| `\'` | Single quote |
| `\"` | Double quote |
| `\r` | Carriage return |
| `\b` | Backspace |

---

# Raw Strings

```python
path = r"C:\Users\Ali\Documents"
```

---

# String Formatting (Recommended)

```python
name = "Ali"
age = 20

print(f"My name is {name} and I am {age} years old.")
```

---

# Most Frequently Used Methods

- `upper()`
- `lower()`
- `strip()`
- `replace()`
- `split()`
- `join()`
- `find()`
- `count()`
- `startswith()`
- `endswith()`
- `isalpha()`
- `isdigit()`
- `isalnum()`
- `islower()`
- `isupper()`

---

# Best Practices

- ✅ Use `f-strings` for formatting.
- ✅ Use `find()` if you don't want an exception when text is missing.
- ✅ Use `index()` only when the substring must exist.
- ✅ Use `strip()` to remove unwanted spaces from user input.
- ✅ Use `join()` instead of repeatedly using `+` in loops.
- ✅ Remember that **strings are immutable**—methods return new strings instead of modifying the original.

---

# Official Documentation

- Python Standard Library: https://docs.python.org/3/library/stdtypes.html#string-methods
- W3Schools Python Strings: https://www.w3schools.com/python/python_strings.asp