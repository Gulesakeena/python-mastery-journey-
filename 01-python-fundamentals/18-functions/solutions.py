# Beginner
'Greeting Function'
def greet():
    return "Hello World"

print(greet())

'Sum Function'
def add(a,b):
    return a+b
print(add(2,3))

'Maximum of Two Numbers'
def maximum(a,b):
    return max(a,b)
print((maximum(2,3)))

'Even/Odd Function'
def even(a):
    if a%2 == 0:
        return "Even"
    else:
        return 'odd'
print(even(4))

'Leap Year Function'
def leap_year(year):

    if year % 400 == 0:
        return "Leap Year"

    elif year % 100 == 0:
        return "Not Leap Year"

    elif year % 4 == 0:
        return "Leap Year"

    else:
        return "Not Leap Year"

print(leap_year(2024))

'Factorial Function'
def fact(n):

    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

print(fact(5))

'Prime Function'
def prime(n):
    count = 0
    for i in range(1,n+1):
        if n% i == 0:
            count = count+1
    if count>2:
        return "Not a prime number"
    else:
        return "prime number"
print(prime(7))
    

'Reverse String'
def reverse_string(text):
    if text == "":
        return ""
    else:
        return reverse_string(text[1:]) + text[0]

print(reverse_string("python"))

'Count Vowels'
def count_vowels(txt):
    count = 0

    for ch in txt:
        if ch in "aeiou":
            count += 1

    return count

print(count_vowels("python"))
        
'Celsius to Fahrenheit'
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(celsius_to_fahrenheit(25))

# Intermediate
'Fibonacci Function'
def fibonacci(number):
    a = 0
    b = 1

    for i in range(number):
        print(a)
        c = a + b
        a = b
        b = c

fibonacci(5)

'Palindrome Checker'
def palindrome(number):
    original_number = number
    reverse = 0
    while number>0:
        digit = number%10
        reverse = reverse*10+ digit
        number = number // 10
    if original_number == reverse:
        return "palindrom"
    else:
        return "Not palindrom"
print(palindrome(121))

'Password Validator'
def password_validator(text):
    password=input("Enter password : ")
    if text == password:
        return"correct password"
    else:
        return "wrong password"
print(password_validator("Gul"))

'Count Words'
def counter(text):
    words = text.split()
    return len(words)
print(counter("My name is Gul"))
    
'Shopping Bill Calculator'
def shopping_bill(price, quantity):
    total = price * quantity

    if total >= 5000:
        discount = total * 0.10
    else:
        discount = 0

    return total - discount

print(shopping_bill(1000, 6))

'Student Grade Function'
def Grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >=80:
        return "B+"
    elif marks >=70:
        return "B"
    elif marks >=60:
        return "C"
    elif marks >=50:
        return "D"
    else:
        return "F"
print(Grade(85))

'BMI Calculator'
def bmi(weight, height):

    bmi_value = weight / (height ** 2)

    if bmi_value < 18.5:
        return "Underweight"

    elif bmi_value < 25:
        return "Normal Weight"

    elif bmi_value < 30:
        return "Overweight"

    else:
        return "Obese"


print(bmi(55, 1.60))
    

'ATM Balance Function'
def atm(balance, amount):

    if amount <= balance:
        balance = balance - amount
        return balance
    else:
        return "Insufficient Balance"

print(atm(10000, 3000))

'Employee Salary Calculator'
def salary_calculator(basic_salary):

    if basic_salary >= 50000:
        bonus = basic_salary * 0.20

    elif basic_salary >= 30000:
        bonus = basic_salary * 0.10

    else:
        bonus = basic_salary * 0.05

    return basic_salary + bonus

print(salary_calculator(40000))

'Calculator Using Functions'
def calculator(a,b,o):
    if o=='+':
        return a+b
    elif o=='-':
        return a-b
    elif o=='*':
        return a*b
    elif o=='/':
        return a/b
    else:
        return "enter correct operator"
print(calculator(2,4,"+"))