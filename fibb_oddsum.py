n=int(input("enter a number to print fibonacci upto n"))
a=0
b=1
c=a+b
sum=1
while(c<=n):
    if(c%2!=0):
        sum=sum+c
    a=b
    b=c
    c = a + b
print(sum)