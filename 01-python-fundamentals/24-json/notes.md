# 24 - Python JSON

## What is JSON?

JSON stands for **JavaScript Object Notation**.

It is a lightweight data format used to exchange data between applications.

Almost every REST API sends and receives JSON.

Example

```json
{
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "FastAPI", "AI"]
}
```

---

# Why JSON?

JSON is used in:

- REST APIs
- FastAPI
- Flask
- Django
- AI Applications
- Configuration Files
- Mobile Apps
- Web Applications
- Databases

---

# Import Module

```python
import json
```

---

# Python Dictionary vs JSON

Python

```python
person = {
    "name": "Ali",
    "age": 22
}
```

JSON

```json
{
    "name": "Ali",
    "age": 22
}
```

Difference:

- Python uses dictionaries.
- JSON is a text format.

---

# Convert JSON String → Python Object

Use `json.loads()`.

```python
import json

text = '{"name":"Ali","age":22}'

data = json.loads(text)

print(data)
print(type(data))
```

Output

```
{'name': 'Ali', 'age': 22}
<class 'dict'>
```

---

# Convert Python Object → JSON String

Use `json.dumps()`.

```python
person = {
    "name": "Sara",
    "age": 24
}

json_text = json.dumps(person)

print(json_text)
```

---

# Pretty Printing

```python
print(json.dumps(person, indent=4))
```

---

# Sort Keys

```python
print(json.dumps(person, indent=4, sort_keys=True))
```

---

# Write JSON to File

Use `dump()`.

```python
with open("data.json", "w") as file:
    json.dump(person, file, indent=4)
```

---

# Read JSON File

Use `load()`.

```python
with open("data.json") as file:
    data = json.load(file)

print(data)
```

---

# Convert Python Types

| Python | JSON |
|---------|------|
| dict | object |
| list | array |
| str | string |
| int | number |
| float | number |
| True | true |
| False | false |
| None | null |

---

# Handling Invalid JSON

```python
import json

try:
    json.loads("{name}")
except json.JSONDecodeError:
    print("Invalid JSON")
```

---

# Best Practices

- Always validate JSON.
- Use `indent=4` for readability.
- Prefer dictionaries when working in Python.
- Use JSON for data exchange.

---

# Interview Questions

## Difference between load() and loads()?

- `load()` → Reads JSON from a file.
- `loads()` → Reads JSON from a string.

---

## Difference between dump() and dumps()?

- `dump()` → Writes JSON to a file.
- `dumps()` → Converts Python object to JSON string.

---

## What module is used for JSON?

```python
json
```

---

## What is the JSON equivalent of Python None?

```
null
```

---

# Key Takeaways

- JSON is the standard format for APIs.
- `loads()` converts JSON string → Python object.
- `dumps()` converts Python object → JSON string.
- `load()` reads JSON files.
- `dump()` writes JSON files.