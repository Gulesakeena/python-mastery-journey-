#interview_challenge.py
'''Challenge 1

Predict:

numbers = {1,2,2,3,3,4}

print(numbers)

Explain why duplicates disappear.'''

# A set does not allow duplicate elements. When duplicate values are added,
# Python automatically removes them and keeps only unique values.
'''Challenge 2

Difference between:

remove()

discard()'''
# remove() raises a KeyError if the element is not present.
# discard() does not raise an error if the element is not present.

'''Challenge 3

Predict:

A = {1,2,3}

A.add((4,5))

print(A)

Why is tuple allowed?'''
# Tuples are immutable and hashable (if all their elements are hashable).
# Since 4 and 5 are integers (which are hashable),
# the tuple (4, 5) is hashable and can be added to a set.

'''Challenge 4

Why does this fail?

A = {1,2}

A.add([3,4])'''
# Lists are mutable and therefore unhashable.
# A set can store only hashable objects.

'''Challenge 5

Difference:

{}

and

set()'''

# {} is an empty dictionary and set( ) is an empty set.


'''Challenge 6

Without using set(), remove duplicates from a list manually.'''

marks = [10,20,30,40,50,60,10,20,30]

unique_marks = []

for i in marks:
    if i not in unique_marks:
        unique_marks.append(i)

print(unique_marks)

'''Challenge 7

Find common elements between two lists using sets.'''
list_1 = [1,2,3,4,5]
list_2 = [4,5,6,7,8]

set1 = set(list_1)
set2 = set(list_2)
commom = set1.intersection(set2)
print(commom)

'''Challenge 8

Check if two strings are anagrams using sets and explain why using only sets is insufficient.'''
word1 = "listen"
word2 = "silent"

from collections import Counter

if Counter(word1) == Counter(word2):
    print("Anagram")
else:
    print("Not Anagram")
#Because a set stores only unique elements and removes duplicates. Anagrams require not only the same unique characters but also the same frequency of each character. Therefore, comparing sets can produce false positives (for example, "aab" and "ab"), so a dictionary or collections.Counter should be used instead.

'''Challenge 9

Count unique words in a paragraph.'''
paragraph = "i love python because python is very intersting and easy"
words = paragraph.split()
paragraph_set = set(words)
print(len(paragraph_set))

'''Challenge 10

Explain why set lookup is approximately O(1).'''
#Set lookup is approximately O(1) because Python sets use a hash table. Each item is stored using its hash value, allowing Python to find it directly without checking every element. In rare cases (hash collisions), lookup can be slower, but on average it remains O(1).
