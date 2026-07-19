# Python Functions - Complete Notes

## What is a Function?

A function is a reusable block of code that performs a specific task.

Instead of writing the same code again and again, we write it once inside a function and call it whenever needed.

### Advantages

- Code reusability
- Better readability
- Easier debugging
- Easier maintenance
- Reduces code duplication

---

# Creating Functions

Use the `def` keyword.

## Syntax

```python
def function_name():
    # code
```

### Example

```python
def greet():
    print("Hello World")

greet()
```

Output

```
Hello World
```

---

# Calling Functions

A function runs only when it is called.

```python
def welcome():
    print("Welcome!")

welcome()
welcome()
```

Output

```
Welcome!
Welcome!
```

---

# Parameters

Parameters are variables written inside the function definition.

```python
def greet(name):
    print("Hello", name)
```

Here,

```
name
```

is a parameter.

---

# Arguments

Arguments are actual values passed to a function.

```python
def greet(name):
    print("Hello", name)

greet("Ali")
```

Here,

```
Ali
```

is the argument.

---

# Positional Arguments

Arguments are assigned according to their position.

```python
def student(name, age):
    print(name, age)

student("Ali", 21)
```

Output

```
Ali 21
```

Incorrect

```python
student(21, "Ali")
```

Output

```
21 Ali
```

because positions changed.

---

# Keyword Arguments

Arguments are passed using parameter names.

```python
def student(name, age):
    print(name, age)

student(age=21, name="Ali")
```

Output

```
Ali 21
```

Order does not matter.

---

# Default Arguments

A parameter can have a default value.

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Sara")
```

Output

```
Hello Guest
Hello Sara
```

---

# Variable-Length Arguments

Sometimes we don't know how many arguments will be passed.

Python provides

- *args
- **kwargs

---

# *args

Collects multiple positional arguments into a tuple.

```python
def add(*numbers):
    print(numbers)

add(1,2,3,4)
```

Output

```
(1, 2, 3, 4)
```

Example

```python
def add(*numbers):

    total = 0

    for num in numbers:
        total += num

    print(total)

add(10,20,30)
```

Output

```
60
```

---

# **kwargs

Collects keyword arguments into a dictionary.

```python
def student(**info):

    print(info)

student(name="Ali", age=21)
```

Output

```
{'name':'Ali','age':21}
```

Example

```python
def student(**info):

    for key,value in info.items():
        print(key,":",value)

student(name="Ali", age=21, department="CS")
```

Output

```
name : Ali
age : 21
department : CS
```

---

# Return Values

A function can return a value using

```
return
```

```python
def add(a,b):

    return a+b

result = add(10,20)

print(result)
```

Output

```
30
```

Without return

```python
def add(a,b):

    print(a+b)

result = add(10,20)

print(result)
```

Output

```
30
None
```

because the function returned nothing.

---

# Difference Between print() and return

print()

- Displays output
- Does not send value back

return

- Sends value back to the caller
- Can be stored in a variable

---

# Scope

Scope means where a variable can be accessed.

Two types

- Local Scope
- Global Scope

---

## Local Variable

Created inside a function.

```python
def demo():

    x = 10

    print(x)

demo()
```

Outside

```python
print(x)
```

Error

```
NameError
```

---

## Global Variable

Created outside a function.

```python
x = 100

def demo():

    print(x)

demo()
```

Output

```
100
```

---

## global Keyword

Used to modify a global variable.

```python
count = 0

def increase():

    global count

    count += 1

increase()

print(count)
```

Output

```
1
```

---

# Recursion

A function calling itself.

```python
def countdown(n):

    if n == 0:
        return

    print(n)

    countdown(n-1)

countdown(5)
```

Output

```
5
4
3
2
1
```

---

## Recursive Factorial

```python
def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n-1)

print(factorial(5))
```

Output

```
120
```

---

# Lambda Functions

Anonymous (nameless) functions.

Syntax

```python
lambda arguments : expression
```

Example

```python
square = lambda x: x*x

print(square(5))
```

Output

```
25
```

Multiple parameters

```python
add = lambda a,b: a+b

print(add(10,20))
```

Output

```
30
```

Used with sorting

```python
students = [
    ("Ali",80),
    ("Sara",95),
    ("Ahmed",70)
]

students.sort(key=lambda x:x[1])

print(students)
```

Output

```
[('Ahmed',70),('Ali',80),('Sara',95)]
```

---

# Type Hints

Used to specify expected data types.

```python
def add(a:int, b:int) -> int:

    return a+b
```

Example

```python
def greet(name:str) -> str:

    return "Hello " + name
```

Type hints improve readability but are not enforced by Python.

---

# Docstrings

Documentation inside a function.

```python
def add(a,b):

    """
    Returns the sum of two numbers.
    """

    return a+b
```

Access docstring

```python
print(add.__doc__)
```

Output

```
Returns the sum of two numbers.
```

---

# Best Practices

✅ Use meaningful function names

```python
calculate_area()
```

instead of

```python
abc()
```

---

✅ One function should perform one task.

Good

```python
calculate_total()
```

Bad

```python
calculate_total_send_email_save_database()
```

---

✅ Keep functions short.

---

✅ Use return instead of print whenever possible.

---

✅ Add docstrings for reusable functions.

---

✅ Avoid global variables.

---

✅ Follow snake_case naming.

Good

```python
calculate_average()
```

Bad

```python
CalculateAverage()
```

---

# Summary

- Functions make code reusable.
- Use `def` to create functions.
- Parameters receive values.
- Arguments send values.
- Positional arguments depend on order.
- Keyword arguments use parameter names.
- Default arguments provide default values.
- `*args` stores extra positional arguments.
- `**kwargs` stores extra keyword arguments.
- `return` sends values back.
- Scope controls variable visibility.
- Recursion means a function calls itself.
- Lambda creates small anonymous functions.
- Type hints improve readability.
- Docstrings document functions.
- Follow best practices for clean code.