range = [1,2,3,4,5]
for i in range:
    print(i)

tup = (1,2,3,4,5,6)
for i in tup:
    print(i)

str = "abcdefghijklmnopqrstuvwxyz"
for char in str:
    if(char == "o"):
        print(char,"is found")
        break
    print(char)
else:
    print("End")


num=[1,4,9,16,25,36,49,64,81,100]
for i in num:
    print(i)

num=[1,4,9,16,25,36,49,64,81,100]
x=9
indx=0
for i in num:
    if(i==x):
        print("found",indx)
        indx += 1
        break
else:
    print("not found")