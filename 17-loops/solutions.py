# exercises.py

# Beginner
'Print numbers 1–100'
for i in range(1,101):
    print(i)

'Print even numbers'
for i in range(2,11,2):
    print(i)

'Print odd numbers'
for i in range(10):
    if i%2 != 0 :
        print(i)

'Sum of first N numbers'
n = 10
count = 0
for i in range(1,n+1):
    count = count + i
print(count)

'Multiplication table'
for i in range(1,11):
    print('2 * ',i,' = ', 2 * i )

'Reverse counting'
for i in reversed(range(10)):
    print(i)
    
'Count vowels'
count = 0
text = "python"

for ch in text:
    if ch.lower() in "aeiou":
        count += 1

print(count)

'Count digits'
number = int(input("Enter a number: "))

count = 0

while number > 0:
    count += 1
    number //= 10

print("Total digits =", count)

'Print every character'
text = 'python'
for char in text :
    print(char)

'Find maximum'
number = [10,20,360,40,50]
largest = number[0]
for i in number:
    if largest < i:
        largest = i
print(largest)

# Intermediate

'Factorial'
number = int(input("Enter a number: "))

factorial = 1
for i in range(1,number+1):
    factorial*=i
print(factorial)

'Fibonacci'
n = int(input("Enter the number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

'Prime numbers'
count = 0

for i in range(1, number + 1):
    if number % i == 0:
        count += 1

if count == 2:
    print("Prime")
else:
    print("Not Prime")

'Armstrong number'
number = int(input("Enter a number : " ))
original_number = number
sum = 0
while number>0:
    digit = number % 10 
    sum = sum + digit**3
    number = number // 10 
if original_number == sum:
    print('Armstrong number')
else:
    print('Not Armstrong number')

'Palindrome'
number = int(input("Enter a number : " ))
original_number = number
reverse = 0
while number>0:
    digit = number % 10 
    reverse = reverse* 10 +digit 
    number = number // 10
if original_number == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

'Perfect number'
number = int(input("Enter a number : " ))
sum = 0
for i in range(1, number):
    if number % i == 0:
        sum = sum + i
if number == sum:
    print("Perfect number")
else:
    print("Not Perfect number")

'Pattern printing'
'''
*
**
***
****
*****
'''
row = 5
for i in range(1 , row+1):
    for j in range(i):
            print("*",end="")
    print()

'''
1
12
123
1234
'''
rows = 4

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

'Nested multiplication table'
for i in range(1,3):
    print(f"\nTable of {i}")
    for j in range(1,11):
        print(f"{i} X {j} = {i*j}")

'Guessing game'
import random
secret = random.randint(1,10)
while True:
    guess = int(input("Enter your guess from 1-10 : "))
    if guess < secret :
        print("Too Low")
    elif guess > secret :
        print("Too High")
    else:
        print('Correct')
        break

'Menu-driven calculator'
while True:

    print("""
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
""")

    choice = int(input("Enter choice: "))

    if choice == 5:
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print("Result =", num1 + num2)

    elif choice == 2:
        print("Result =", num1 - num2)

    elif choice == 3:
        print("Result =", num1 * num2)

    elif choice == 4:
        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Cannot divide by zero")

    else:
        print("Invalid Choice")

