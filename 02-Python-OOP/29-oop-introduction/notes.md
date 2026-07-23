# 29 - Object-Oriented Programming (OOP) Introduction

# What is OOP?

Object-Oriented Programming (OOP) is a programming paradigm that organizes code into **objects** instead of just functions.

An object contains:

- Data (Attributes)
- Behavior (Methods)

Think of an object as something from the real world.

Example:

Car

Attributes

- Brand
- Color
- Speed

Methods

- Start()
- Stop()
- Accelerate()

---

# Why was OOP introduced?

As software became larger, procedural programming became difficult to maintain.

Problems included:

- Duplicate code
- Difficult debugging
- Poor scalability
- Hard maintenance
- Weak code organization

OOP solves these problems by organizing related data and behavior together.

---

# Procedural Programming vs Object-Oriented Programming

## Procedural Programming

Program is divided into functions.

Example

```
calculate_salary()
print_salary()
save_salary()
```

Functions are separate.

Data is passed from one function to another.

---

## Object-Oriented Programming

Program is divided into objects.

Example

Employee Object

Data

- Name
- Salary

Methods

- calculate_salary()
- print_salary()
- save()

Everything related to Employee stays inside the Employee class.

---

# What is a Class?

A class is a blueprint or template.

Example

Blueprint of a House.

You cannot live inside a blueprint.

It is only a design.

---

# What is an Object?

An object is a real instance created from a class.

Blueprint → House

Class → Object

Student Class

↓

Ali Object

↓

Ahmed Object

↓

Sara Object

---

# Attributes

Attributes are variables that belong to an object.

Example

Student

- Name
- Roll Number
- Age

---

# Methods

Methods are functions inside a class.

Example

Student

- study()
- sleep()
- attend_class()

---

# Real-Life Examples

## Mobile Phone

Attributes

- Brand
- RAM
- Storage
- Battery

Methods

- Call()
- Charge()
- Restart()

---

## Bank Account

Attributes

- Account Number
- Balance
- Holder Name

Methods

- Deposit()
- Withdraw()
- Check Balance()

---

## Car

Attributes

- Brand
- Color
- Speed

Methods

- Start()
- Stop()
- Brake()

---

# Advantages of OOP

- Better code organization
- Easy maintenance
- Reusable code
- Modular design
- Easier debugging
- Scalable applications
- Real-world modeling

---

# Disadvantages

- More memory usage
- Slightly slower than procedural programming
- More planning required
- Can be unnecessary for very small scripts

---

# Where is OOP Used?

- Web Development
- AI Applications
- Desktop Applications
- Mobile Apps
- Games
- Robotics
- Banking Systems
- Hospital Management
- ERP Systems

---

# Four Pillars of OOP

1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction

These will be covered in later modules.

---

# Procedural vs OOP Example

Without OOP

```
calculate_salary()
print_salary()
save_salary()
```

With OOP

```
Employee

Employee.calculate_salary()
Employee.print_salary()
Employee.save()
```

Notice how everything related to Employee stays together.

---

# Interview Notes

Class

Blueprint

Object

Instance of a class

Attribute

Variable inside an object

Method

Function inside an object

---

# Key Takeaways

✔ OOP organizes code into objects.

✔ Objects contain data and behavior.

✔ Classes are blueprints.

✔ Objects are created from classes.

✔ OOP improves maintainability and scalability.

✔ OOP models real-world entities.