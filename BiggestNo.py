a=int(input("enter any num"))
big=0
rem=0`wsqa
while(a>0):
    rem=a%10
    if(big<rem):
        big=rem
    a=a//10
print(big)