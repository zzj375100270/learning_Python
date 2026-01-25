# 工作日判断
day = int(input("请输入你想查询的是星期几，以数字1-7表示："))
if 1 <= day <= 5:
    print("这一天是工作日！")
elif day == 6 or day == 7:
    print("这一天是周末！")
else:
    print("无效输入")
