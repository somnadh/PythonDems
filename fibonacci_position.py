n = int(input("enter a number"))
rem=0
a=0
b=1
flag=0
loc=0
while(n>0):
    rem = n % 10
    loc+=1
    c = 1
    while (rem >= c):
        c = a + b
        if (c == rem):
            print("fibonacci found at",loc)
            flag=1
            break
        a = b
        b = c
    n=n/10;
if(flag==1):
    print("fibonacci found")
else:
    print("fibonacci not found")