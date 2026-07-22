# Python Iterators - Interview Questions

## Theory

1. What is an iterator?
2. What is an iterable?
3. Difference between iterable and iterator?
4. What does `iter()` do?
5. What does `next()` do?
6. What is `StopIteration`?
7. How does a `for` loop work internally?
8. Which methods are required to build a custom iterator?
9. Iterator vs Generator?
10. Why are iterators memory efficient?

---

## Coding Questions

1. Build a counter iterator.
2. Fibonacci iterator.
3. Prime iterator.
4. Alphabet iterator.
5. Countdown iterator.

---

## Predict the Output

```python
numbers = [1, 2]

it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))
```

**Question:** Which exception is raised?

---

```python
word = "AI"

it = iter(word)

for ch in it:
    print(ch)

print(next(it))
```

**Question:** Why does this fail?

---

## LeetCode Practice

Easy

- Flatten Nested List Iterator
- Peeking Iterator

Medium

- Zigzag Iterator
- Design Iterator for Combination

(Hard versions are optional at this stage.)