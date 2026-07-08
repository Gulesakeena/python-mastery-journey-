'''Challenge 1

Predict the output:

print(10 + 5 * 2)

Explain using operator precedence.'''

# 20 because according to operator precedence rules * solves before then +


'''Challenge 2

Output?

x = 5

x += 3 * 2

print(x)'''

# x = x + 3 * 2 --> x = 5 + 3 * 2 -- > 5 + 6 -- > 11
output : 11

'''Challenge 3

Predict:

print(True + 5 * False)'''

# 1 + 5 * 0
# output : 1

'''Challenge 4

Explain:

a = [1,2]
b = [1,2]

print(a == b)
print(a is b)'''
True
False

'''Challenge 5

Without using %

Check whether a number is even.'''
number = int(input("Enter a number: "))

if (number // 2) * 2 == number:
    print("Even")
else:
    print("Odd")


'''Challenge 6

Without using comparison operators

Determine if two numbers are equal.'''

num_1 = 20
num_2 = 20

if not (num_1 - num_2):
    print("Equal")
else:
    print("Not Equal")

'''Challenge 7 (Hard)

Predict:

print(not True and False or True)

Explain step by step.'''

# Explaination : 
'''
not True = False
now False and Fasle or True 
False and Fasle --> False
False or True  -- > True
final output is True
'''

'''Challenge 8 (Hard)

Output?

print(4 << 2)
print(32 >> 3)

Explain.'''

# print(4 << 2) -- >Left shift by 2 means multiply by 2² (4) -- > 4 * 4 = 16
# print(32 >> 3) -- > Right shift by 3 means divide by 2³ (8).  32 / 8 = 4

'''Challenge 9 (Very Hard)

Write your own power function.

power(2,5)

Output

32

Restrictions:

Don't use:

**
pow()'''

def power(base, exponent):
    result = 1

    for i in range(exponent):
        result = result * base

    return result


base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

print(power(base, exponent))

'''Challenge 10 (Interview Favorite)

Without using:

+

Add two numbers.

(Hint: Use bitwise operators.)'''

def add(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum =", add(num1, num2))