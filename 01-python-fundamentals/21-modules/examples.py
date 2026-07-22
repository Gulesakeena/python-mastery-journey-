"""
21 - Python Modules
"""

# ----------------------------
# import
# ----------------------------

import math 
print(math.sqrt(100))
print(math.factorial(10))

# ----------------------------
# from ... import
# ----------------------------

from math import sqrt
print(sqrt(64))


# ----------------------------
# Alias
# ----------------------------
import math as m
print(m.pi)

# ----------------------------
# Multiple Imports
# ----------------------------
from math import factorial,sqrt
print(factorial(10))
print(sqrt(90))


# ----------------------------
# Built-in Modules
# ----------------------------

import random 
print(random.randint(1,10))

import datetime
print(datetime.datetime.now())

# ----------------------------
# __name__
# ----------------------------

print(__name__)


# ----------------------------
# __main__
# ----------------------------

def greet():
    print("Hello!")

if __name__ == "__main__":
    greet()