# ==========================
# Iterator, Iterable & Iteration
# ==========================

# --------------------------
# What is Iteration
# --------------------------
"""
Iteration is the process of accessing each item of a collection one by one.
Any time you use a loop to go through a sequence, you are performing iteration.
"""

num = [1, 2, 3, 4]

for i in num:
    print(i)


# --------------------------
# What is an Iterator
# --------------------------
"""
An Iterator is an object that allows you to traverse through a sequence
one element at a time without storing all elements in memory.

An Iterator has two methods:
1. __iter__()
2. __next__()
"""

import sys

# List stores all values in memory
L = [x for x in range(1, 100000)]
print("Size of List:", sys.getsizeof(L), "bytes")

# range is an iterable (not an iterator)
# It generates values one at a time and therefore uses much less memory.
x = range(1, 100000)
print("Size of range object:", sys.getsizeof(x), "bytes")


# --------------------------
# What is an Iterable
# --------------------------
"""
An Iterable is an object that can be iterated over.

It creates an Iterator when passed to iter().
"""

L = [1, 2, 3, 4]

print(type(L))          # List -> Iterable
print(type(iter(L)))    # List Iterator


# --------------------------
# Important Points
# --------------------------
"""
Every Iterator is also an Iterable.

Not every Iterable is an Iterator.

Examples of Iterables:
- list
- tuple
- set
- dictionary
- string
- range
"""


# --------------------------
# Easy Trick
# --------------------------
"""
Every Iterable has:
    __iter__()

Every Iterator has:
    __iter__()
    __next__()
"""


# --------------------------
# Checking whether an object is Iterable
# --------------------------

a = 2

# Method 1
# Try using a for loop.
# If TypeError occurs, it is not iterable.

# for i in a:
#     print(i)

# Method 2

print("__iter__" in dir(a))          # False
print("__iter__" in dir([1, 2, 3]))  # True


# --------------------------
# Understanding how a for loop works
# --------------------------

num = [1, 2, 3]

for i in num:
    print(i)


# Step 1 -> Create Iterator

iter_num = iter(num)

print(next(iter_num))
print(next(iter_num))
print(next(iter_num))

# print(next(iter_num))
# Raises StopIteration


"""
When there are no more elements left,
Python raises a StopIteration exception.
"""


# --------------------------
# Making our own for loop
# --------------------------

def own_loop(iterable):

    iterator = iter(iterable)

    while True:

        try:
            print(next(iterator))

        except StopIteration:
            break


a = [1, 2, 3]
b = range(1, 6)
c = (1, 2, 3)
d = {1, 2, 3}
e = {0: 10, 1: 20, 2: 30}

print("\nList")
own_loop(a)

print("\nRange")
own_loop(b)

print("\nTuple")
own_loop(c)

print("\nSet")
own_loop(d)

print("\nDictionary (Keys)")
own_loop(e)


# --------------------------
# A Confusing Point
# --------------------------

num = [1, 2, 3]

iterator1 = iter(num)
print(id(iterator1))

iterator2 = iter(iterator1)
print(id(iterator2))

"""
Both IDs are the same.

Reason:
An iterator returns itself when iter() is called.
"""


# --------------------------
# Creating our own range()
# --------------------------

class OwnRange:

    def __init__(self, start, end):

        self.start = start
        self.end = end

    def __iter__(self):

        return OwnRangeIterator(self)


class OwnRangeIterator:

    def __init__(self, iterable_obj):

        self.iterable = iterable_obj

    def __iter__(self):

        return self

    def __next__(self):

        if self.iterable.start >= self.iterable.end:
            raise StopIteration

        current = self.iterable.start

        self.iterable.start += 1

        return current


x = OwnRange(1, 11)

print("\nCustom Range")

for i in x:
    print(i)


# --------------------------
# Difference between Iterable and Iterator
# --------------------------

"""
Iterable
--------
Can be used in a for loop.

Examples:
list
tuple
set
dictionary
string
range

Iterator
--------
Produces one value at a time.

Has both:
__iter__()
__next__()

Examples:
list_iterator
tuple_iterator
range_iterator
"""


# --------------------------
# Summary
# --------------------------

"""
Iteration
---------
Process of visiting each element one by one.

Iterable
--------
Object that can be iterated over.

Iterator
--------
Object that returns one element at a time.

iter(obj)
---------
Creates an iterator.

next(iterator)
--------------
Returns the next element.

StopIteration
-------------
Raised when there are no more elements left.
"""