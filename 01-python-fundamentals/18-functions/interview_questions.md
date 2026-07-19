# interview_challenge.py

'''
Challenge 1

Create a function that returns the largest of three numbers.
'''

def largest(a, b, c):
    return max(a, b, c)

print(largest(10, 25, 15))


'''
Challenge 2

Create a function that checks whether a number is prime.
'''

def is_prime(n):

    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

print(is_prime(17))


'''
Challenge 3

Create a function that returns the factorial of a number.
'''

def factorial(n):

    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

print(factorial(5))


'''
Challenge 4

Create a recursive function to calculate power.
'''

def power(base, exponent):

    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)

print(power(2, 5))


'''
Challenge 5

Reverse a string using recursion.
'''

def reverse_string(text):

    if text == "":
        return ""

    return reverse_string(text[1:]) + text[0]

print(reverse_string("python"))


'''
Challenge 6

Count vowels in a string.
'''

def count_vowels(text):

    count = 0

    for ch in text.lower():
        if ch in "aeiou":
            count += 1

    return count

print(count_vowels("Education"))


'''
Challenge 7

Find the sum of all numbers using *args.
'''

def total_sum(*numbers):

    total = 0

    for num in numbers:
        total += num

    return total

print(total_sum(10, 20, 30, 40))


'''
Challenge 8

Display all student information using **kwargs.
'''

def student_info(**info):

    for key, value in info.items():
        print(f"{key}: {value}")

student_info(
    name="Ali",
    age=21,
    department="SE",
    cgpa=3.8
)


'''
Challenge 9

Write a lambda function to find the square of a number.
'''

square = lambda x: x ** 2

print(square(7))


'''
Challenge 10

Sort a list of tuples by the second element using lambda.
'''

students = [
    ("Ali", 85),
    ("Sara", 95),
    ("Ahmed", 78),
    ("Zain", 88)
]

students.sort(key=lambda student: student[1])

print(students)