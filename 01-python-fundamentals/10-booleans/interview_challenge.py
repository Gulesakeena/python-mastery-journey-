'''Challenge 1

Predict the output:

print(bool("False"))
print(bool("0"))
print(bool(" "))
Explain why.'''

"False" #is a non-empty string, so bool("False") is True.
"0" #is also a non-empty string, so bool("0") is True.
" " #(a space) is still a non-empty string, so bool(" ") is True.



'''Challenge 2

Predict:

print(True + True)
print(True * 10)
print(False + 100)

Why?'''

# 2
# 10
# 100

'''Challenge 3

Output?

x = []

if x:
    print("True")
else:
    print("False")'''

False

'''Challenge 4

Without using ==

Check if two numbers are equal.

(Hint: Use arithmetic or logical reasoning.)'''

number_1 = 10
number_2 = 10

if number_1 - number_2 == 0:
    print("both are equal")
else :
    print("both are not equal")

'''Challenge 5

Write your own function:

is_even(number)

Return True or False.'''

def is_even(number):
     return number % 2 == 0
number = int(input("Enter a number"))
is_even(number)


'''Challenge 6

Write:

is_prime(number)

Return only Boolean values.'''

def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


number = int(input("Enter a number: "))

print(is_prime(number))


number = int(input("Enter a number: "))
is_prime(number)

'''Challenge 7 (Hard)

Explain:

print(True and False or True)

Why?
'''
# True because first and implement and True and false = False because in or if there is only one true in and output is False then False or True = True because in or if there is only one true output is true

'''Challenge 8 (Hard)

Predict:

x = None

print(bool(x))

Explain.'''

# Fasle becaue in python None in boolean is consider as 0 that is false

'''Challenge 9 (Very Hard)

Implement:

is_valid_password(password)

Return only True or False.

Conditions:

At least 8 characters
One uppercase
One lowercase
One digit
One special character '''

def is_valid_password(password):
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special_character = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_special_character = True

    if (
        len(password) >= 8
        and has_uppercase
        and has_lowercase
        and has_digit
        and has_special_character
    ):
        print(True)
    else:
        print(False)


password = input("Enter a strong password: ")
is_valid_password(password)

'''Challenge 10 (Interview Favorite)

Without using:

if

Return whether a number is positive.

(Hint: Use Boolean expressions directly.)'''

def is_positive(number):
    return number > 0

number = int(input(("Enter a number : ")))
print(is_positive(number))




