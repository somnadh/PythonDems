n=int(input("enter the number"))
a=0
b=1
c=1
flag=0
while(n>=c):
    c=a+b
    if(c==n):
       flag=1
       break
    a=b
    b=c
if(flag==1):
    print(n,"is fibonacci term")
else:
    print(n,"is not fibonacci term")