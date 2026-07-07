'''Challenge 1

Predict the output:

text = "Python"

print(text[-3])
print(text[1:5])
print(text[::-1])'''

# output -- > h , ytho , nohtyP

'''Challenge 2

Explain why this gives an error:

name = "Python"

name[0] = "J"   '''

# Explaination :This gives an error because strings are immutable in Python.Once a string is created, its characters cannot be changed using indexing. 


'''Challenge 3

Without using len():

Find the length of a string.'''
text = "python"
length = 0
for char in text:
    length = length + 1
print("Length f string is :",length)


'''Challenge 4

Without using slicing:

Reverse a string.'''
text = 'python'
reverse = ""
for char in text:
    reverse = char + reverse 
print(reverse)



'''Challenge 5
Check whether a string is a palindrome.

Example:

madam

Output:

Palindrome'''
text = str(input("Enter a string :"))
original_text = text
reverse = ""
for char in text:
    reverse = char + reverse 
if reverse == original_text:
    print("the string is Palindrome")
else:
    print("the string is not Palindrome")


'''Challenge 6

Find the frequency of every character.

Example:

banana

Output:

b : 1
a : 3
n : 2'''
text = "banana"
printed = ""
for char in text:
    if char not in printed:
        print(char , ' : ' , text.count(char))
    printed = printed + char 



'''Challenge 7

Remove duplicate characters.

Example:

banana

Output:

ban'''
text = "banana"
printed = ""
for char in text:
    if char not in printed:
        printed = printed + char
print(printed)

'''Challenge 8

Compress a string.

Example:

aaabbccccdd

Output:

a3b2c4d2'''
text = 'aaabbccccdd'
printed = ""
count = ''
final_output=""
for i in text:
    if i not in printed: 
        printed = printed + i
        count = i + str(text.count(i))
        final_output=final_output+str(count)
print(final_output)

'''Challenge 9 (Hard)

Find the first non-repeating character.

Example:

aabbccddef

Output:

e'''
text = "aabbccddef"

for char in text:
    if text.count(char) == 1:
        print("First non-repeating character:", char)
        break




'''Challenge 10 (Very Hard)

Implement your own version of:

is_palindrome(text)

Restrictions:

Don't use slicing ([::-1])
Don't use reversed()'''
def is_palindrome(text):
    original_text = text
    reverse = ""

    for char in text:
        reverse = char + reverse

    if reverse == original_text:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")


text = input("Enter a string: ")
is_palindrome(text)
