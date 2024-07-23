#  Write a Program to Concatenate Two Dictionaries

d1 = list(map(int,input("data1: ").split(",")))
d2 = list(map(int,input("data2: ").split(",")))
d3 = list(map(int,input("data3: ").split(",")))
d4 = list(map(int,input("data4: ").split(",")))
a = dict(zip(d1,d2))
b = dict(zip(d3,d4))
for i in b.keys():
	if i in a.keys():
		a[i]+=b[i]
	else:
		a[i]=b[i]
print("concatenation:",list(sorted(a.items())))




