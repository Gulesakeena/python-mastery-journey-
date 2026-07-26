# 37 - Pass by Object Reference (Call by Sharing)

# Learning Objectives

After completing this topic, you should be able to:

- Understand how Python passes arguments to functions.
- Understand what Pass by Object Reference means.
- Differentiate between mutable and immutable objects.
- Understand object references in memory.
- Predict function outputs involving lists, objects, and integers.
- Avoid common interview mistakes.

---

# What is Pass by Object Reference?

Python **does not use Pass by Value or Pass by Reference**.

Python uses:

> **Pass by Object Reference** (also called **Call by Sharing**)

When a function is called:

- Python does **not** copy the object.
- Python does **not** pass the actual variable.
- Python passes a **reference to the same object**.

---

# How It Works

Example

```python
a = 10

def fun(x):
    print(x)

fun(a)
```

Memory

```
Object 10

 ▲      ▲
 │      │
 a      x
```

Both variables point to the same object.

---

# Immutable Objects

Examples

- int
- float
- str
- tuple
- bool

Immutable means:

> Their value cannot be changed after creation.

Example

```python
def fun(x):
    x = 20

a = 10

fun(a)

print(a)
```

Output

```python
10
```

Why?

Because

```python
x = 20
```

creates a **new object**.

Memory

Before

```
Object 10

 ▲      ▲
 │      │
 a      x
```

After

```
Object 10        Object 20

 ▲                   ▲
 │                   │
 a                   x
```

The original object remains unchanged.

---

# Mutable Objects

Examples

- list
- dict
- set
- custom class objects

Mutable means:

> Their contents can be modified without creating a new object.

Example

```python
def fun(lst):
    lst.append(100)

numbers = [1,2,3]

fun(numbers)

print(numbers)
```

Output

```python
[1,2,3,100]
```

Memory

Before

```
List

[1,2,3]

 ▲          ▲
 │          │
numbers    lst
```

After append()

```
Same List

[1,2,3,100]

 ▲             ▲
 │             │
numbers       lst
```

The same object is modified.

---

# Reassigning a Mutable Object

Example

```python
def fun(lst):
    lst = [1,2,3,100]

numbers = [1,2,3]

fun(numbers)

print(numbers)
```

Output

```python
[1,2,3]
```

Why?

Because

```python
lst = [1,2,3,100]
```

creates a new list.

Memory

```
Old List              New List

[1,2,3]           [1,2,3,100]

   ▲                   ▲
   │                   │
numbers               lst
```

The original list is unchanged.

---

# append() vs =

Example 1

```python
lst.append(100)
```

Result

✔ Modifies the original object.

---

Example 2

```python
lst = lst + [100]
```

Result

✔ Creates a new list.

---

Comparison

| Code | Original Object Modified? | New Object Created? |
|-------|---------------------------|---------------------|
| append() | ✅ Yes | ❌ No |
| extend() | ✅ Yes | ❌ No |
| pop() | ✅ Yes | ❌ No |
| remove() | ✅ Yes | ❌ No |
| sort() | ✅ Yes | ❌ No |
| reverse() | ✅ Yes | ❌ No |
| lst = lst + [...] | ❌ No | ✅ Yes |
| lst = [...] | ❌ No | ✅ Yes |

---

# Slicing Creates a Copy

Example

```python
numbers = [1,2,3]

copy = numbers[:]
```

Memory

```
List1              List2

[1,2,3]        [1,2,3]

 ▲                 ▲
 │                 │
numbers          copy
```

These are different objects.

Example

```python
def change(lst):
    lst.append(5)

numbers = [1,2,3]

change(numbers[:])

print(numbers)
```

Output

```python
[1,2,3]
```

Because a copy was passed.

---

# Class Objects

Example

```python
class Student:

    def __init__(self, name):
        self.name = name
```

Create object

```python
s = Student("Ali")
```

Memory

```
Student Object

name = Ali

     ▲
     │
     s
```

---

# Modifying an Object

```python
def change(student):
    student.name = "Sara"

s = Student("Ali")

change(s)

print(s.name)
```

Output

```python
Sara
```

Both variables point to the same object.

Memory

```
Student Object

name = Sara

 ▲          ▲
 │          │
 s      student
```

---

# Reassigning an Object

```python
def change(student):
    student = Student("Sara")

s = Student("Ali")

change(s)

print(s.name)
```

Output

```python
Ali
```

Memory

```
Object1             Object2

Ali                 Sara

 ▲                    ▲
 │                    │
 s                student
```

The parameter now points to a new object.

The original object remains unchanged.

---

# Mutable vs Immutable

| Mutable | Immutable |
|----------|-----------|
| list | int |
| dict | float |
| set | str |
| custom objects | tuple |
| bytearray | bool |

---

# Interview Trick

Question

```python
def fun(lst):
    lst.append(100)

a = [1,2,3]

fun(a)

print(a)
```

Answer

```python
[1,2,3,100]
```

---

Question

```python
def fun(lst):
    lst = [1,2,3,100]

a = [1,2,3]

fun(a)

print(a)
```

Answer

```python
[1,2,3]
```

---

Question

```python
def fun(x):
    x = 20

a = 10

fun(a)

print(a)
```

Answer

```python
10
```

---

# Common Mistakes

❌ Thinking Python uses Pass by Value.

❌ Thinking Python uses Pass by Reference.

❌ Confusing object modification with variable reassignment.

❌ Forgetting that slicing (`[:]`) creates a copy.

---

# Best Practices

✔ Use immutable objects when values should not change.

✔ Be careful when passing mutable objects to functions.

✔ Pass a copy (`[:]` or `.copy()`) if you do not want the original object modified.

✔ Understand whether your code modifies the object or creates a new one.

---

# Key Takeaways

- Python uses **Pass by Object Reference (Call by Sharing)**.
- Function parameters point to the same object as the caller.
- Mutable objects can be modified inside functions.
- Immutable objects cannot be modified; reassignment creates a new object.
- `append()`, `pop()`, `remove()`, and `sort()` modify the original object.
- Assignment (`=`) creates a new reference.
- Slicing (`[:]`) creates a new copy of a list.
- Reassigning a parameter does **not** affect the caller.
- Modifying the shared object **does** affect the caller.