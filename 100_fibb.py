#programme to print required fibonacci series

n=int(input("how many fibonacci term do u want")) 
a=0
b=1
c=a+b
count=2
print(a)
print(b)
while(1):
    if(count==n):
        break
    print(c)
    count+=1
    a=b
    b=c
    c = a + b
