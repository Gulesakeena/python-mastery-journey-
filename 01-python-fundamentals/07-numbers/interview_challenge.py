'''Challenge 1 (Easy)

Predict the output:

print(15 / 2)
print(15 // 2)
print(15 % 2)
Explain why each result is different.'''

# ANS
'7.5'
'7'
'1'
'7.5 is the devision result that is a decimal and 7 is the floor devision that is a whole number without a decimal point 1 is the remainder of 15%2'


''' Challenge 2 (Medium)

Without using max():

Find the largest among four numbers.'''

a = 21
b = 43
c = 54
d = 83

if (a > b) and (a > c) and (a > d ) :
    print( a , "is the largest number")
elif (b > a) and (b > c) and (b > d ) :
    print( b , "is the largest number")
elif (c > a) and (c > b) and (c > d ) :
    print( c , "is the largest number")
else:
    print( d , "is the largest number")

'''Challenge 3 (Medium)

Without using min():

Find the smallest among four numbers.'''

a = 21
b = 43
c = 54
d = 83

if (a < b) and (a < c) and (a < d ) :
    print( a , "is the smallest number")
elif (b < a) and (b < c) and (b < d ) :
    print( b , "is the smallest number")
elif (c < a) and (c < b) and (c < d ) :
    print( c , "is the smallest number")
else:
    print( d , "is the smallest number")

'''Challenge 4 (Medium)

Swap two numbers without using a third variable.'''

a = 4 
b = 6
 
print("before swaping")
print("a : ", a)
print("b : ", b)

a , b = b , a

print("after swaping")
print("a : ", a)
print("b : ", b)


'''Challenge 5 (Medium)

Find whether a number is:

Even
Odd
without using any library. '''

a = 12
if a % 2 == 0:
    print( a , "is an even number")
else : 
    print( a , "is an odd number")


'''Challenge 6 (Hard)

Reverse a number without converting it to a string.

Example:

Input:
123456

Output:
654321'''

'''
Challenge 6 (Hard)

Reverse a number without converting it to a string.

Example:

Input:
123456

Output:
654321
'''

# User Input
number = int(input("Enter a number: "))

# Store the original number
original_number = number

# Variable to store the reversed number
reverse = 0

# Reverse the number
while number > 0:
    # Get the last digit
    digit = number % 10

    # Add the digit to the reversed number
    reverse = reverse * 10 + digit

    # Remove the last digit
    number = number // 10

# Print the result
print("Original Number :", original_number)
print("Reversed Number :", reverse)

'''Challenge 7 (Hard)

Count the digits in a number without using len() or converting it to a string.

Example:

987654

Output:
6  '''

number = 987654
count = 0
while number > 0:
 number = number // 10 
 count = count + 1
print(count)



"""Challenge 8 (Hard)

Find the sum of all digits.

Example:

Input:
4567

Output:
22"""

number = 4567
total_sum = 0

while number > 0 :
    digit = number % 10 
    total_sum = total_sum + digit
    number = number // 10 
print(total_sum)


'''Challenge 9 (Very Hard)

Check whether a number is an Armstrong Number.

Example:

153 → True
370 → True
371 → True
407 → True
154 → False'''


# User Input
number = int(input("Enter a number: "))

# Store the original number
original_number = number

# Count total digits
digits = len(str(number))

# Variable to store the sum
total = 0

# Calculate Armstrong sum
while number > 0:
    digit = number % 10
    total = total + (digit ** digits)
    number = number // 10

# Check result
if total == original_number:
    print(original_number, "is an Armstrong Number.")
else:
    print(original_number, "is not an Armstrong Number.")




'''Challenge 10 (Interview Favorite)

Check whether a number is a Palindrome.

Example:

121 → True
123 → False
1221 → True'''

num= input("Enter a number : ")
number = int(num)
original_number =number
reverse = 0

while number > 0 :
    digit = number % 10 
    number = number // 10 
    reverse = ( reverse * 10 ) + digit

if reverse == original_number :
    print(original_number , " is a Palindrome")
else : 
    print(original_number , " is not a Palindrome")