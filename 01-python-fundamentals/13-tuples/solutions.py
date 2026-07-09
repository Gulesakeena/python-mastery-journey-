'Create a tuple of five colors.'
color = ("red","green","orange","blue","black")

'Print first element.'
print(color[0])

'Print last element.'
print(color[-1])

'Print tuple length.'
print(len(color))

'Count occurrences of a value.'
print(color.count('red'))

'Find index of an element.'
print(color.index('red'))

'Slice first three elements.'
print(color[:3])

'Concatenate two tuples.'
numbers = (1,2,3,4,5)
print(numbers + color)

'Repeat a tuple three times.'
print(numbers*3)

'Create a single-element tuple.'
a = (10,)
print(a)

'Intermediate'

'Swap two variables using tuple unpacking.'
a = 1
b = 2

print("Before Swap")
print("a:", a)
print("b:", b)

a, b = b, a

print("After Swap")
print("a:", a)
print("b:", b)


'Find maximum value without using max().'
number = (1,4,6,5,3,2)
largest = number[0]
for i in number :
    if i > largest :
        largest = i
print(largest)

'Find minimum value without using min().'
number = (1,4,6,5,3,2)
smallest = number[0]
for i in number:
    if i < smallest:
        smallest = i
print(smallest)

'Convert list to tuple.'
number = [1,2,3,4,5]
num_tuple = tuple(number)
print(type(num_tuple))

'Convert tuple to list.'
number = (1,2,3,4,5)
number_list = list(number)
print(type(number_list))

'Check whether an element exists.'
number = (1,2,3,4,5)
if 3 in number :
    print("Found")
else :
    print("Not found")

'Iterate over tuple.'
number = (1,2,3,4,5)
for i in number :
    print(i)

'Reverse tuple using slicing.'
number = (1,2,3,4,5)
print(number[::-1])

'Find sum of tuple.'
number = (1,2,3,4,5)
print(sum(number))

'Find average.'
number = (1,2,3,4,5)
average = sum(number)/len(number)
print(average)