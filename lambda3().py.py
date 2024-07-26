# this one is also solved by lambda function but by using function

city = ['patna','barh','goa','delhi','kota','muzaffarpur']
def length(city):
    return len(city)
result = sorted(city, key = length)
print("Sorted city:",result)

# this one is only solved by using lambda function()
city = ['patna','barh','goa','delhi','kota','muzaffarpur']
result = sorted(city, key = lambda x:len(x))
print("Sorted city:",result)