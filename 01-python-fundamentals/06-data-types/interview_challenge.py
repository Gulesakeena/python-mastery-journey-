
"""
===========================================================
Python Data Types - Interview Challenges & Solutions
===========================================================

Author : Gule
Purpose:
    Practice Python data types, mutability, references,
    and common interview questions.

Topics Covered:
    - isinstance()
    - bool as int
    - List references
    - Tuple immutability
    - Sets
    - Dictionary vs Set
    - Mutable vs Immutable objects
    - Equality vs Data Types

===========================================================
"""


# =========================================================
# Challenge 1
# =========================================================
"""
Without using type():

Write a program that determines whether a variable
contains a string or a number.
"""

print("=" * 50)
print("Challenge 1")
print("=" * 50)

a = "Hello"

if isinstance(a, str):
    print("This is a string.")
elif isinstance(a, (int, float, complex)):
    print("This is a number.")

"""
Explanation:
- isinstance() checks whether an object belongs to a
  particular data type.
- Unlike type(), it also supports inheritance.
"""


# =========================================================
# Challenge 2
# =========================================================
"""
Predict the output before running:

x = True
y = False

print(x + y)
print(x * 10)
"""

print("\n" + "=" * 50)
print("Challenge 2")
print("=" * 50)

x = True
y = False

print(x + y)
print(x * 10)

"""
Expected Output

1
10

Explanation

True behaves like the integer 1.
False behaves like the integer 0.

Since bool is a subclass of int, Python allows
arithmetic operations on Boolean values.

True + False
= 1 + 0
= 1

True * 10
= 1 * 10
= 10
"""


# =========================================================
# Challenge 3
# =========================================================
"""
a = [1, 2, 3]
b = a

b.append(4)

print(a)
print(b)

Why are both outputs the same?
"""

print("\n" + "=" * 50)
print("Challenge 3")
print("=" * 50)

a = [1, 2, 3]
b = a

b.append(4)

print(a)
print(b)

"""
Explanation

Output

[1, 2, 3, 4]
[1, 2, 3, 4]

Reason

b = a does NOT create a new list.

Instead, both variables reference the SAME list object.

When b.append(4) is executed,
the original list is modified.

Underlying Concept:
Reference (Object Aliasing)
"""


# =========================================================
# Challenge 4
# =========================================================
"""
Why does this code fail?

x = (1, 2, 3)
x[0] = 100
"""

print("\n" + "=" * 50)
print("Challenge 4")
print("=" * 50)

x = (1, 2, 3)

try:
    x[0] = 100
except TypeError as error:
    print(error)

"""
Explanation

Tuples are immutable.

Once created, their elements cannot be modified.

Attempting to assign a new value raises:

TypeError:
'tuple' object does not support item assignment

Underlying Concept:
Immutability
"""


# =========================================================
# Challenge 5
# =========================================================
"""
Why are duplicate values removed?
"""

print("\n" + "=" * 50)
print("Challenge 5")
print("=" * 50)

numbers = {1, 2, 2, 3, 4, 4, 5}

print(numbers)

"""
Explanation

Sets only store UNIQUE values.

Duplicate values are automatically ignored.

Output

{1, 2, 3, 4, 5}

(Note: Order may vary because sets are unordered.)

Underlying Concept:
Unique Elements
"""


# =========================================================
# Challenge 6
# =========================================================
"""
Explain the difference between:

[]
()
{}
set()
"""

print("\n" + "=" * 50)
print("Challenge 6")
print("=" * 50)

print("[]     -> List")
print("()     -> Tuple")
print("{}     -> Dictionary")
print("set()  -> Set")

"""
Summary

[]      -> Ordered, Mutable, Allows Duplicates

()      -> Ordered, Immutable,
            Allows Duplicates

{}      -> Dictionary (Key : Value)

set()   -> Unordered,
            Mutable,
            Unique Values Only

Interview Tip

{} creates an EMPTY DICTIONARY.

To create an empty set, use:

set()
"""


# =========================================================
# Challenge 7
# =========================================================
"""
Explain why strings are immutable
but lists are mutable.
"""

print("\n" + "=" * 50)
print("Challenge 7")
print("=" * 50)

"""
Explanation

Strings are immutable.

Their characters cannot be modified
after creation.

Example

name = "Python"

name[0] = "J"

Raises:
TypeError

----------------------------------------

Lists are mutable.

Their elements can be modified.

Example

numbers = [1, 2, 3]

numbers[0] = 100

Output

[100, 2, 3]

Why?

Strings:
- Safe
- Memory efficient
- Hashable
- Can be dictionary keys

Lists:
- Designed for frequently changing data

Underlying Concept

Mutable vs Immutable Objects
"""


# =========================================================
# Challenge 8
# =========================================================
"""
Predict every output.
"""

print("\n" + "=" * 50)
print("Challenge 8")
print("=" * 50)

a = 10
b = 10.0
c = "10"

print(type(a))
print(type(b))
print(type(c))

print(a == b)
print(a == c)

"""
Expected Output

<class 'int'>
<class 'float'>
<class 'str'>
True
False

Explanation

10 and 10.0 have different data types
but equal numeric values.

Therefore

10 == 10.0

returns

True

However,

10 == "10"

returns

False

because one value is an integer
and the other is a string.
"""


# =========================================================
# End of File
# =========================================================

print("\n" + "=" * 50)
print("All Python Data Type Challenges Completed Successfully!")
print("=" * 50)

