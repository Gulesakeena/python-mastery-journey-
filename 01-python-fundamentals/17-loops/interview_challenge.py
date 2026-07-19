'''Challenge 1

Predict

for i in range(5):
    print(i)
else:
    print("Done")'''

# 0 1 2 3 4 Done

'''Challenge 2

Output?

for i in range(5):

    if i == 3:
        break

else:

    print("Finished")'''

# No output

'''Challenge 3

Difference between

break

and

continue'''

# Immediately terminates the loop and exits it completely.
# Skips the current iteration and moves to the next iteration of the loop.

'''Challenge 4

Difference

pass

vs

continue'''

# pass is nothing it is only a placeholder when we write nothing
# continuous only skip the current itation and execut from the next itation


'''Challenge 5

Predict

for i in range(5):

    pass

print(i)'''

# 4

'''Challenge 6

Write your own range() using a generator.'''
def my_range(start, stop, step=1):

    while start < stop:
        yield start
        start += step


for i in my_range(1, 6):
    print(i)

'''Challenge 7

Print a matrix diagonally.'''
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(matrix)):
    print(matrix[i][i])

'''Challenge 8
Explain why modifying a list while iterating over it can cause bugs.'''
#Because when elements are added or removed during iteration,the indexes change.
#This may cause elements to be skipped,processed twice,or produce unexpected results.

'''
Challenge 9

Write nested loops to print a chessboard.'''
rows = 8
cols = 8

for i in range(rows):
    for j in range(cols):

        if (i + j) % 2 == 0:
            print("⬜", end=" ")
        else:
            print("⬛", end=" ")

    print()

'''Challenge 10

Implement FizzBuzz without using % (bonus challenge).'''
fizz = 0
buzz = 0

for i in range(1, 101):

    fizz += 1
    buzz += 1

    if fizz == 3 and buzz == 5:
        print("FizzBuzz")
        fizz = 0
        buzz = 0

    elif fizz == 3:
        print("Fizz")
        fizz = 0

    elif buzz == 5:
        print("Buzz")
        buzz = 0

    else:
        print(i)