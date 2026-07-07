Mistake 1

I tried:

name[0] = "J"

Error:
TypeError

Reason:
Strings are immutable.

------------------------

Mistake 2

I confused find() with index().

Reality:

find() returns -1 if not found.
index() raises ValueError.

------------------------

Mistake 3

I forgot that slicing excludes the ending index.