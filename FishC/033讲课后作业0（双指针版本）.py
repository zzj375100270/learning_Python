#033讲课后作业0（双指针版本）
s = input("请输入字符串s：")
t = input("请输入字符串t：")
i,j = 0,0
while i < len(s) and j < len(t):
    if s[i] == t[j]:
        i += 1
    j += 1
if i == len(s):
    print("字符串s是字符串t的子序列。")
else:
    print("字符串s不是字符串t的子序列。")