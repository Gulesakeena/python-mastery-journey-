Mistake 1

Used {}

Thinking it creates an empty set.

Reality:

{} creates an empty dictionary.

Correct:

set()

------------------------

Mistake 2

Tried to add a list into a set.

Lists are mutable and unhashable.

------------------------

Mistake 3

Used remove() for an element that didn't exist.

Result:

KeyError

Better:

discard()