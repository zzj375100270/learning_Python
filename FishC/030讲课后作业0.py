#030讲课后作业0
code = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
old = input("请输入需要加密的明文（只支持英文字母）：")
step = input("请输入移动的位数：")
if not step.lstrip('-').isdigit():
    print("请输入正确的位数！")
else:
    step = int(step)
    step = step % 52
    new_code = code[step:]+code[:step]
    new_code = new_code[:26].upper()+new_code[26:].lower()
    new = []
    for each in old:
        if each.isalpha() and each.isascii():
            new.append(new_code[code.index(each)])
        else:
            new.append(each)
    new1 = ''.join(new)
    print(new1)