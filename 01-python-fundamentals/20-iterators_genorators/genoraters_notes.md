# Generators in Python

## Objective

Learn Python Generators from beginner to advanced level. By the end of these notes, you will understand how generators work, why they are useful, how they differ from iterators, and where they are used in real-world applications.

---

# 1. Introduction to Generators

A **Generator** is a special type of function that produces values **one at a time** instead of creating and returning all values at once.

Unlike a normal function, a generator uses the **`yield`** keyword instead of **`return`**.

Because generators produce values only when needed, they are **memory efficient** and ideal for working with large datasets.

Example:

```python
def numbers():
    yield 1
    yield 2
    yield 3

g = numbers()

print(next(g))
print(next(g))
print(next(g))
```

Output

```
1
2
3
```

---

# 2. Why Generators?

Suppose you need one million numbers.

### Using a List

```python
numbers = [x for x in range(1000000)]
```

The list stores **every value in memory**.

```
Memory

1
2
3
4
5
...
1000000
```

This uses a large amount of RAM.

---

### Using a Generator

```python
numbers = (x for x in range(1000000))
```

The generator stores only its current state.

```
Memory

Current Value
```

The next value is produced only when requested.

Benefits:

- Uses less memory
- Faster for large data
- Suitable for infinite sequences

---

# 3. Generator vs Iterator

Both generators and iterators produce values one at a time.

| Generator | Iterator |
|------------|----------|
| Created using `yield` | Created using classes |
| Automatically implements `__iter__()` and `__next__()` | Must implement `__iter__()` and `__next__()` manually |
| Very little code | More code |
| Easy to write | More complex |
| Memory efficient | Memory efficient |

---

## Custom Iterator Example

```python
class Counter:

    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):

        if self.current > self.end:
            raise StopIteration

        value = self.current
        self.current += 1

        return value


for num in Counter(1, 5):
    print(num)
```

---

## Generator Version

```python
def counter(start, end):

    while start <= end:
        yield start
        start += 1

for num in counter(1, 5):
    print(num)
```

Notice that the generator does the same work with much less code.

---

# 4. Generator vs Function

Normal Function

```python
def greet():
    return "Hello"

print(greet())
```

Output

```
Hello
```

The function ends immediately after returning.

---

Generator Function

```python
def greet():
    yield "Hello"

g = greet()

print(next(g))
```

Output

```
Hello
```

The generator pauses instead of ending.

---

# 5. yield vs return (Python Tutor Style Explanation)

## return

```python
def demo():

    print("Start")

    return 10

    print("End")

print(demo())
```

Execution

```
Start

↓

return 10

↓

Function Ends
```

Output

```
Start
10
```

---

## yield

```python
def demo():

    print("Start")

    yield 10

    print("Middle")

    yield 20

    print("End")

g = demo()

print(next(g))
print(next(g))
print(next(g))
```

Execution

```
Call next()

↓

Start

↓

yield 10

↓

Pause

↓

Call next()

↓

Middle

↓

yield 20

↓

Pause

↓

Call next()

↓

End

↓

StopIteration
```

Output

```
Start
10
Middle
20
End
```

**Important**

- `return` ends the function.
- `yield` pauses the function and remembers its state.

---

# 6. Generator Function

Any function containing **`yield`** becomes a generator.

```python
def fruits():

    yield "Apple"
    yield "Banana"
    yield "Orange"

g = fruits()

for fruit in g:
    print(fruit)
```

Output

```
Apple
Banana
Orange
```

---

# 7. Generator Object

Calling a generator function does **not** execute it immediately.

```python
def demo():
    yield 1

g = demo()

print(g)
print(type(g))
```

Output

```
<generator object ...>

<class 'generator'>
```

The generator object starts execution only when `next()` or a loop requests a value.

---

# 8. next() Function

`next()` retrieves one value at a time.

```python
def numbers():

    yield 100
    yield 200
    yield 300

g = numbers()

print(next(g))
print(next(g))
print(next(g))
```

Output

```
100
200
300
```

If no values remain,

```python
next(g)
```

raises

```
StopIteration
```

---

# 9. for Loop with Generators

Instead of calling `next()` repeatedly, use a loop.

```python
def counter():

    for i in range(1, 6):
        yield i

for value in counter():
    print(value)
```

Output

```
1
2
3
4
5
```

The `for` loop automatically handles `StopIteration`.

---

# 10. Building Custom range() using Generator

Instead of creating an iterator class, we can use a generator.

```python
def my_range(start, end):

    while start < end:
        yield start
        start += 1

for num in my_range(5, 11):
    print(num)
```

Output

```
5
6
7
8
9
10
```

---

# 11. Generator Expressions

List Comprehension

```python
numbers = [x*x for x in range(5)]

print(numbers)
```

Output

```
[0, 1, 4, 9, 16]
```

---

Generator Expression

```python
numbers = (x*x for x in range(5))

for value in numbers:
    print(value)
```

Output

```
0
1
4
9
16
```

Difference

| List Comprehension | Generator Expression |
|--------------------|----------------------|
| Uses [] | Uses () |
| Stores all values | Generates values one by one |
| More memory | Less memory |

---

# 12. Memory Comparison (sys.getsizeof)

```python
import sys

numbers = [x for x in range(100000)]

generator = (x for x in range(100000))

print(sys.getsizeof(numbers))
print(sys.getsizeof(generator))
```

The list occupies much more memory because every value is stored.

The generator occupies very little memory because values are produced only when needed.

---

# 13. Infinite Generators

Generators can create infinite sequences.

```python
def even_numbers():

    number = 0

    while True:

        yield number

        number += 2

g = even_numbers()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
```

Output

```
0
2
4
6
8
```

Since the loop never ends, values can be generated forever.

---

# 14. Chaining Generators

One generator can use another.

```python
def numbers():
    for i in range(1,6)
    yield i
def squares(values):
    for value in values:
        yield value*value

for i in range(numbers()):
    print(i)
```

Output

```
1
4
9
16
25
```

This technique is useful when processing data step by step.

---

# 15. Practical Example (Reading Images/Files)

Suppose a folder contains thousands of images.

Instead of loading every image into memory, we can load one image at a time.

Example:

```python
import os

def file_reader(folder):

    for file in os.listdir(folder):

        yield file

for filename in file_reader("Images"):
    print(filename)
```

Advantages

- Less memory usage
- Faster startup
- Suitable for large datasets

The same idea is commonly used with images, videos, text files, databases, and APIs.

---

# 16. Advantages

- Memory efficient
- Faster for large datasets
- Produces values only when needed
- Easy to implement
- Automatically behaves like an iterator
- Suitable for streaming data
- Supports infinite sequences

---

# 17. Disadvantages

- Can be used only once
- Cannot access values using indexing
- Cannot move backward
- Values disappear after being consumed

---

# 18. When to Use Generators

Use generators when:

- Reading large files
- Processing millions of records
- Loading images one by one
- Streaming videos
- Reading API responses
- Infinite sequences
- Data pipelines
- Machine Learning datasets

Avoid generators when:

- You need random indexing.
- You need to reuse the data multiple times.

---

# 19. Interview Questions

### Q1. What is a Generator?

A generator is a function that produces values one at a time using `yield`.

---

### Q2. Why use Generators?

To save memory and process large datasets efficiently.

---

### Q3. Difference between yield and return?

- `return` ends the function.
- `yield` pauses the function.

---

### Q4. Difference between Generator and Iterator?

Generators are easier to create and automatically implement iterator methods.

---

### Q5. What does next() do?

Returns the next generated value.

---

### Q6. What happens after all values are consumed?

Python raises `StopIteration`.

---

### Q7. Can generators be infinite?

Yes.

---

### Q8. What is a Generator Expression?

A generator created using parentheses.

Example

```python
(x*x for x in range(5))
```

---

# 20. Practice Questions

### Beginner

- Create a generator that prints numbers 1–10.
- Generate even numbers.
- Generate odd numbers.
- Generate squares.
- Generate cubes.
- Generate alphabets A–Z.
- Create a countdown generator.
- Create a multiplication table generator.

### Intermediate

- Build your own range().
- Generate Fibonacci numbers.
- Generate prime numbers.
- Generate factorial values.
- Generate vowels from a string.
- Read a file line by line.

### Advanced

- Infinite even numbers generator.
- Infinite Fibonacci generator.
- Chain two generators.
- Build a CSV file reader using generators.
- Process images one by one using generators.

---

# 21. Cheatsheet

Create Generator

```python
def demo():
    yield 1
```

---

Generator Object

```python
g = demo()
```

---

Next Value

```python
next(g)
```

---

Loop

```python
for value in g:
    print(value)
```

---

Generator Expression

```python
(x for x in range(10))
```

---

Infinite Generator

```python
while True:
    yield value
```

---

# 22. Summary

- A Generator is a special function.
- Uses `yield` instead of `return`.
- Produces values one at a time.
- Automatically behaves like an iterator.
- Saves memory.
- Can represent infinite sequences.
- Supports lazy evaluation.
- Useful for large datasets and streaming data.
- `next()` retrieves one value at a time.
- `for` loops automatically consume generators until `StopIteration`.
- Generator expressions provide a compact way to create generators.
```