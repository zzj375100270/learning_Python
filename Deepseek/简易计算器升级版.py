# 简易计算器升级版
a = input("请输入第一个数字：")
b = input("请输入第二个数字：")
c = input("请输入你需要的运算（+、-、*、/）：")
num1 = float(a)
num2 = float(b)
if c == '+':
    result = num1 + num2
    print(f'{a} + {b} = {result}')
elif c == '-':
    result = num1 - num2
    print(f'{a} - {b} = {result}')
elif c == '*':
    result = num1 * num2
    print(f'{a} * {b} = {result}')
elif c == '/':
    if num2 != 0:
        result = num1 / num2
        print(f'{a} / {b} = {result}')
    else:
        print("除数不能为0！")
else:
    print("输入错误！")
