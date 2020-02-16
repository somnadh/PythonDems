r=int(input("Enter No of Rows for 1st Matrix:"))
c=int(input("Enter No of column for 1nd Matrix:"))
matrix = []
print("Enter the entries rowwise:")
for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input()))
    matrix.append(a)
r1=int(input("Enter No of Rows for 2nd Matrix:"))
c1=int(input("Enter No of column for 2nd Matrix:"))
matrix1 = []
print("Enter the entries rowwise:")
for i in range(r1):
    a1 = []
    for j in range(c1):
        a1.append(int(input()))
    matrix1.append(a1)
result=[[0 for j in range(0,r)] for i in range(0,c)]
for i in range(r1):
    for j in range(c1):
        result.append(0)
if r==c1:
    for i in range(r):
        for j in range(c):
            for k in range(c1):
                result[i][j]+=matrix[i][k]*matrix1[k][j]

    for i in range(r):
        for j in range(c):
            print(result[i][j], end=" ")
        print()
else:
    print("Matrix Multiplication is impossible")

