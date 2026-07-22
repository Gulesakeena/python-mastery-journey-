# Python Modules

## Objective

Learn how Python modules work, how to import them, create your own modules, and organize code effectively.

---

# What is a Module?

A module is a Python file (`.py`) that contains functions, variables, classes, or executable code which can be reused in other Python programs.

Example:

```
calculator.py
```

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

Use it in another file:

```python
import calculator

print(calculator.add(5, 3))
```

Output

```
8
```

---

# Why Use Modules?

- Code Reusability
- Better Code Organization
- Easier Maintenance
- Avoid Writing Duplicate Code
- Share Code Across Projects

---

# Types of Modules

## 1. Built-in Modules

Already included with Python.

Examples

- math
- random
- os
- sys
- time
- datetime
- statistics
- collections
- itertools

Example

```python
import math

print(math.sqrt(25))
```

Output

```
5.0
```

---

## 2. User-Defined Modules

Modules created by the programmer.

Example

```
greetings.py
```

```python
def hello():
    print("Hello World")
```

Main file

```python
import greetings

greetings.hello()
```

---

## 3. Third-Party Modules

Installed using pip.

Examples

- numpy
- pandas
- requests
- flask
- django
- matplotlib

Installation

```bash
pip install requests
```

Example

```python
import requests
```

---

# Importing Modules

## Import Entire Module

```python
import math

print(math.sqrt(49))
```

---

## Import Specific Function

```python
from math import sqrt

print(sqrt(49))
```

---

## Import Multiple Functions

```python
from math import sqrt, factorial

print(sqrt(25))
print(factorial(5))
```

---

## Import Everything

```python
from math import *
```

Not recommended because it can create name conflicts.

---

## Import with Alias

```python
import math as m

print(m.sqrt(36))
```

---

Another example

```python
import numpy as np
```

---

# Using dir()

Shows everything inside a module.

```python
import math

print(dir(math))
```

---

# Using help()

Displays module documentation.

```python
import math

help(math)
```

---

# Common Built-in Modules

## math

Provides mathematical functions.

```python
import math

print(math.sqrt(64))
print(math.factorial(5))
print(math.pi)
```

---

## random

Generates random values.

```python
import random

print(random.randint(1, 10))
```

Random choice

```python
names = ["Ali", "Sara", "Ahmed"]

print(random.choice(names))
```

Random float

```python
print(random.random())
```

Shuffle list

```python
numbers = [1,2,3,4,5]

random.shuffle(numbers)

print(numbers)
```

---

## os

Works with operating system.

Current directory

```python
import os

print(os.getcwd())
```

List files

```python
print(os.listdir())
```

Create folder

```python
os.mkdir("Demo")
```

Remove folder

```python
os.rmdir("Demo")
```

Rename file/folder

```python
os.rename("old.txt", "new.txt")
```

---

## sys

Provides system information.

```python
import sys

print(sys.version)
print(sys.platform)
```

Memory size

```python
numbers = [1,2,3]

print(sys.getsizeof(numbers))
```

---

## time

Working with time.

```python
import time

print(time.time())
```

Pause execution

```python
time.sleep(2)

print("Done")
```

---

## datetime

Working with dates and times.

```python
from datetime import datetime

now = datetime.now()

print(now)
```

Current date

```python
from datetime import date

print(date.today())
```

---

## statistics

Statistical calculations.

```python
import statistics

numbers = [10,20,30,40]

print(statistics.mean(numbers))
print(statistics.median(numbers))
```

---

# Creating Your Own Module

calculator.py

```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
```

main.py

```python
import calculator

print(calculator.add(5,3))
print(calculator.multiply(4,5))
```

---

# Module Search Path

Python searches modules in:

- Current folder
- Standard Library
- Installed packages

View search path

```python
import sys

print(sys.path)
```

---

# __name__ Variable

Every Python file has a special variable called `__name__`.

Example

```python
print(__name__)
```

If the file is run directly

```
__main__
```

If imported

```
module_name
```

---

# if __name__ == "__main__"

Used to prevent code from running when the file is imported.

calculator.py

```python
def add(a,b):
    return a+b

if __name__ == "__main__":
    print(add(5,3))
```

Main file

```python
import calculator
```

Output

```
Nothing is printed automatically.
```

---

# Best Practices

- Use meaningful module names.
- Keep one purpose per module.
- Avoid `from module import *`.
- Group related functions together.
- Write documentation and comments.
- Use aliases only when needed.

---

# Time Complexity

| Operation | Complexity |
|-----------|------------|
| Import Module (first time) | O(1) |
| Function Call | Depends on Function |
| Attribute Access | O(1) |
| Module Lookup | O(1) |

---

# Interview Questions

### What is a module?

A Python file containing reusable code.

---

### Difference between a module and a package?

Module

- Single `.py` file.

Package

- Collection of multiple modules inside a folder.

---

### Difference between import and from...import?

```python
import math

math.sqrt(25)
```

```python
from math import sqrt

sqrt(25)
```

---

### Why use aliases?

To shorten long module names.

Example

```python
import numpy as np
```

---

### Why should we avoid `from module import *`?

Because it imports everything and may create naming conflicts.

---

### What does `__name__ == "__main__"` do?

It ensures code runs only when the file is executed directly, not when imported.

---

# Summary

- Module = Python file containing reusable code.
- Built-in modules come with Python.
- User-defined modules are created by programmers.
- Third-party modules are installed using pip.
- Use `import` or `from ... import`.
- `dir()` lists module contents.
- `help()` shows documentation.
- `__name__ == "__main__"` prevents unwanted execution during imports.
- Modules improve code organization and reusability.
```