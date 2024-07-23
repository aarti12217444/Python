# Write a program to create a Dictionary using two Lists

d1 = input("data1: ").split(",")
d2 = input("data2: ").split(",")
if len(d1) == len(d2):
	t = dict(zip(d1,d2))
	print(sorted(t.items()))
else:
	print("length should be equal")