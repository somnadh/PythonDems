a=["somnadh","kiran","rajesh"]
print(a) #['somnadh', 'kiran', 'rajesh']
print(a[2]) #rajesh
print(a[1:2]) #['kiran']
print(a[:]) #['somnadh', 'kiran', 'rajesh']
a.append(500)
print(a) #['somnadh', 'kiran', 'rajesh', 500]
a.insert(1,"waste")
print(a)#['somnadh', 'waste', 'kiran', 'rajesh', 500]
a.pop(0)
print(a)#['waste', 'kiran', 'rajesh', 500]