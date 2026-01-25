#031讲课后作业0
string = input("请输入一个字符串（“单词“”以空格进行分隔）：")
if not string:
    print("0")
elif string.find(' ') == 0:
    print("1")
else:
    s = string.split()
    print(len(s))