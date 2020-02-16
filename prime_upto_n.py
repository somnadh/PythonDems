n=int(input("enter a number to print prime numbers"))
i=2
while(i<=n):
    j=2
    count=2
    vikram = 0
    while(j<i):
        if(i%j==0):
            vikram=1
        j+=1
    if(vikram==0):
        print(i)
    i+=1
