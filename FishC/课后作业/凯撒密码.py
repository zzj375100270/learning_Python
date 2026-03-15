#凯撒密码
old = input("请输入需要加密的明文（只支持英文字母）：")
step = input("请输入移动的位数：")
if not step.lstrip('-').isdigit():
    print("请输入正确的位数！")
else:
    step = int(step) % 26
    new = ""
    for char in old:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + step) % 26 + base)
            new += new_char
        else:
            new += char
    print("加密后的密文为：", new)