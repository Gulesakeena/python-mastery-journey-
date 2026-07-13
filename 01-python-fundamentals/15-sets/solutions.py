# Beginner
'Create a set of five fruits.'
fruit = {'apple', 'banana','chary','mango','orange'}

'Print all elements.'
print(fruit)

'Add a new fruit.'
fruit.add()

'Remove a fruit.'
fruit.remove('banana')

'Check membership.'
print('banana'in fruit)

'Print set length.'
print(len(fruit))

'Create an empty set.'
mpty_set = set()

'Remove duplicates from a list using a set.'
marks = [10,20,30,40,50,60,10,20,30]
unque_marks = set(marks)

'Iterate through a set.'
for i in marks:
    print(i)

'Clear a set.'
fruit.clear()

#Intermediate
'Union of two sets.'
A = {1,2,3,4}
B = {3,4,5,6}

print("Union",A | B)
print("intersection",A&B)
print("difference",A-B)
print("Symmetric Difference",A^B)

'Check superset.'
print(A.issuperset(B))

'Check disjoint sets.'
print(A.isdisjoint(B))

'Convert tuple to set.'
marks=(10,20,3,40,50)
marks_set = set(marks)

'Convert string to set.'
text = "python"
print(set(text))

'Count unique characters in a string.'
print(len(set(text)))