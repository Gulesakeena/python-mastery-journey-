# 42 - Dataclasses

## Theory

1. What is a dataclass?
2. Why do we use dataclasses?
3. What methods are automatically generated?
4. What is `field()`?
5. Why do we use `default_factory`?
6. What is `__post_init__()`?
7. What is a frozen dataclass?
8. Can dataclasses inherit from each other?
9. Difference between a dataclass and a normal class.
10. When should you use a dataclass instead of a regular class?

---

## Coding Questions

1. Create a Student dataclass.
2. Use default values.
3. Use field(default_factory=list).
4. Calculate total price using __post_init__().
5. Create a frozen dataclass.

---

## Interview Challenge

Build an Employee Management System.

Requirements

- Create an Employee dataclass.
- Store employee ID, name, department, and salary.
- Use `field(default_factory=list)` to store completed projects.
- Use `__post_init__()` to calculate yearly salary.
- Display employee details.
- Create multiple Employee objects and compare them using `==`.