from Methods import CheckEO, CheckPrime, CheckArmstrong, CheckPerfect,CheckPalindrome,CheckStrong

#print(CheckEO(int(input("enter any to check even or odd"))))
print(CheckPrime(int(input("enter any to check prime or Not"))))
#print(CheckArmstrong(int(input("enter any to check armstrong  or Not"))))
print("even numbers")
for i in range(1,100):
    if(CheckEO(i)==True):
        print(i)

print("odd numbers")
for i in range(1,100):
    if(CheckEO(i)!=True):
        print(i)


print("Armstrong numbers")
for i in range(100, 500):
    if (CheckArmstrong(i)):
        print(i)


print("perfect numbers")
for i in range(1, 1000):
    if (CheckPerfect(i)):
        print(i)



print("palindrome numbers")
for i in range(100, 500):
    if (CheckPalindrome(i)):
        print(i)

print("Strong numbers")
for i in range(100, 500):
    if (CheckStrong(i)):
        print(i)