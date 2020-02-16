n=int(input("enter the number"))
i=1
c=0
while(n>=i):
    if(n%i==0):
        c+=1
    i+=1
if(c==2):
    print(n,"is a prime number")
else:
    print(n,"is a not prime number")