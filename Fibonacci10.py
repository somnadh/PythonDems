a=1
b=2
sum=2
while(1):
    if(sum>1000000):
        break
    d=a+b
    if(d%2==0):
        sum+=d
    a=b
    b=d
print("sum of even fibo below one million",sum)