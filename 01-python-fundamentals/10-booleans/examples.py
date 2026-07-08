# Boolean values
print(True)
print(False)

# Type
print(type(True))
print(type(False))

# Comparison
print(5 > 6)
print(10 == 10)
print(6 != 7)

# bool()
print(bool(1))
print(bool(0))

print(bool(''))
print(bool("python"))

print(bool([]))
print(bool([1,2,3]))

print(bool({}))
print(bool({'a':1}))

# Logical Operators
age = 20
print(age > 18 and age < 30)
print(age > 30 or age == 20)
print(not(age > 18))

values = [
    0,
    1,
    "",
    "Hello",
    [],
    [1],
    {},
    {"a":1},
    None,
    False,
    True
] 
for value in values:
    print(value , bool(value))