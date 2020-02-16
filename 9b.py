def dups(list):
    for i in list:
        count = list.count(i)
        if count > 1:
            print ('There are duplicates in list')
            return True
    print ('There are no duplicates in list' )
    return False

a = [2,4,16,8,78]
b = [2,8,3,2,8,785,457]
print(a)
dups(a)
print(b)
dups(b)