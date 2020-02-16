n=int(input("enter a number to print fibonacci upto n"))
a=0
b=1
c=a+b
print(a,b)
while(c<=n):
    print(c)
    a=b
    b=c
    c = a + b