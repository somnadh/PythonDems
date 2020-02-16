n=int(input("enter a number to print prime numbers"))
i=2
sum=0
while(i<=n):
    j=2
    count=2
    flag = 0
    while(j<i):
        if(i%j==0):
            flag=1
        j+=1
    if(flag==0):
        if(i>2):
           sum=sum+i
    i+=1
print(sum)
