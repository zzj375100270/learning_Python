# 三个整数排序
a = int(input("请输入第一个整数："))
b = int(input("请输入第二个整数："))
c = int(input("请输入第三个整数："))
num1 = a
num2 = b
num3 = c
if num1 < b:
    num1 = b
if num1 < c:
    num1 = c
if num3 > b:
    num3 = b
if num3 > a:
    num3 = a
if num2 == num1 or num2 == num3:
    num2 = a
if num2 == num1 or num2 == num3:
    num2 = c
print(f"三个整数从小到大排序是{num3}<{num2}<{num1}")
