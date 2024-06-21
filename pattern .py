# ****
# ****
# ****
# ****
# ****

for i in range(0,5):
    for j in range(0,5):
        print("*",end=" ")
    print() 


# *****
# *   *
# *   *
# *   *
# *****

for i in range(0,5):
    for j in range (0,5):
        if i==0 or i == 5-1 or j==0 or j==5-1:
            print("*",end=" ")
        else:
            print(' ',end=' ')
    print()


# *
# **
# ***
# ****
# *****

for i in range(1,5+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()


#     *
#    **
#   ***
#  ****
# *****

for i in range(5):
    for j in range(1,5-i):
        print(" ",end=" ")
    for k in range(0,i+1):
        print("*",end=" ")
    print()


# *****
# ****
# ***
# **
# *
n=int(input("enter number: "))
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()


# *****
#  ****
#   ***
#    **
#     *

n=int(input("enter number: "))
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for k in range(n,i,-1):
        print("*",end=" ")
    print()


#     *
#    ***
#   *****
#  *******
# *********

for i in range(1,5+1):
    for j in range(n-i):
        print(' ',end=' ')
    for k in range(2*i-1):
        print("*",end=" ")
    print()

# 1
# 12
# 123
# 1234
# 12345

for i in range(5):
    for j in range(i+1):
        print(j+1,end=" ")
    print()










