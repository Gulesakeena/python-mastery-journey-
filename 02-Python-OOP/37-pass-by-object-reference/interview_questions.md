# 37 - Pass by Object Reference

## Theory

1. Is Python pass-by-value or pass-by-reference?
2. What is Call by Sharing?
3. What does `id()` return?
4. Explain mutable vs immutable objects.
5. Why does modifying a list affect the original object?
6. Why doesn't modifying an integer affect the original value?
7. What happens when an object is reassigned inside a function?
8. Explain object references with an example.
9. What is the difference between changing an object and rebinding a variable?
10. Why do interviewers ask about this topic?

---

## Coding Questions

1. Write a function that modifies a list.
2. Write a function that attempts to modify an integer.
3. Demonstrate object identity using `id()`.
4. Show why reassignment inside a function doesn't affect the caller.
5. Explain the output of a mutable object example.

---

## Interview Challenge

Create an Inventory System.

Requirements:

- Store products in a list.
- Create a function that adds a product.
- Create another function that reassigns the product list.
- Print the list before and after each function.
- Use `id()` to explain why one operation changes the original object while the other does not.