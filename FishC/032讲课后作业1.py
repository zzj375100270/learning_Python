#032讲课后作业1
old = input("请输入待解压的字符串：")
if not old.isalnum():
    print("请输入正确的字符串！")
else:
    new = []
    num = ''
    current = old[0]
    for i in range(1,len(old)):
        if old[i].isalpha():
            if old[i] == current:
                new.append(current)
            elif num:
                new.append(current*(int(num)-1))
                current = old[i]
                new.append(current)
                num = ''
            else:
                current = old[i]
                new.append(current)
        elif old[i].isdigit():
            num += old[i]
    if num:
        new.append(current*(int(num)-1))
    print(f'解压后的字符串是：{''.join(new)}')