'''Challenge 1

Predict:

a = (5)

print(type(a))'''
# output -- > int

'''Challenge 2

Predict:

a = (5,)

print(type(a))

Explain why.'''

#output --> A trailing comma tells Python to create a tuple. Without the comma, Python treats it as an integer.

'''Challenge 3

Output?

numbers = (1,2,3)

numbers += (4,)

print(numbers)'''

#output --> (1,2,3,4)

'''Challenge 4

Why does this fail?

numbers = (1,2,3)

numbers[0]=100'''

# ANS ---------------------------
'''List	Tuple
Mutable	Immutable
Uses []	Uses ()
Many methods	Only count() and index()
Slightly slower	Slightly faster'''
# ------------------------------

'''Challenge 5

Difference:

list

tuple'''
# list is mutable and tuple is immutable means when we craete list we can change its element through indxing but we can't change the element of tuple when it created

'''Challenge 6

Tuple unpacking

student = ("Ali",20,"CS")

Unpack into three variables.'''

student = ("Ali",20,"CS")
name , age , department = student
print(name)
print(age)
print(department)

'''Challenge 7

Extended unpacking

numbers = (1,2,3,4,5)

a,*b,c = numbers

Predict output.'''

numbers = (1,2,3,4,5)
a , *b , c = numbers
print(a)
print(b)
print(c)

'''Challenge 8

Without using:

count()

Count occurrences manually.'''

number = (1,2,3,4,5,5)
target = 5
count = 0
for num in number :
    if num == target :
        count = count + 1
print(target, "appears", count, "times")

        

'''Challenge 9

Without using:

index()

Find index manually.'''

number = (1,2,3,4,5,5)

target = 5
index = 0

for num in number:
    if num == target:
        print("Index:", index)
        break
    index += 1

'''Challenge 10

Why are tuples hashable but lists are not?

Explain.'''

# Tuples are hashable because they are immutable. Their contents cannot change after creation, so Python can safely compute a fixed hash value. Lists are mutable, so their contents can change, making them unhashable.

'''Interview Theory Questions
Prepare answers for:

What is a tuple?
Why are tuples immutable?
Difference between tuple and list.
Why are tuples faster?
When should tuples be used?
What is tuple packing?
What is tuple unpacking?
What is extended unpacking?
What is namedtuple?
Why can tuples be dictionary keys while lists cannot?'''