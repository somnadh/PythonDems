r = int(input("enter a range"))
a = []
for i in range(r):
    a.append(int(input()))
tup=tuple(a) #converting list into tuple
print(tup)
s=set(tup) #converting tuple into set
print(s)
