i = 100
j = int(input("Enter upper range: "))
for num in range(i, j + 1):
    sum = 0
    temp = num
    while temp > 0:
        rem = temp % 10
        sum += rem**3
        temp =temp//10
    if num == sum:
        print(num)