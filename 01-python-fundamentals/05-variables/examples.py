# Creating variables
name="Gul"
age=21
city="Wazirabad"

print(name)
print(age)
print(city)

# Multiple assignment
a = b = c = 100

print(a)
print(b)
print(c)

# Same value
a , b , c = 15

print(a)
print(b)
print(c)

# Output variables
print(name.age,city)

# String concatenation
first_name="Gul e"
last_name="sakeena"

print(first_name + " " + last_name)


# Numbers
num1 = 50
num2 = 25

print(num1 + num2)

# List unpacking
fruits=["apple","orange","banana"]
x,y,z = fruits
print(x)
print(y)
print(z)

# Global variable
language="python"

def show_language():
    print(language)

show_language()
