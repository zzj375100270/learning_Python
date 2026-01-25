# 数字比较器
a = input("请输入第一个数字：")
b = input("请输入第二个数字：")
c = input("请输入第三个数字：")
num1 = float(a)
num2 = float(b)
num3 = float(c)
print(f'你输入的三个数字分别为{a}、{b}和{c}')
if num1 > num2 and num1 > num3:
    print(f'三个数里最大的是{a}~')
elif num2 > num1 and num2 > num3:
    print(f'三个数里最大的是{b}~')
else:
    print(f'三个数里最大的是{c}~')
