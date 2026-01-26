#033讲课后作业1
old = input("输入：")
if not old.isdigit():
    print("输入错误！")
else:
    for i in range(len(old)-1,-1,-1):
        if int(old[i]) % 2 == 1:
            new = old[:i+1]
            break
        else:
            new = '0'
    print(f'输出：{new}')
