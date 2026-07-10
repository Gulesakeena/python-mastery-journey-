Mistake 1

Used

student["age"]

for a missing key.

Result:

KeyError

Correct:

student.get("age")

------------------------

Mistake 2

Used list as dictionary key.

Lists are mutable and cannot be hashed.

------------------------

Mistake 3

Thought duplicate keys are allowed.

Reality:

The last value overwrites previous ones.