def CheckEO(n):
    if(n%2==0):
        return True
    else:
        return False



def CheckPrime(n):
    c=0
    i=2
    while(i<n):
        if(n%i==0):
            c=1
            break
        i+=1
    if(c==0):
        return True
    else:
        return False


def CheckPalindrome(n):
    temp=n
    rev=0
    while(n!=0):
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    if(temp==rev):
        return True
    else:
        return False


def CheckArmstrong(n):
    temp=n
    rev=0
    while(n>0):
        rem=n%10
        rev=(rem*rem*rem)+rev
        n=n//10
    if (temp == rev):
        return True
    else:
        return False


def CheckPerfect(n):
    sum=0
    rev=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i

    if n == sum:
        return True
    else:
        return False


def CheckStrong(n):
    temp=n
    sum=0
    while(n>0):
        rem=n%10
        fact=1
        for i in range(1,rem+1):
            fact=fact*i
        sum=sum+fact
        n=n//10
    if (temp == sum):
        return True
    else:
        return False


a=int(input("enter any num to check prime or not"))
if(CheckPrime(a)==True):
    print("prime number")
else:
    print("Not prime number")
print(CheckEO(int(input("enter any num to check even or odd"))))
print(CheckPalindrome(int(input("enter any num to check palindrome or not"))))

print(CheckArmstrong(int(input("enter any num to check armstrong or not"))))
print(CheckPerfect(int(input("enter any num to check perfect or not"))))
print(CheckStrong(int(input("enter any num to check strong or not"))))
