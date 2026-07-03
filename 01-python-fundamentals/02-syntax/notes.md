# Python Syntax Notes

## What is Syntax?

Syntax is the set of rules that defines how Python code must be written.

If the syntax is incorrect, Python raises a SyntaxError.

---

## Indentation

Python uses indentation (spaces) to define blocks of code.

Usually, 4 spaces are used for one indentation level.

Example:

if True:
    print("Hello")

---

## Why Indentation?

Unlike many programming languages, Python does not use curly braces `{}`.

Instead, indentation tells Python which statements belong together.

---

## Case Sensitivity

Python is case-sensitive.

Example:

name = "Ali"

print(name)

print(Name)

The second line will produce a NameError because `Name` and `name` are different identifiers.