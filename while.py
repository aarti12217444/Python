#print hello 5 times
i=1
while(i<=5):
    print("h")
    i += 1
    
j = 1
while(j<=5):
    print(j)
    j += 1

j = 1
while(j<=5):
    print("*")
    j += 1

#print num from 1 to 100
num=1
while(num <= 100):
    print(num)
    num += 1

#print num from 100 to 1
num=100
while(num >= 1):
    print(num)
    num -= 1


#print the multiplication table of a num n
n=int(input("enter n: "))
i=1
while(i<=10):
    print(n*i)
    i += 1


#print the element of the following list using loop
num=[1,4,9,16,25,36,49,64,81,100]
i=0
while (i<len(num)):
    print(num[i])
    i += 1
   

#search for a number x in this tuple using loop
num=(1,4,9,16,25,36,49,64,81,100)
x=81
i=0
while (i<len(num)):
    if(num[i]==x):
        print("FOUND at indx",i)
    i += 1