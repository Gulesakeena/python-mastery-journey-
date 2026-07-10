# Beginner

'Create a dictionary of a student.'
student = {
    "name" : "ali",
    "age" : 21,
    "department" : "SE"
}

'Print one value.'
print(student['age'])

'Update one value.'
student['age'] = 23

'Add a new key.'
student['city'] = "Lahore"

'Delete a key.'
student.pop("name")

'Print all keys.'
print(student.keys())

'Print all values.'
print(student.values())

'Print all key-value pairs.'
print(student)

'Check whether a key exists.'
if 'name' in student :
    print("Key exist")
else :
    print("Not found")

'Print dictionary length.'
print(len(student))

# Intermediate

'Merge two dictionaries.'
student_1 = {
    "name" : "ali",
    "age" : 21,
    "department" : "SE"
}
student_2 = {
    "name" : "Gul",
    "age" : 22,
    "department" : "SE"
}
merge = {}

merge.update(student_1)
merge.update(student_2)
print(merge)

'Find highest value.'
marks = {
    "Ali": 85,
    "Sara": 92,
    "Ahmed": 78,
    "Zain": 95
}
highest = max(marks.values())
print(highest)

'Find lowest value.'
marks = {
    "Ali": 85,
    "Sara": 92,
    "Ahmed": 78,
    "Zain": 95
}
lowest = min(marks.values())
print(lowest)

'Count frequency of characters in a string.'
text = "python"
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)

'Count frequency of words in a sentence.'
sentence = "I love python I love AI"
words = sentence.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print(freq)

'Invert keys and values.'
marks = {
    "Ali": 85,
    "Sara": 92,
    "Ahmed": 78,
    "Zain": 95
}
new_dict = {}
for keys,values in marks.items() :
    new_dict[values] = keys

print(new_dict)


'Sort dictionary by keys.'
marks = {
    "Ali": 85,
    "Sara": 92,
    "Ahmed": 78,
    "Zain": 95
}
new_dict = {}
for key in sorted(marks):
    new_dict[key] = marks[key]
print(new_dict)

'Sort dictionary by values.'

marks = {
    "Ali": 85,
    "Sara": 92,
    "Ahmed": 78,
    "Zain": 95
}
new_dict = {}
for keys,values in sorted(marks.items(), key=lambda item: item[1]):
    new_dict[keys] = values
print(new_dict)

'Remove duplicate values.'
marks = {
    "Ali": 85,
    "Sara": 95,
    "Ahmed": 78,
    "Zain": 95
}

new_dict = {}

for key, value in marks.items():
    if value not in new_dict.values():
        new_dict[key] = value

print(new_dict)

'Create dictionary from two lists.'
number_1 =[1,2,3,4,5]
number_2 =[6,7,8,9,10]
new_dict = {}
for i in range(len(number_1)):
    new_dict[number_1[i]]=number_2[i]

print(new_dict)