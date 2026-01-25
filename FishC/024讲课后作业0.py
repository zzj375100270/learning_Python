#024讲课后作业0
n = int(input("请输入三角形的行数："))
triangle = []
for i in range(n):
    row = [1]*(i+1)

    if i > 1:
        for j in range(1,i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
    triangle.append(row)

for a in triangle:
    for b in a:
        print(b,end=' ')
    print()