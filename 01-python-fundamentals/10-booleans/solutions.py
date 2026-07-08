#Beginner
'Print True.'
print(True)

'Print False.'
print(False)

'Check if 10 > 5.'
print(10 > 5)

'Check if 5 == 8.'
print(5 == 8)

'Convert 0 into Boolean.'
print(bool(0))

'Convert 100 into Boolean.'
print(bool(100))

'Convert an empty string into Boolean.'
print(bool(''))

'Convert "Python" into Boolean.'
print(bool("Python"))

'Convert an empty list into Boolean.'
print(bool([]))

'Convert a non-empty dictionary into Boolean.'
print(bool({}))

#Intermediate
'Check whether a number is positive.'
number = int(input("enter a number"))
if number > 0:
    print(True)
else:
    print(False)

'Check whether a person is eligible to vote.'
age = int(input("Enter age: "))
if age >= 18:
    print("person is eligible to vote")
else:
    print("person is not eligible to vote")

'Check whether a number is even.'
number = input("Enter a number")
if number % 2 == 0:
    print("Number is even")
else:
    print("Number is not even")

'Check whether a year is a leap year.'
year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not a Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")

'Check whether a password length is at least 8 characters.'
password = input("Enter a password")
if len(password) >= 8:
    print(" password length is of least 8 characters")
else:
    print(" password length is not of least 8 characters")

'Check whether two strings are equal.'
str_1 = "python"
str_2 = "Python"

if str_1 == str_2 :
    print("both strings are equal")
else:
    print("these string are not equal")

'Check whether a number lies between 10 and 100.'
number = int(input("Enter a number : "))
if number >= 10 and number <= 100 :
    print("it is lies between between 10 and 100")
else:
    print("it is not lies between 10 and 100")

'Use and, or, and not in different examples.'
# Use and
age = 20
has_id = True
if has_id :
    print(age >= 18 and has_id)

# Use or 
age = 16
has_permission = True

print(age >= 18 or has_permission)
 
# Use not
is_logged_in = True
print(not is_logged_in)

'Write a Boolean expression that returns True only if both numbers are positive.'
number_1 = int(input("Enter 1st number: "))
number_2 = int(input("Enter 2nd number: "))

if number_1 > 0 and number_2 > 0:
    print("Both numbers are positive")
else:
    print("Not positive")

'Print whether a username is empty or not.'
username = input("Enter a username : ")
if username == "" :
    print("User name is enpty")
else :
    print("Username is nt empty")
