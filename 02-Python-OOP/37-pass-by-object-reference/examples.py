"""
37 - Pass by Object Reference
"""

# --------------------------
# Example 1 - Immutable
# --------------------------

x = 10
y = x

print(id(x))
print(id(y))

y += 5

print(x)
print(y)

# --------------------------
# Example 2 - Mutable
# --------------------------

numbers = [1, 2, 3]
copy = numbers

copy.append(4)

print(numbers)
print(copy)

# --------------------------
# Example 3 - Function with List
# --------------------------

def add_item(lst):
    lst.append(100)

values = [10, 20]

add_item(values)

print(values)

# --------------------------
# Example 4 - Function with Integer
# --------------------------

def increase(num):
    num += 1

value = 50

increase(value)

print(value)

# --------------------------
# Example 5 - Reassignment
# --------------------------

def clear_list(lst):
    lst = []

items = [1, 2, 3]

clear_list(items)

print(items)

# --------------------------
# Example 6 - id()
# --------------------------

nums = [5, 10]

print(id(nums))

nums.append(15)

print(id(nums))