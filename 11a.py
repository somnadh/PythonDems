r=int(input("Enter No of Rows for 1st Matrix:"))
c=int(input("Enter No of column for 1nd Matrix:"))
matrix = []
print("Enter the entries rowwise:")
for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input()))
    matrix.append(a)


for i in range(r):
    for j in range(c):
        print(matrix[i][j], end=" ")
    print()