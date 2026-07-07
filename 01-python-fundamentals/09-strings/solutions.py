'Print your full name.'
name = 'Gul e sakeena'
print(name)

"Print the first character."
print(name[0])

"Print the last character."
print(name[-1])

"Print the first five characters."
print(name[0:5])

"Print the last four characters."
print(name[-1:-4])

"Convert a string to uppercase."
print(name.upper())

"Convert a string to lowercase."
print(name.lower())

"Remove spaces using strip()."
print(name.strip())

"Replace one word with another."
print(name.replace("G","g"))

"Split a sentence into words"
sentance = " python , java , c++ "
sentance.split(",")

"Reverse a string using slicing."
text = "python"
print(text[::-1])

"Count vowels."
text="python"
count = 0
for char in text:
    if char in ('a','e','i','o','u'):
        count=count+1
if count > 0:
    print(count)
else:
    print("There is no vowel")

#A More Pythonic Version
text = "python"
count = 0

for char in text:
    if char in "aeiou":
        count += 1

if count:
    print("Number of vowels:", count)
else:
    print("There are no vowels.")

'Count consonants.'
text = "python"
count = 0

for char in text:
    if char not in "aeiou":
        count += 1

if count:
    print("Number of constants:", count)
else:
    print("There are no constant.")

'Check if a string starts with a specific letter.'
text = "pyhon"
print(text.startswith("p"))

'Check if it ends with ".com".'
text = "pyhon"
print(text.endswith("com"))

'Count occurrences of a character.'
text = "pyhon"
print(text.count("o"))

'Find the first occurrence of a word.'
text = "pyhon"
print(text.find("o"))

'Convert every word to title case.'
sentance = "i love python"
print(sentance.title())

"Remove all spaces."
sentance = "  i love python  "
print(sentance.strip())

'Print every character on a new line.'
print("\ni \nlove \npython")