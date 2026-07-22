"""
22 - Python Dates
"""

# -----------------------------
# Import Module
# -----------------------------

import datetime

# -----------------------------
# Current Date & Time
# -----------------------------

now = datetime.datetime.now()

print("Current Date & Time:", now)

# -----------------------------
# Current Date
# -----------------------------

today = datetime.date.today()

print("Today's Date:", today)

# -----------------------------
# Create Custom Date
# -----------------------------

birthday = datetime.datetime(2004, 5, 12)

print("Birthday:", birthday)

# -----------------------------
# Access Date Components
# -----------------------------

print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)

print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

# -----------------------------
# Formatting Dates
# -----------------------------

print(now.strftime("%d/%m/%Y"))
print(now.strftime("%A"))
print(now.strftime("%B"))
print(now.strftime("%d %B %Y"))
print(now.strftime("%I:%M %p"))

# -----------------------------
# String to Date
# -----------------------------

date_string = "22-07-2026"

converted = datetime.datetime.strptime(
    date_string,
    "%d-%m-%Y"
)

print(converted)

# -----------------------------
# Date Arithmetic
# -----------------------------

from datetime import timedelta

tomorrow = now + timedelta(days=1)

yesterday = now - timedelta(days=1)

next_week = now + timedelta(weeks=1)

print("Tomorrow:", tomorrow)
print("Yesterday:", yesterday)
print("Next Week:", next_week)

# -----------------------------
# Difference Between Dates
# -----------------------------

d1 = datetime.datetime(2026, 1, 1)
d2 = datetime.datetime(2026, 12, 31)

difference = d2 - d1

print("Difference:", difference.days, "days")

# -----------------------------
# Mini Example
# -----------------------------

print(
    f"Today is {now.strftime('%A, %d %B %Y')}"
)