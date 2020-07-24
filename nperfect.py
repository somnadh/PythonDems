n=int(input("enter any number to print up to n"))
j=1
while(j<=n):
    i=1
    temp=j
    perfect=0
    while(j>i):
        if(j%i==0):
            perfect=perfect+i
        i+=1
    if(temp==perfect):
        print(temp,"perfect number")
    j+=1
