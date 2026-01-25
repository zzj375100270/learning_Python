#027讲课后作业0
s = input("请输入你想转换的字符串：")
j = 0
while j <= len(s)-2:
    if s[j] == s[j+1].swapcase():
        s = s[:j] + s[j+2:]
        if j > 0:
            j -= 1
    else:
        j += 1
print(s)