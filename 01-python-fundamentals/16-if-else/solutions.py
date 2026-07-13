# Beginner
'Check positive or negative.'
number = 0
if number > 0 :
    print("positive")
else:
    print("negative")

'Check even or odd.'
number = 80
if number % 2 == 0:
    print("positive")
else:
    print("negative")

'Largest of two numbers.'
a = 2
b = 3
if a > b :
    print(a ," is greater ")
else:
    print(b ," is greater")

'Largest of three numbers.'
a = 20
b = 30 
c = 40
if a > b and a > c :
    print(a , " is largest")
elif b > a and b > c :
    print(b , " b is greater")
else:
    print(c , " is greater")

'Leap year checker.'
year = 2026
if year % 400 == 0:
    print(year , " is a leap year")
elif year % 100 == 0:
    print(year , " is not a leap year")
elif year % 4 == 0:
    print(year , " is a leap year")
else:
    print(year , " is not a leap year")

'Vowel or consonant.'
char = 'e'
if char in 'aeiou':
    print(char , " is a vowel")
else:
    print(char , " is a consonant")

'Eligible to vote.'
age = 18
if age >= 18:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")

'Divisible by 5 and 11.'
number = 12
if number % 5 == 0 and number % 11 == 0:
    print('Divisible by 5 and 11')
else:
    print("Not Divisible by 5 and 11")

'Check alphabet, digit or special character.'
text = '123'
if text.isalpha():
    print("alphabet")
elif text.isdigit():
    print("digit")
elif text.isidentifier():
    print("Specal character")

'Grade calculator.'
number = 60
if number >= 90:
    print("A+")
elif number >= 80:
    print("A")
elif number >= 70:
    print("B")
elif number >= 60:
    print("C")
elif number >=50:
    print("D")
else:
    print("F")


#Intermediate
'Income tax calculator.'
income = float(input("Enter your annual income: "))

if income <= 600000:
    tax_rate = 0
elif income <= 1200000:
    tax_rate = 5
elif income <= 2400000:
    tax_rate = 10
elif income <= 5000000:
    tax_rate = 15
else:
    tax_rate = 20

tax = income * tax_rate / 100
net_income = income - tax

print("Annual Income:", income)
print("Tax Rate:", tax_rate, "%")
print("Tax Amount:", tax)
print("Net Income:", net_income)

'ATM withdrawal validation.'
balance = 10000
correct_pin = 1234

pin = int(input("Enter PIN: "))
amount = int(input("Enter withdrawal amount: "))

if pin == correct_pin:
    if amount > 0:
        if amount % 500 == 0:
            if amount <= balance:
                if balance - amount >= 500:
                    balance -= amount
                    print("Withdrawal Successful")
                    print("Remaining Balance:", balance)
                else:
                    print("Minimum balance of Rs.500 must remain.")
            else:
                print("Insufficient Balance")
        else:
            print("Amount must be a multiple of 500.")
    else:
        print("Invalid Amount")
else:
    print("Incorrect PIN")


'Login authentication.'
stored_username = "admin"
stored_password = "Admin123"

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == "":
    print("Username cannot be empty.")
elif password == "":
    print("Password cannot be empty.")
elif username == stored_username and password == stored_password:
    print("Login Successful")
else:
    print("Invalid Username or Password")

'Electricity bill calculator.'
units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 10
elif units <= 200:
    bill = units * 15
elif units <= 300:
    bill = units * 20
else:
    bill = units * 25

print("Electricity Bill = Rs.", bill)


'BMI category checker.'
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

bmi = weight / (height * height)

print("BMI =", round(bmi, 2))

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal Weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")


'Password strength checker.'
password = input("Enter Password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif not char.isalnum():
        has_special = True

if (
    len(password) >= 8
    and has_upper
    and has_lower
    and has_digit
    and has_special
):
    print("Strong Password")
else:
    print("Weak Password")

'Student scholarship eligibility.'
cgpa = float(input("Enter CGPA: "))
income = int(input("Enter Family Income: "))

if cgpa >= 3.8 and income < 50000:
    print("100% Scholarship")
elif cgpa >= 3.5 and income < 50000:
    print("50% Scholarship")
else:
    print("Not Eligible")

'Online shopping discount system.'
amount = float(input("Enter Total Purchase Amount: "))

if amount >= 20000:
    discount = 30
elif amount >= 10000:
    discount = 20
elif amount >= 5000:
    discount = 10
else:
    discount = 0

discount_amount = amount * discount / 100
final_amount = amount - discount_amount

print("Discount:", discount, "%")
print("Discount Amount:", discount_amount)
print("Final Amount:", final_amount)


'Traffic signal simulator.'
signal = input("Enter Signal Color: ").lower()

if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Get Ready")
elif signal == "green":
    print("Go")
else:
    print("Invalid Signal")


'Movie ticket pricing based on age.'
age = int(input("Enter Age: "))

if age < 5:
    price = 0
elif age <= 12:
    price = 300
elif age <= 59:
    price = 600
else:
    price = 400

print("Ticket Price = Rs.", price)