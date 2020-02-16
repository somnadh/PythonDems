r = int(input("enter a range"))
a = []
for i in range(r):
    a.append(int(input()))
tup=tuple(a) #converting list into touple
print(tup)
s=set(tup) #converting touple into set
print(s)