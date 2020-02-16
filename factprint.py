n=int(input("enter one number"))
i=1
fact=1
x=''
while(i<=n):
    fact*=i
    if(i!=n):
        x+=str(i)+"x"
    else:
        x+=str(i)
    i+=1
print(str(n)+"!="+x+"=",fact)