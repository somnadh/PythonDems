n=int(input("enter an number"))
an=0
temp=n
while(n>0):
    rem=n%10
    an=an+(rem**3)
    n=n//10
if(an==temp):
    print(temp,"is armstrong number")
else:
    print(temp,"is not armstrong number")

