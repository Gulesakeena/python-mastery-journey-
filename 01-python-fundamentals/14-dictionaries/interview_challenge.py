'''Challenge 1

Predict:

student = {"name": "Ali"}

print(student.get("age"))'''
# None 

'''Challenge 2

Why does this fail?

student = {
    ["name"]: "Ali"
}'''
# because key is a list and key can't be a list bacause list is mutable

'''Challenge 3

Difference between:

student["age"]

and

student.get("age")'''
# student["age"] gives  error because key age is not present in dictionary 
# student.get("age") gives None because if key is not resent .get dont gines error it returns None

'''Challenge 4

Without using:

len()

Find dictionary size.'''

marks = {
    "Ali": 85,
    "Sara": 95,
    "Ahmed": 78,
    "Zain": 95
}
length = 0
for key in marks:
    length = length + 1
print(length)


'''Challenge 5

Find duplicate values.'''

marks = {
    "Ali": 85,
    "Sara": 95,
    "Ahmed": 78,
    "Zain": 95
}
duplicates = []

for value in marks.values():
    if list(marks.values()).count(value) > 1 and value not in duplicates:
        duplicates.append(value)

print(duplicates)

'''Challenge 6

Count frequency of every character.

Input

banana

Output

{
'b':1,
'a':3,
'n':2
}'''
freq = {}
character = "banana"
for char in character:
    freq[char] = freq.get(char,0) + 1
print(freq)

'''Challenge 7

Merge dictionaries without using update().'''

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

for key, value in student_1.items():
    merge[key] = value

for key, value in student_2.items():
    merge[key] = value

print(merge)

'''Challenge 8

Reverse keys and values.'''
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

'''Challenge 9

Find the key with the highest value.'''
marks = {
    "Ali": 85,
    "Sara": 92,
    "Ahmed": 78,
    "Zain": 95
}
highest_key = ""
highest_value = 0

for key, value in marks.items():
    if value > highest_value:
        highest_value = value
        highest_key = key

print(highest_key)

'''Challenge 10

Explain why dictionary lookups are approximately O(1).'''

#Python dictionaries use a hash table. When a key is searched, Python computes its hash and directly accesses the corresponding memory location instead of scanning all elements. Therefore dictionary lookups are approximately O(1) on average.