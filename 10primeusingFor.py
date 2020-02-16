sum=0
k=2
for i in range(1,11):
    i=10
    c=0
    for j in range(2,k):
        if(k%j==0):
            c+=1
    if((c==0)and(k!=1)):
        print(k)
        sum+=k
    k+=1
print(sum)