a = int(input("enter a number"))
temp=a
rem=0
rev=0
while (a>0):
    rem = a % 10
    rev = (rev * 10) + rem
    a = a/10
print(rev)
if(rev==temp):
    print(temp," is a palindrome")
else:
    print(temp,"is not palindrome")
