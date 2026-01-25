# 猜拳游戏
import random
user = int(input("剪刀石头布，输入1=石头，2=剪刀，3=布："))
computer = random.randint(1,3)
if user == computer:
    print("平局！")
elif (user == 1 and computer == 2) or (user == 2 and computer == 3) or (user == 3 and computer == 1):
    print("你赢啦！")
else:
    print("你输啦！")
