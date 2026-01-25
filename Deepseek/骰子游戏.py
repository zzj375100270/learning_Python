# 骰子游戏
import random
answer = input("游戏开始吗？Y/N：")
if answer == "Y" or answer == "y":
    user = random.randint(1,6)
    computer = random.randint(1,6)
    if user == computer:
        print(f'你的点数是{user}，电脑的点数是{computer}，平局！')
    elif user < computer:
        print(f'你的点数是{user}，电脑的点数是{computer}，你输啦！')
    else:
        print(f'你的点数是{user}，电脑的点数是{computer}，你赢啦！')
else:
    print("游戏结束！")

