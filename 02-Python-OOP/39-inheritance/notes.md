# 39 - Inheritance

# What is Inheritance?

Inheritance allows one class to acquire the attributes and methods of another class.

Instead of writing the same code multiple times, a new class can reuse an existing class.

Inheritance represents an

> **IS-A Relationship**

Example

```
Car IS-A Vehicle

Dog IS-An Animal

Student IS-A Person

Manager IS-An Employee
```

---

# Why Use Inheritance?

Without inheritance

```
Employee

name
salary

Manager

name
salary
department

Developer

name
salary
language
```

The code for `name` and `salary` is repeated.

With inheritance

```
Employee
   ▲
   │
 ┌─┴─────────┐
 │           │
Manager   Developer
```

The common code is written only once.

---

# Parent Class

A parent class is the class whose properties and methods are inherited.

```python
class Animal:

    def speak(self):
        print("Animal speaks")
```

---

# Child Class

A child class inherits from the parent class.

```python
class Dog(Animal):
    pass
```

Now `Dog` automatically gets `speak()`.

---

# Example

```python
class Animal:

    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    pass


dog = Dog()

dog.speak()
```

Output

```
Animal speaks
```

---

# Adding New Methods

A child class can have its own methods.

```python
class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):

    def bark(self):
        print("Barking")
```

Dog now has

- eat()
- bark()

---

# Constructor Inheritance

```python
class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):
    pass
```

The child automatically inherits the parent's constructor.

---

# super()

`super()` is used to call methods from the parent class.

Example

```python
class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, roll):

        super().__init__(name)

        self.roll = roll
```

Benefits

- Avoids duplicate code.
- Calls the parent constructor.
- Keeps the inheritance chain clean.

---

# Method Overriding

A child class can replace a parent's method with its own implementation.

```python
class Animal:

    def speak(self):
        print("Animal speaks")


class Dog(Animal):

    def speak(self):
        print("Dog barks")
```

Output

```
Dog barks
```

---

# Types of Inheritance

## 1. Single Inheritance

```
Animal
   │
 Dog
```

---

## 2. Multiple Inheritance

```
Teacher   Researcher
      \   /
    Professor
```

---

## 3. Multilevel Inheritance

```
Animal
   │
 Mammal
   │
  Dog
```

---

## 4. Hierarchical Inheritance

```
        Animal
      /    |    \
    Dog   Cat   Cow
```

---

## 5. Hybrid Inheritance

A combination of multiple inheritance types.

---

# Method Resolution Order (MRO)

When multiple inheritance exists, Python follows the Method Resolution Order (MRO) to determine which method to execute.

Use

```python
ClassName.mro()
```

Example

```python
print(Dog.mro())
```

---

# Advantages

✔ Code Reusability

✔ Less Duplication

✔ Easy Maintenance

✔ Better Organization

✔ Extensibility

---

# Disadvantages

- Deep inheritance trees become difficult to understand.
- Excessive inheritance increases complexity.
- Sometimes composition is a better choice.

---

# Aggregation vs Inheritance

Aggregation

```
Car HAS-A Engine
```

Inheritance

```
Car IS-A Vehicle
```

---

# Interview Notes

Relationship

```
Inheritance

IS-A
```

Aggregation

```
HAS-A
```

Composition

```
PART-OF
```

---

# Best Practices

✔ Keep inheritance hierarchies simple.

✔ Use inheritance only when an IS-A relationship exists.

✔ Prefer composition if inheritance doesn't fit naturally.

✔ Use `super()` to initialize parent classes.

---

# Key Takeaways

- Inheritance promotes code reuse.
- Child classes inherit parent attributes and methods.
- `super()` calls the parent implementation.
- Method overriding customizes behavior.
- Python supports five inheritance types.
- MRO determines method lookup order.