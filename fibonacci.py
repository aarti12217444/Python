# a=0
# b=a+1=0+1=1
# c=1+1=2
# d=2+1=3
# .
# .
# .
# .

# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         print(a, end=" ")
#         a, b = b, a + b

# num_terms = int(input("Enter the number of terms: "))
# fibonacci(num_terms)


# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         print(a, end=" ")
#         a , b=b, a+b
        
# num_terms=int(input("Enter number: "))
# fib(num_terms)


def fib(n):
    a,b=0,1
    for _ in range(n):
        print(a,end=" ")
        a, b=b ,a+b
num_term=int(input("Enter number: "))
fib(num_term)