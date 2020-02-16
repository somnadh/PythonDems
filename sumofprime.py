a=int(input("enter any number to print sum of prime"))
b=a
sum=0;
while(a>1):
    c=0
    i=2
    while(i<a):
        if(a%i==0):
            c+=1
            break
        i+=1;
    if(c==0):
        sum+=a;
    a-=1
print("sum of prime upto",b,"is==>", sum)