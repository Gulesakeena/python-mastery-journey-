# Beginner (10)
'Create a list of five cities.'
cities = ['lahore','gujrat',"wazirabad","islamabad",'sialot']

'Print the first element.'
print(cities[0])

'Print the last element.'
print(cities[-1])

'Replace the third item.'
cities[2]='Gujranwala'
print(cities)

'Add a new item.'
cities.append("sargodah")
print(cities)

'Insert an item at index 2.'
cities.insert(2,"karachi")
print(cities)

'Remove one item.'
cities.remove("sargodah")
print(cities)

'Print list length.'
print(len(cities))

'Sort ascending.'
cities.sort()
print(cities)

'Sort descending.'
cities.sort(reverse=True)
print(cities)

# Intermediate (10)
'Find largest element.'
numbers = [1,3,5,7,9,9,10]
print(max(numbers))

'Find smallest element.'
print(min(numbers))

'Calculate sum.'
print(sum(numbers))

'Calculate average.'
print(sum(numbers)/len(numbers))

'Remove duplicates.'
numbers = list(set(numbers))
print(numbers)

'Reverse a list.'
numbers.reverse()
print(numbers)

'Count occurrences.'
print(numbers.count(9))

'Merge two lists.'
merge = cities + numbers
print(merge)

'Check if an element exists.'
if 10 in numbers:
    print('Found')

'Copy a list without affecting the original.'
copy = numbers.copy()
print(copy)