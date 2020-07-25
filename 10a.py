#programme to print cummulative product
def product(l):
    p =1
    for i in l:
        p *= i
    return p
a= [1,2,3,4,5,6,7,8,9,10]
c=product(a)
print("Cummulative product of",a,"is==>",c)
