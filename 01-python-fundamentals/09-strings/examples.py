# Creating Strings
name = "Gul"
city = "Wazirabad"
print(name)
print(city)

# Indexing
print(name[1])
print(city[-3])

# Slicing
print(name[1:3])
print(city[-3,-5])

# Upper & Lower
print(name.upper())
print(name.lower())

# Remove Spaces
text = "  python  "
print(text.strip())

# Replace 
text = " Yello "
print(text.replace('Y','J'))

# Split
sentance = 'I , Love , python'
print(sentance.split(','))

# Concatenation 
first_name = 'Gul e'
second_name = "sakeena"
full_name = first_name + " " + second_name

# f-string
age = 21
print(f" My age is { age }")

# String Methods
print(name.startswith("G"))
print(name.endswith("e"))
print(name.isalpha())
print(name.isdigit())
print(name.count("e"))
print(name.find("l"))