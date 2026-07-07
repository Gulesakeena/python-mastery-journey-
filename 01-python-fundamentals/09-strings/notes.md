# Python Strings Complete Notes

## 1. Introduction to Strings

A string is a sequence of characters enclosed inside quotes.

Python strings are immutable, meaning once a string is created, its value cannot be changed.

Examples:

```python
name = "Ali"
message = 'Hello World'
text = """This is
a multi-line
string"""
```

Python allows three types of quotes:

```python
"Double quotes"

'Single quotes'

"""Triple quotes for multi-line strings"""
```

---

# 2. Creating Strings

## Single Line String

```python
name = "Python"
```

## Multi-Line String

```python
description = """
Python is a high-level,
interpreted programming language.
"""
```

## Empty String

```python
empty = ""
```

---

# 3. String Immutability

Strings cannot be changed after creation.

Example:

```python
name = "Python"

name[0] = "J"
```

Output:

```
TypeError: 'str' object does not support item assignment
```

Correct way:

```python
name = "Python"
new_name = "J" + name[1:]

print(new_name)
```

Output:

```
Jython
```

---

# 4. String Indexing

Each character in a string has an index position.

Example:

```python
text = "Python"

print(text[0])
print(text[1])
```

Output:

```
P
y
```

Index starts from `0`.

```
P  y  t  h  o  n
0  1  2  3  4  5
```

---

# 5. Negative Indexing

Python supports negative indexes.

Example:

```python
text = "Python"

print(text[-1])
print(text[-2])
```

Output:

```
n
o
```

```
P   y   t   h   o   n
-6 -5  -4  -3  -2  -1
```

---

# 6. String Slicing

Syntax:

```python
string[start:end:step]
```

Example:

```python
text = "Python"

print(text[0:3])
```

Output:

```
Pyt
```

Note:
- Start index included
- End index excluded


## Examples

```python
text = "Python"

print(text[:])
```

Output:

```
Python
```


```python
print(text[2:])
```

Output:

```
thon
```


```python
print(text[:4])
```

Output:

```
Pyth
```


```python
print(text[::2])
```

Output:

```
Pto
```


Reverse string:

```python
text = "Python"

print(text[::-1])
```

Output:

```
nohtyP
```

---

# 7. Loop Through String

Example:

```python
for char in "Python":
    print(char)
```

Output:

```
P
y
t
h
o
n
```

---

# 8. String Length

Use `len()` function.

```python
text = "Python"

print(len(text))
```

Output:

```
6
```

---

# 9. Check String Membership

Use:

- `in`
- `not in`

Example:

```python
text = "Python"

print("Py" in text)

print("Java" not in text)
```

Output:

```
True
True
```

---

# 10. String Concatenation

Joining strings using `+`.

Example:

```python
first = "Hello"
second = "World"

result = first + second

print(result)
```

Output:

```
HelloWorld
```

With space:

```python
result = first + " " + second
```

Output:

```
Hello World
```

---

# 11. String Repetition

Using `*`.

Example:

```python
word = "Hi"

print(word * 3)
```

Output:

```
HiHiHi
```

---

# 12. String Escape Characters

Escape characters allow special characters.

| Escape | Meaning |
|---|---|
| \n | New line |
| \t | Tab |
| \\ | Backslash |
| \' | Single quote |
| \" | Double quote |

Examples:

```python
print("Hello\nWorld")
```

Output:

```
Hello
World
```

Example:

```python
print("Hello\tPython")
```

Output:

```
Hello   Python
```

---

# 13. Raw Strings

Raw strings ignore escape characters.

Use:

```python
r"string"
```

Example:

```python
path = r"C:\Users\Python"

print(path)
```

Output:

```
C:\Users\Python
```

---

# 14. String Methods

Python provides many built-in string methods.

---

# 15. upper()

Converts string into uppercase.

```python
text = "python"

print(text.upper())
```

Output:

```
PYTHON
```

---

# 16. lower()

Converts string into lowercase.

```python
text = "PYTHON"

print(text.lower())
```

Output:

```
python
```

---

# 17. capitalize()

First character uppercase.

```python
text = "python"

print(text.capitalize())
```

Output:

```
Python
```

---

# 18. title()

First letter of every word uppercase.

```python
text = "python programming"

print(text.title())
```

Output:

```
Python Programming
```

---

# 19. swapcase()

Changes uppercase to lowercase and vice versa.

```python
text = "PyThOn"

print(text.swapcase())
```

Output:

```
pYtHoN
```

---

# 20. strip()

Removes spaces from beginning and end.

```python
text = "  Python  "

print(text.strip())
```

Output:

```
Python
```

---

# 21. lstrip()

Removes left spaces.

```python
text.lstrip()
```

---

# 22. rstrip()

Removes right spaces.

```python
text.rstrip()
```

---

# 23. replace()

Replace characters.

Syntax:

```python
string.replace(old,new)
```

Example:

```python
text="I like Java"

print(text.replace("Java","Python"))
```

Output:

```
I like Python
```

---

# 24. split()

Convert string into list.

Example:

```python
text="Python Java C++"

print(text.split())
```

Output:

```
['Python','Java','C++']
```

Using separator:

```python
data="apple,banana,orange"

print(data.split(","))
```

---

# 25. join()

Join list elements into string.

Example:

```python
words=["Python","is","easy"]

result=" ".join(words)

print(result)
```

Output:

```
Python is easy
```

---

# 26. find()

Returns index of first occurrence.

Example:

```python
text="Pythoon"

print(text.find("o"))
```

Output:

```
4
```

Returns:

```
-1
```

if not found.

---

# 27. index()

Same as find but gives error if not found.

```python
text.index("z")
```

---

# 28. count()

Counts occurrences.

Example:

```python
text="banana"

print(text.count("a"))
```

Output:

```
3
```

---

# 29. startswith()

Checks starting characters.

```python
text="Python"

print(text.startswith("Py"))
```

Output:

```
True
```

---

# 30. endswith()

Checks ending characters.

```python
text.endswith("on")
```

---

# 31. isalpha()

Checks only alphabets.

```python
"Python".isalpha()
```

Output:

```
True
```

---

# 32. isdigit()

Checks digits.

```python
"123".isdigit()
```

Output:

```
True
```

---

# 33. isalnum()

Checks letters and numbers.

```python
"Python123".isalnum()
```

Output:

```
True
```

---

# 34. isspace()

Checks whitespace.

```python
"   ".isspace()
```

Output:

```
True
```

---

# 35. String Formatting

## Old Style Formatting

```python
name="Ali"

print("Hello %s" % name)
```

---

# 36. format()

Example:

```python
name="Ali"

print("Hello {}".format(name))
```

---

# 37. f-string (Recommended)

Modern Python way.

```python
name="Ali"
age=20

print(f"My name is {name} and age is {age}")
```

Output:

```
My name is Ali and age is 20
```

---

# 38. String Formatting Numbers

```python
price=100

print(f"Price: {price:.2f}")
```

Output:

```
Price: 100.00
```

---

# 39. Unicode Strings

Python 3 strings support Unicode.

Example:

```python
text="Hello 😊"

print(text)
```

---

# 40. Comparing Strings

Python compares strings using Unicode values.

Example:

```python
print("apple"=="apple")

print("a"<"b")
```

---

# 41. String Algorithms Practice

## Reverse String

```python
text="Python"

reverse=text[::-1]

print(reverse)
```

---

## Count Characters

```python
text="python"

for char in text:
    print(char)
```

---

## Check Palindrome

```python
text="madam"

if text == text[::-1]:
    print("Palindrome")
```

---

## Count Vowels

```python
text="python"

count=0

for char in text:
    if char in "aeiou":
        count+=1

print(count)
```

---

# 42. Important String Interview Questions

1. Reverse a string.
2. Check palindrome string.
3. Count vowels and consonants.
4. Find duplicate characters.
5. Remove duplicate characters.
6. Find longest word.
7. Check anagram strings.
8. Count frequency of characters.
9. Convert uppercase to lowercase.
10. Find substring.

---

# 43. Important Notes

- Strings are immutable.
- Strings are ordered collections.
- Strings support indexing and slicing.
- Strings can contain Unicode characters.
- Python provides many built-in string methods.
- Use f-strings for modern formatting.
- Use `#` for comments, not triple quotes.

---

# Official Documentation Reference

Python String Documentation:

https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

W3Schools Python Strings:

https://www.w3schools.com/python/python_strings.asp