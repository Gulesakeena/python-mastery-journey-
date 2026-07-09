# Creating tuples
fruits = ("apple","kivi","mango","orange")
print(fruits)

# Single element tuple
a = (10,)
print(type(a))

b = (10)
print(type(b))

# Accessing elements
print(fruits[0])
print(fruits[-1])

# Slicing
print(fruits[1:3])

# Unpacking
person = ("ali",21,"pakistan")
name , age , country = person 
print(name)
print(age)
print(country)

# Nested tuple
matrix = (
    (1,2),
    (3,4)
)
print(matrix[1][0])

# count()
number = (1,2,3,4,4,5,5)
print(number.count(5))

# index()
print(number.index(2))

# Concatenation
a = (1,2)
b = (2,3)
print(a+b)

# Repetition
print(('AI',)*3)




