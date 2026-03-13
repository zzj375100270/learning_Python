def calc():
    while True:
        num1 = input("请输入第一个数字：")
        if num1.lower() == "q":
            break
        num2 = input("请输入第二个数字：")
        if num2.lower() == "q":
            break
        func = input("请输入你需要的运算(+ - * /)")
        if func.lower() == "q":
            break
        if func not in ("+","-","*","/"):
            raise ValueError("输入的运算有误")
            continue
        try:
            x = float(num1)
            y = float(num2)
            if func == "+":
                result = x + y
            elif func == "-":
                result = x - y
            elif func == "*":
                result = x * y
            elif func == "/":
                result = x / y
        except ValueError:
            print("输入的数字有误")
            continue
        except ZeroDivisionError:
            print("除数不能为0")
            continue
        else:
            print(f"{num1} {func} {num2} = {result}")
        
