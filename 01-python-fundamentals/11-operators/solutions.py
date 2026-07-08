# Beginner
'Add two numbers.'
a = 10
b = 20
print(a + b)

'Subtract two numbers.'
a = 10
b = 20
print(a - b)

'Multiply two numbers.'
a = 10
b = 20
print(a * b)

'Divide two numbers.'
a = 10
b = 20
print(a / b)

'Find the remainder.'
a = 10
b = 20
print(a % b)

'Find power.'
a = 10
b = 20
print(a ** b)

'Use +=.'
a = 10
b = 20
a += b
print(a)

'Use *=.'
a = 10
b = 20
a *= b
print(a)

'Compare two numbers.'
a = 10
b = 20
print(a >= b)

'Check whether a character exists in a string.'
text = "python"

char = input("Enter a character: ")

if char in text:
    print("Character exists in the string.")
else:
    print("Character does not exist in the string.")

# Intermediate
'Check whether a number is between 50 and 100.'
number = int(input("Enter a number : "))
if number >= 50 and number <= 100 :
    print("number is between 50 and 100")
else :
    print("number is not between 50 and 100")

'Check whether a student passed (marks ≥ 40).'
marks = int(input("Enter your marks : "))
if marks >= 40 :
    print("Pass")
else:
    print("Fail")

'Swap two variables using operators.'
a = 10
b = 20
print("Before swapping")
print("a : ",a)
print("b : ",b)

a , b = b , a

print("After swapping")
print("a : ",a)
print("b : ",b)


'Find the largest of three numbers.'
a = 10 
b = 20 
c = 30
if a > b and a > c :
    print(a , " is the largest number") 
elif b > a and b > c :
    print(b , " is the largest number")
else : 
    print(c , " is the largest number")

'Check if a number is divisible by both 3 and 5.'
number = int(input("Enter a number"))
if number % 3 == 0 and number % 5 == 0 :
    print("number is divisible by both 3 and 5")
else : 
    print("number is not divisible by both 3 and 5")

'Check if a character is a vowel.'
char = input("Enter a character : ")
if char.lower() in ('aeiou'):
    print("character is a vowel")
else :
    print("character is not a vowel")

'Demonstrate is vs ==.'
# Demonstrate is :
if [1,3] is [1,3] :
    print(True)
else :
    print(False)

# Demonstrate ==
if [1,3] == [1,3] :
    print(True)
else :
    print(False)


'Demonstrate in vs not in.'
text = "python"
print('Z' in text)
print('Z' not in text)

'Use bitwise left shift.'
print( 10 << 2)

'Use bitwise right shift.'
print(10 >> 2)