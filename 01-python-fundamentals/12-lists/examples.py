# Creating Lists
fruits = ["banana","apple","orange"]
numbers = [1,2,3,4]
mixed = ['banana',1,3.3,False]

print(fruits)
print(numbers)
print(mixed)

# Indexing
print(numbers[1])
print(fruits[3])
print(mixed[-3])

# Slicing
print(numbers[1:3])
print(fruits[-1:-2])

# Updating
numbers[1] = 0
print(numbers)

# Adding Items
numbers.append(4)
numbers.insert(1,1)
print(numbers)

# Removing Items
mixed.remove(False)
numbers.pop(2)
del fruits[0]
print(fruits)

# Looping
for i in fruits:
    print(i)

# Sorting
scores = [70,90,100,25,80]
print(scores.sort())
print(scores.sort(reverse=True))

# Copy
num = numbers.copy()

# Join 
combine = fruits + ["kivi","grappes"]
print(combine)

# Nested List
mixed = [
    [1,2],
    [3,4]
]
print(mixed[1][0])

# List Comprehension
squares = (x*x for x in range(10))
print(squares)






