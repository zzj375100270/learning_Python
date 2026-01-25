#024讲课后作业1
n = int(input("请输入三角形的行数："))
triangle = []
for i in range(n):
    row = [1]*(i+1)

    if i > 1:
        for j in range(1,i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
    triangle.append(row)

for a in range(n):
    num1 = int(8*((n-a-1))/2)
    print(' '*num1,end='')
    for b in range(a+1):
        num2 = 8-len(str(triangle[a][b]))
        print(triangle[a][b],end=' '*num2)
    print()