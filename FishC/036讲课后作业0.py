#036讲课后作业0
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
    print("凯撒加密后的密文为：", new)
# 摩斯密文表
c_table = [".-", "-...", "-.-.", "-..", ".", "..-.",
           "--.", "....", "..", ".---", "-.-", ".-..",
           "--", "-.", "---", ".--.", "--.-", ".-.",
           "...", "-", "..-", "...-", ".--", "-..-",
           "-.--", "--..", ".----", "..---", "...--", "....-",
           ".....", "-....", "--...", "---..", "----.", "-----"]
# 摩斯明文表
d_table = ["A", "B", "C", "D", "E", "F",
           "G", "H", "I", "J", "K", "L",
           "M", "N", "O", "P", "Q", "R",
           "S", "T", "U", "V", "W", "X",
           "Y", "Z", "1", "2", "3", "4",
           "5", "6", "7", "8", "9", "0"]
new_code = []
for each in new:
    if each.isalnum():
        j = d_table.index(each.upper())
        new_code.append(c_table[j])

print(f"凯撒、摩斯混合加密后的密文是：{' '.join(new_code)}")
