'''Challenge 1

Predict:

nums = [10,20,30]

print(nums[-2])'''
# output --> 20

'''Challenge 2

Predict:

nums = [1,2,3]

nums.append([4,5])

print(nums)

Explain.'''

#output --> [1,2,3,4,5] because in python when we appnd a list means add item at the end

'''Challenge 3

Difference?

append()

extend()

Give examples.
'''
numbers = [1,2,3,4,5]
numbers.append([6,7])
print(numbers)
# this append( ) add the 6 7 at the end

numbers.extend([8,9])
print(numbers)
# extend list by appending element from the iterable.

'''Challenge 4

Difference?

remove()

pop()

del'''
# remove --> remove items at the end
# pop --> remove item by dfault at the end other wise remove before the specfic position
# del --> remove first occerance of that item that we want to remove

'''Challenge 5

Without using:

max()

Find the maximum element.'''

numbers = [1,2,3,4,5]
largest = 0
for i in numbers:
    if i > largest:
        largest = i 
print(largest ,"is the maximum element")

'''Challenge 6

Without using:

min()

Find the minimum.'''
numbers = [1, 2, 3, 4, 5]

smallest = numbers[0]

for i in numbers:
    if i < smallest:
        smallest = i

print(smallest, "is the minimum element")

'''Challenge 7

Without using:

sort()

Sort a list.

(Hint: Bubble Sort)'''

numbers = [5, 3, 8, 1, 2]

n = len(numbers)

for i in range(n):
    for j in range(n-1-i):
        if numbers[j] > numbers[j+1]:
            numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
print("sorted list : ", numbers)

'''Challenge 8

Rotate list left by one position.

Example

[1,2,3,4]

↓

[2,3,4,1]'''
# way 1
number = [1,2,3,4]
shift_num=number.pop(0)
number.append(shift_num)
print(number)

# way 2
number = [1,2,3,4]
left_move_list = number[1:]
left_move_list.append(number[0])
print(left_move_list)

# way 3
numbers = [1, 2, 3, 4]

first = numbers[0]

for i in range(len(numbers) - 1):
    numbers[i] = numbers[i + 1]

numbers[-1] = first

print(numbers)

'''
Challenge 9

Rotate list right by one position.

[1,2,3,4]

↓

[4,1,2,3]'''

number = [1, 2, 3, 4]
shifted_num = number.pop()
number.insert(0,shifted_num)
print(number)


'''Challenge 10

Move all zeros to the end.

Input

[0,1,0,3,12]

Output

[1,3,12,0,0]'''
numbers = [0, 1, 0, 3, 12]

result = []

# Add all non-zero numbers
for num in numbers:
    if num != 0:
        result.append(num)

# Count zeros
zero_count = numbers.count(0)

# Add zeros at the end
for i in range(zero_count):
    result.append(0)

print(result)

    

