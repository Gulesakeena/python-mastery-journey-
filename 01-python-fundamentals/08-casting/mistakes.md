Mistake 1

I tried:

int("12.5")

Error:
ValueError

Reason:
"12.5" is not a valid integer string.

Correct:
float("12.5")

------------------------

Mistake 2

I thought:

bool("False")

would return False.

Reality:

Any non-empty string is True.

------------------------

Mistake 3

I forgot that int() truncates the decimal part instead of rounding.