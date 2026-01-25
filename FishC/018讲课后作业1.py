# 018讲课后作业1
# 回文数

num = input("请输入一个正整数：")
x = len(num)
num1 = int(num)
b = 0
for i in range(1,x+1):
    a = num1 % 10
    b = b + a * (10**(x-i))
    num1 = num1 // 10
if b == int(num):
    print(f"{num}是一个回文数！")
else:
    print(f"{num}不是一个回文数！")