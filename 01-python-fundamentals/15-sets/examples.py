# Creating Sets

marks={10,20,30,40,50,60}
print(type(marks))

# Empty Set
empty_set = set()

## Duplicate values
marks = {10,20,20,30,40,50}
print(marks)

# Add
marks.add(60)
print(marks)

# Update
marks.update(10,70)

# Remove
marks.remove(30)
marks.discard(20)

removed = marks.pop()
print("Removed:", removed)

# Membership
print(10 in marks)
print(100 not in marks)

# Loop
for i in marks:
    print(i)

# Set Operations
A = {1,2,3,4}
B = {3,4,5,6}

print("Union ",A | B)
print("Intersection ",A & B)
print("Difference ",A - B)
print("Symmetric Difference ",A ^ B)

# Copy
B = A.copy()

# Clear
B.clear()

# Frozen Set
fs = frozenset([1,2,3,4,5])
print(fs)
