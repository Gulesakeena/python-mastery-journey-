# 22 - Python Dates

## Learning Objectives

After completing this topic, you should be able to:

- Understand Python's `datetime` module.
- Get the current date and time.
- Create custom dates.
- Extract year, month, day, hour, minute, and second.
- Format dates using `strftime()`.
- Parse strings into dates using `strptime()`.
- Perform date arithmetic with `timedelta`.

---

# Why Do We Need Dates?

Dates and times are used in almost every application:

- User registration
- Login history
- Banking transactions
- Attendance systems
- Logging
- Scheduling
- AI model timestamps

Python provides the built-in `datetime` module for working with dates and times.

---

# Importing the Module

```python
import datetime
```

or

```python
from datetime import datetime
```

---

# Current Date & Time

```python
from datetime import datetime

now = datetime.now()
print(now)
```

---

# Current Date

```python
from datetime import date

today = date.today()
print(today)
```

---

# Creating a Date

```python
from datetime import datetime

birthday = datetime(2004, 5, 12)

print(birthday)
```

---

# Accessing Components

```python
now.year
now.month
now.day

now.hour
now.minute
now.second
```

---

# Formatting Dates

Use `strftime()`.

Example:

```python
now.strftime("%d/%m/%Y")
```

Common format codes:

| Code | Meaning | Example |
|------|---------|---------|
| %Y | 4-digit year | 2026 |
| %y | 2-digit year | 26 |
| %m | Month | 07 |
| %d | Day | 22 |
| %H | Hour (24-hour) | 15 |
| %I | Hour (12-hour) | 03 |
| %M | Minute | 45 |
| %S | Second | 09 |
| %A | Weekday | Monday |
| %B | Month name | July |

---

# Converting String to Date

Use `strptime()`.

```python
from datetime import datetime

date = datetime.strptime("22-07-2026", "%d-%m-%Y")

print(date)
```

---

# Date Arithmetic

Use `timedelta`.

```python
from datetime import datetime, timedelta

today = datetime.now()

tomorrow = today + timedelta(days=1)

yesterday = today - timedelta(days=1)
```

You can also add:

- days
- weeks
- hours
- minutes
- seconds

---

# Difference Between Two Dates

```python
from datetime import datetime

d1 = datetime(2026, 1, 1)
d2 = datetime(2026, 12, 31)

difference = d2 - d1

print(difference.days)
```

---

# Common Interview Questions

## Q1. Which module is used for dates?

```python
datetime
```

---

## Q2. Difference between `datetime` and `date`?

- `date` stores only the date.
- `datetime` stores both date and time.

---

## Q3. Which function gives the current date and time?

```python
datetime.now()
```

---

## Q4. Which method formats a date?

```python
strftime()
```

---

## Q5. Which method converts a string into a date?

```python
strptime()
```

---

# Best Practices

- Use `datetime.now()` for timestamps.
- Use `strftime()` for displaying dates.
- Use `strptime()` when reading user input.
- Use `timedelta` for date calculations.

---

# Key Takeaways

- Python uses the `datetime` module for working with dates and times.
- `datetime.now()` returns the current date and time.
- `strftime()` formats dates into readable strings.
- `strptime()` converts strings into `datetime` objects.
- `timedelta` is used for date calculations.