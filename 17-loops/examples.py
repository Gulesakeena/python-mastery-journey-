# while loop 
i = 1
while i <= 5 :
    print(i)
    i=i+1

# for loop
for i in range(5):
    print(i)

# range 
for i in range(1,10,2):
    print(i)

# break
for i in range(10):
    if i == 5 :
        break
    print(i)

# continue
for i in range(10):
    if i%2 == 0:
        continue
    print(i)

# pass
for i in range(10):
    if i == 2:
        pass
    print(i)

# else
for i in range(5):
    print(i)
else:
    print("loop finish")

# enumerate
names = ["Ali","Sara","Ahmed"]
for index , name in enumerate(names,start=1):
    print(index,name)

#Zip
names = ["Ali","Sara","Ahmed"]
marks = [90,85,45]
for names,marks in zip(names,marks):
    print(names,marks)

# reversed
for i in reversed(range(5)):
    print(i)

# nested loop
for i in range(3):
    for j in range(3):
        print(i,j)
    
# multiplication table
for i in range(1,6):

    for j in range(1,6):

        print(i*j,end="\t")

    print()