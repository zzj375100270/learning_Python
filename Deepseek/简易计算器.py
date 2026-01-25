# 简易计算器
num1 = input("请输入第一个数字：")
num2 = input("请输入第二个数字：")

和 = float(num1) + float(num2)
差 = float(num1) - float(num2)
积 = float(num1) * float(num2)


print(f'输入的两个数为{num1}和{num2}')
print(f'两数之和为{和}')
print(f'两数之差为{差}')
print(f'两数之积为{积}')
if float(num2) != 0:
    商 = float(num1) / float(num2)
    print(f'两数之商为{商}')
else:
    print('除数不能为0哦~')
