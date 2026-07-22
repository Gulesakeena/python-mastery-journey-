"""
23 - Python Math
"""

import math

# ----------------------------
# Constants
# ----------------------------

print("Pi:", math.pi)
print("Euler:", math.e)

# ----------------------------
# Square Root
# ----------------------------

print(math.sqrt(81))

# ----------------------------
# Power
# ----------------------------

print(math.pow(2, 5))
print(2 ** 5)

# ----------------------------
# Absolute Value
# ----------------------------

print(abs(-50))

# ----------------------------
# Ceiling & Floor
# ----------------------------

print(math.ceil(4.2))
print(math.floor(4.9))

# ----------------------------
# Factorial
# ----------------------------

print(math.factorial(6))

# ----------------------------
# GCD
# ----------------------------

print(math.gcd(48, 18))

# ----------------------------
# Logarithms
# ----------------------------

print(math.log(10))
print(math.log10(100))

# ----------------------------
# Exponential
# ----------------------------

print(math.exp(2))

# ----------------------------
# Trigonometry
# ----------------------------

angle = math.radians(90)

print(math.sin(angle))
print(math.cos(angle))
print(math.tan(angle))

# ----------------------------
# Degree Conversion
# ----------------------------

print(math.degrees(math.pi))

# ----------------------------
# Infinity & NaN
# ----------------------------

print(math.inf)
print(math.nan)

print(math.isinf(math.inf))
print(math.isnan(math.nan))

# ----------------------------
# Built-in vs Math
# ----------------------------

print(round(4.6))
print(pow(2, 3))
print(math.pow(2, 3))

# ----------------------------
# Mini Example
# ----------------------------

radius = 7

area = math.pi * radius ** 2

print("Circle Area:", area)