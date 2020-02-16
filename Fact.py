a = int(input("enter number"))
fact=1
n=a
while(a>0):
    fact=fact*a
    a=a-1
while(n>1):
    print(n,"*",n-1)
    n-=1
print(fact)