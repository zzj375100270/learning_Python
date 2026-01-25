# 简单加密器
num = int(input("请输入一个三位整数："))
c = num % 10
num = int(num / 10)
b = num % 10
a = int(num / 10)
a = (a + 3) % 10
b = (b + 3) % 10
c = (c + 3) % 10
print(f"加密后的数字为{a}{b}{c}")
