#unique and mutable but their element are immutable
collection={1,2,3,4}
print(collection)
print(type(collection))

coll=set()#empty set
print(type(coll))
coll.add(1)
coll.add(2)
print(coll)
coll.remove(1)
print(coll)
coll.clear()
print(coll)


s1={1,2,3}
s2={2,3,4}
print(s1.union(s2))
print(s1.intersection(s2))




word={
    # "key":"value",
    "table":["a piece of furniture","list of facts & figure"],
    "cat":"a small animal"
}
print(word)


sub={
    "python","C++","python","js","java",
    "python","java","C++","C"
}
print(len(sub))


# marks={}

# x=int(input("enter phy: "))
# marks.update({"phy":x})

# x=int(input("enter che: "))
# marks.update({"che":x})

# x=int(input("enter maths: "))
# marks.update({"maths: ":x})
# print(marks)


values1={9,"9.0"}
print(values1)

value2={"9","9.0"}
print(value2)