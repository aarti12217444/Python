numbers = [90, 67, 47, 78, 100]
def even(x):
    return x % 2==0
result = list(filter(even,numbers))
print("Even number:",result)
