# Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def unique(x):
    return list(set(x))
    
sample = input("enter element: ").split(',')
unique1 = unique(sample)
print("sample: ",sample)
print("unique_elements: ",unique1)