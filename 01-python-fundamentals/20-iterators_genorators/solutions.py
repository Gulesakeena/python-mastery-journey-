# Beginner
'Create an iterator from a list.'
number = [1,2,3,4]
it = iter(number)

'Print elements using next().'
print(next(it))
print(next(it))
print(next(it))
print(next(it))

'Iterate over a string manually.'
string = "python"
it = iter(string)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

'Iterate over a tuple.'
tup = (1,2,3,4)
it = iter(tup)
print(next(it))
print(next(it))
print(next(it))
print(next(it)) 

'Iterate over a dictionary.'
dic = {"name" : "ALI" , "age" : 21}
it = iter(dic)
print(next(it))
print(next(it)) 

'Catch StopIteration.'
def own_for_loop(iterabe):
    while True:
        try:
            print(next(iterabe))
        except StopIteration:
            break
    
'Count items using an iterator.'
numbers = [10, 20, 30, 40, 50]
count = 0
iterator = iter(numbers)
while True:
    try:
        next(iterator)
        count = count+1
    except StopIteration:
            break
print(count)


'Print only even numbers.'
numbers = [1,2,3,4,5,6,7,8,9,10]
iterator = iter(numbers)
while True:
    try:
          it = next(iterator)
          if it % 2 == 0:
               print(it)
    except StopIteration:
        break

'Convert a set into an iterator.'
my_set = {10, 20, 30, 40}

iterator = iter(my_set)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

'Reverse a list and iterate.'
number = [1,2,3,4,5]
iterator = iter(reversed(number))
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

# Intermediate
'Create a custom iterator that prints numbers 1–10.'
class Counter:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        current = self.start
        self.start+=1
        return current
        

counter = Counter(1,11)
for i in counter:
    print(i)
        
        
'Create an iterator that prints only odd numbers.'
numbers = [1,2,3,4,5,6,7,8,9,10]
iterator = iter(numbers)
while True:
    try:
          it = next(iterator)
          if it % 2 != 0:
               print(it)
    except StopIteration:
        break

'Countdown iterator (10 to 1).'
class Counter:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        current = self.end
        self.end-=1
        return current
        

counter = Counter(0,10)
for i in counter:
    print(i)

'Alphabet iterator (A–Z).'
class Alphabet:

    def __init__(self):
        self.current = ord('A')

    def __iter__(self):
        return self

    def __next__(self):

        if self.current > ord('Z'):
            raise StopIteration

        letter = chr(self.current)
        self.current += 1

        return letter


obj = Alphabet()

for letter in obj:
    print(letter)


'Square number iterator.'
class Counter:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        current = self.start
        self.start+=1
        return current*current
        

counter = Counter(1,11)
for i in counter:
    print(i)