# n=int(input()) 
# s = n  # assigning input value to the s variable
# b = len(str(n))
# sum1 = 0
# while n != 0:
#     r = n % 10
#     sum1 = sum1+(r**b)
#     n = n//10
# if s == sum1:
#     print("The given number", s, "is armstrong number")
# else:
#     print("The given number", s, "is not armstrong number")






n=int(input("Enter number: "))
b=len(str(n))
a=n
sum=0
while(n != 0):
    r=n % 10
    sum=sum+(r**b)
    n=n // 10
if a == sum:
    print("The given numbern",a, "is a armstrong number")
else:
    print("The given numbern",a, "is not a armstrong number")
 