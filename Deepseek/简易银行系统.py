# 简易银行系统

money = 1000

while True:
    call = input("""请输入你的指令：
                1、存款
                2、取款
                3、查询
                4、退出\n""")
    

    if call == "1":
        money_get = float(input("存款金额："))
        if money_get < 0:
            print("存款金额需大于0！")
        else:
            money = money + money_get
            print(f"您的余额为：{money:.2f}")
    
    elif call == "2":
        money_away = float(input("取款金额："))
        if money < money_away:
            print("余额不足！")
        else:
            money = money - money_away
            print(f"您的余额为：{money:.2f}")
    
    elif call == "3":
        print(f"您的余额为：{money:.2f}")

    elif call == "4":
        print("感谢您的使用！")
        break

    else:
        print("指令错误！")
