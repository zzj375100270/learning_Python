#023讲课后作业0
import random
x = [0]*88
for i in range(88):
    x[i] = [0]*88
    for j in range(88):
        x[i][j] = random.randint(0,1024)

found = False
y = input("请输入一个待匹配的整数：")
for i in range(88):
    for j in range(88):
        if int(y) == x[i][j]:
            print(f"{i} {j}")
            found = True
if not found:
    print("没有这个数！")

