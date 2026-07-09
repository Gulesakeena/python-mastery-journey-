Mistake 1

I used:

append([1,2])

instead of

extend([1,2])

Result:

Nested list was created.

-------------------

Mistake 2

I forgot:

list.copy()

and accidentally modified the original list.

-------------------

Mistake 3

I thought:

sort()

returns a new list.

Reality:

It sorts in place and returns None.