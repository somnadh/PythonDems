a=int(input("enter First number"))
b=int(input("enter second number"))
c=a+b;
print(c)
print(a//b)
"FLOOR DIVISION it gives only integer value after the decimal point are removed"
print(a/b)
print(a**2)
"Exponent"
print(a%b)
"""modulo gives reminder"""
print("===================================")
print("Comparison operators")
print (a>b)
print (a<b)
print (a>=b)
print (a<=b)
print (a!=b)
print (a==b)
print("===================================")
print("Assignment operators")
c=a+b
print (c)
a+=b
"""like this we have a-=b,a*=b,...a//=b all arithmetic operators """
print(a)
print("===================================")
print("Bitwise operators")
a,b=6,2
print (a&b) #2
print(a^b)#xor 4
print (a|b) #6
print(~a) #-7 binari compliment
print(a<<2)#left shift"""
print(a>>2)#right shift
print("===============================")
print("Logical Operators")
print(a>b)and (a<b)
print(a>b)or (a<b)
print (not(a>b))
print("===============================")
print("Membership Operators")
name="somunadham kinthada"
fname="kiran"
mname="kumar"
sname="boddu"
print(fname in name)#returns true if it exits
print(fname not in name) #returns true if it nit exits
print("===============================")
print("identity Operators")
a=10
b=10
print(a is b) #it compare the memory location of two objects
print(a is not b)
print(id(a)==id(b))
