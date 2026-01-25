#023讲课后作业1
import random

m = int(input("请输入行数："))
n = int(input("请输入列数："))
list1 = random.choices(range(1025),k=m*n)
s = [0]*m
for i in range(m):
    s[i] = [0]*n
    for j in range(n):
        s[i][j] = list1[-1]
        list1 = list1[:-1]

lucky_num = []
min_a = []
min_b = []
for a in range(m):
    for b in range(n):
        if s[a][b] == min(s[a]):
           min_a.append(a)
           min_b.append(b)
is_max = True
for x in range(m):
    if s[min_a[x]][min_b[x]] < s[x][min_b[x]]:
        is_max = False
        break
if is_max:
    lucky_num.append(s[min_a[x]][min_b[x]])

if lucky_num:
    print(lucky_num)
else:
    print("No Lucky number!")
