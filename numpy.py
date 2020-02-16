
R1 = int(input("Enter the number of rows for First Matrix:"))
C1 = int(input("Enter the number of columns for First Matrix:"))
a1=[]
print("enter", R1*C1, "elements")
for i in range(0,R1):
    a1.append([])
    for j in range(0,C1):
        a1[i].append(int(input()))



R2 = int(input("Enter the number of rows for Second Matrix:"))
C2 = int(input("Enter the number of columns for Second Matrix:"))
a2=[]
print("enter", R2*C2, "elements")
for i in range(0,R2):
    a2.append([])
    for j in range(0,C2):
        a2[i].append(int(input()))
print("addition of two matrix")
for i in range(0,R2):
    for j in range(0,C2):
        print(a1[i][j]+a2[i][j],end=' ')
    print()

