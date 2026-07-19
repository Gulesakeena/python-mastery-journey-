"""
19 - Python Arrays
Examples
"""

from array import array

# ----------------------------------
# Creating Arrays
# ----------------------------------

numbers = array('i', [10, 20, 30, 40, 50])

print("Original:", numbers)


# ----------------------------------
# Accessing Elements
# ----------------------------------

print(numbers[0])
print(numbers[2])
print(numbers[-1])


# ----------------------------------
# Updating Elements
# ----------------------------------

numbers[1] = 100

print(numbers)


# ----------------------------------
# Traversing
# ----------------------------------

print("\nTraversal:")

for num in numbers:
    print(num)


# ----------------------------------
# Append
# ----------------------------------

numbers.append(60)

print(numbers)


# ----------------------------------
# Insert
# ----------------------------------

numbers.insert(2, 25)

print(numbers)


# ----------------------------------
# Remove
# ----------------------------------

numbers.remove(40)

print(numbers)


# ----------------------------------
# Pop
# ----------------------------------

numbers.pop()

print(numbers)


# ----------------------------------
# Reverse
# ----------------------------------

numbers.reverse()

print(numbers)


# ----------------------------------
# Count
# ----------------------------------

print(numbers.count(10))


# ----------------------------------
# Index
# ----------------------------------

print(numbers.index(25))


# ----------------------------------
# Extend
# ----------------------------------

extra = array('i', [70, 80, 90])

numbers.extend(extra)

print(numbers)


# ----------------------------------
# Length
# ----------------------------------

print(len(numbers))


# ----------------------------------
# Iterate with Index
# ----------------------------------

for i in range(len(numbers)):
    print(i, numbers[i])


# ----------------------------------
# Simple Search
# ----------------------------------

target = 80

if target in numbers:
    print(f"{target} Found")
else:
    print("Not Found")


# ----------------------------------
# Simple Sum
# ----------------------------------

print(sum(numbers))


# ----------------------------------
# Maximum & Minimum
# ----------------------------------

print(max(numbers))
print(min(numbers))


# ----------------------------------
# Array vs List
# ----------------------------------

python_list = [1, "Ali", 3.5]

print(python_list)

# The following would raise an error because arrays require a single data type:
#
# array('i', [1, "Ali", 3])