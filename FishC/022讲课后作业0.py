# 022讲课后作业0

x = [[0]*3]*3

y = [0] * 3
for i in range(3):
    y[i] = [0]*3

z = [[0]*3]*3
for j in range(3):
    for i in range(3):
        z[j][i] = [0]*2

print(x)
print(y)
print(z)