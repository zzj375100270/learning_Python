#028讲课后作业1
old = input("请输入需要加密的明文：")
trans_old = input("请输入需要替换的字符：")
trans_new = input("请输入将要替换的字符：")
if len(trans_old) != len(trans_new):
    print("需要替换的字符数量必须跟将要替换的字符数量一致！")
else:
    table = str.maketrans(trans_old,trans_new)
    new = old.translate(table)
    print(new)
    trans = False
    for a in trans_new:
        if trans_new.count(a) > 1:
            trans = True
            break
    for b in trans_old:
        if trans_old.count(b) > 1:
            trans = True
            break
    if trans:
        print("由于替换字符出现冲突，该密文无法解密！")