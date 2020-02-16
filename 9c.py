def Unique(list):
    unique = set(list)
    for i in unique:
        count = list.count(i)
        if count > 1:
            print ('There are no unique elements in list')
            return True
    print ('There are unique elements in list' )
    return False
a = [2,4,16,8,78]
b = [2,8,3,2,8,785,457]
print(a)
Unique(a)
print(b)
Unique(b)