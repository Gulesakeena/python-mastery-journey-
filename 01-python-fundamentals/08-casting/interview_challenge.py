'''Challenge 1

Predict the output:

print(int(5.99))

Why?'''

5 
# why because the int tupecasting convert the float to int 

'''Challenge 2

Predict the output:

print(bool(""))
print(bool(" "))
print(bool("0"))
print(bool(0))
print(bool(0.0))

Explain every line.'''

False # empty string in boolean typecasting return false
True # string with 1 space in boolean typecasting return true
True # string with 0 in boolean typecasting return true
False # 0 in boolean typecasting return false 
False # 0.0 in boolean typecasting return false 

'''Challenge 3

What happens?

print(int("123"))
print(int("12.3"))

Why does one work and the other fail?'''

123
12.3

'''Challenge 4

Predict the output:

print(float(10))
print(str(10))
print(bool(10))'''

10.0
"10"
True

'''Challenge 5

Without running:

x = "50"
y = 20

print(x + str(y))

Output?'''

5020

'''Challenge 6

Fix the code:

age = "21"

print(age + 5)'''

age = "21"

print(int(age) + 5)

'''Challenge 7 (Interview Favorite)

Explain why:

print(int(True))
print(int(False))

returns:

1
0  '''

# because in python the True gives the 1 and False gives the  0

'''Challenge 8

Predict:

print(bool([]))
print(bool([1]))
print(bool({}))
print(bool({"a":1}))'''

False
True
False
True


'''Challenge 9 (Hard)

Write a function:

safe_int(value)

Behavior:

safe_int("100") → 100
safe_int("abc") → None
safe_int("") → None
safe_int("10.5") → None

Use try/except.'''

def safe_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


value = input("Enter any value: ")

print(safe_int(value))


'''Challenge 10 (Very Hard)

Implement your own converter.

Create:

convert(value, target_type)

Examples:

convert("100", int)
convert("3.14", float)
convert(50, str)
convert(0, bool)

If conversion fails, return:

None'''

def convert(value, target_type):
    try:
        if target_type == "int":
            return int(value)

        elif target_type == "float":
            return float(value)

        elif target_type == "str":
            return str(value)

        else:
            return "Unsupported type."

    except ValueError:
        return "Can't be converted."


value = input("Enter value: ")
target_type = input("Enter target type (int, float, str): ")

result = convert(value, target_type)

print(result)

