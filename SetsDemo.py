a=set()
b=set()
print("enter 5 elements")
for i in range(0,5):
    a.add(int(input()))

print("enter 4 elements")
for i in range(0,5):
    b.add(int(input()))

print(a,b)
c=a.copy()
a.update(b)
print(a)
print(c)
a.symmetric_difference_update(b)
print("symmetric difference",a)
print("a union b",a|b)
print("a intersection b",a&b)
print("a difference b",a-b)
print("b difference a",b-a)
print(" value (a-b)|(b-a)",(a-b)|(b-a))
print("(a|b)-(b&a)",(a|b)-(b&a))
print("a|(b-a)|b",a|(b-a)|b)

