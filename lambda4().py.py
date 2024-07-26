# this one is also solved by lambda function

city = ['patna','barh','goa','delhi','kota','muzaffarpur']

result = sorted(city, key = lambda x:len(x))
print("Sorted city:",result)

# this one is only solved by using lambda function() and then reverseing it...
city = ['patna','barh','goa','delhi','kota','muzaffarpur']
result = sorted(city, key = lambda x:len(x),reverse=True)
print("Sorted city:",result)