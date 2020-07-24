a=int(input("enter any number"))
i=1
temp=a
perfect=0
while(a>i):
    if(a%i==0):
        perfect=perfect+i
    i+=1
if(temp==perfect):
    print(temp,"perfect number")
else:
    print(temp,"not perfect number")
