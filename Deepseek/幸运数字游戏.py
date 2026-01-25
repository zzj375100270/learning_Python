# 幸运数字游戏
import random

num2 = random.randint(1,10)
i = 2
while i > 0:
    i = i - 1
    num = input("猜一下幸运数字是多少~输入1-10之间的整数：")
    num1 = int(num)
    if num1 == num2:
        print(f"你猜对啦，幸运数字是{num1}！")
        break
    elif num1 < num2:
        print("小啦~")
    else:
        print("大啦~")
print(f"游戏结束！幸运数字是{num2}")
