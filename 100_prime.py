a=int(input("how many prime numbers do u want"))
i=2
pcount=0
while 1:
    if(pcount==a):
        break
    flag = 0
    j=2
    while(j<i):
        if(i%j==0):
            flag=1
        j+=1
    if(flag==0):
        print(i)
        pcount+=1
    i+=1