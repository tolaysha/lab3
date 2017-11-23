h=[1,2,3,4,5]
a=[i**3 for i in h]
print(a)
print(list(map(lambda x: x**3, h)))
