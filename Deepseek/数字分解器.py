# 数字分解器
num = (input("请输入一个三位整数："))
num1 = int(num)
a = num1 % 10
num1 = int(num1 / 10)
b = num1 % 10
c = int(num1 / 10)
print(f"{num}的百位是：{c}，十位是：{b}，个位是：{a}！")
