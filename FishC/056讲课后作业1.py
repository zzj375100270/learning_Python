while True:
    try:
        result = eval(input("请输入一行语句："))
        if result:
            print(f"结果是：{result}")
    except ZeroDivisionError:
        print("错误：除数为0")
    except KeyboardInterrupt:
        print("\n程序结束~")
        break
    except NameError:
        print("错误：变量未定义")
    except SyntaxError:
        print("错误：语法错误")
    except ValueError:
        print("错误：传入的参数类型不恰当")
    except IndexError:
        print("错误：索引错误")