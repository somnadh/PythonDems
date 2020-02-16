a=int(input("enter a nubmer"))
big=0
rem=0
while(a>0):
    rem=a%10
    if(rem>big):
        big=rem
    a=a//10
print(big)
