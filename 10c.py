def gcd(n,m):
    while(n!=m):
        if(n>m):
            n=n-m
        else:
            m=m-n
    return n
def lcm(n, m):
 return n * m / gcd
n1 = int(input("Enter n1 value:"))
n2 = int(input("Enter n2 value:"))
gcd = gcd(n1, n2)
print("GCD value is:",gcd)
print("LCM value is:",int(lcm(n1,n2)))