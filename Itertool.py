import itertools as i
sum=0
k=2
primecount=0
for i in i.repeat(1):
    if(primecount==10):
        break
    c=0
    for j in range(2,k):
        if(k%j==0):
            c+=1
    if((c==0)and(k!=1)):
        print(k)
        primecount+=1
        sum+=k
    k=k+1
print(sum)