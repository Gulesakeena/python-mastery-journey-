# ---------------------------
# Arithmetic Operators
# ---------------------------

a = 15
b = 4

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# ---------------------------
# Assignment Operators
# ---------------------------

x = 10

x += 5
print(x)

x -= 3
print(x)

x *= 2
print(x)

x /= 4
print(x)

# ---------------------------
# Comparison Operators
# ---------------------------

print(10 == 10)
print(10 != 5)
print(10 > 5)
print(5 < 3)
print(10 >= 10)
print(5 <= 8)

# ---------------------------
# Logical Operators
# ---------------------------

age = 20

print(age > 18 and age < 30)
print(age < 18 or age == 20)
print(not(age == 20))

# ---------------------------
# Identity Operators
# ---------------------------

a = [1,2]
b = a
c = [1,2]

print(a is b)
print(a is c)

print(a == c)

# ---------------------------
# Membership Operators
# ---------------------------

name = "Python"

print("P" in name)
print("Z" not in name)

numbers = [1,2,3,4]

print(3 in numbers)

# ---------------------------
# Bitwise Operators
# ---------------------------

print(5 & 3)
print(5 | 3)
print(5 ^ 3)
print(~5)
print(5 << 1)
print(5 >> 1)