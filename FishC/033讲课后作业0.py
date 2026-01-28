#033讲课后作业0
s = input("请输入字符串s：")
t = input("请输入字符串t：")
s_in_t = True
s_index = 0
for each in s:
    if each in t[s_index:]:
        s_index = t.index(each,s_index) + 1
        continue
    else:
        s_in_t = False
        break
if s_in_t:
    print("字符串s是字符串t的子序列。")
else:
    print("字符串s不是字符串t的子序列。")