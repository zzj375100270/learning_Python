# 015课后作业0

alcohol = int(input("请输入酒精含量："))

if 0 <= alcohol < 20:
    print("您没有饮酒！")

elif 20 <= alcohol < 80:
    print("您酒驾了！请跟我们走一趟！")

elif alcohol >= 80:
    print("您醉驾了！芭比Q咯~")

else:
    print("输入错误！")