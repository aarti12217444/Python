numbers = [90, 67, 47, 78, 100,89,44,129,56,89,90,67,45,26,78,100]

result = sorted(list(filter(lambda x:x % 2==0 ,numbers)))
print("Even number:",result)
