#027讲课后作业1
s = input("请输入符合规则的字符串：")
alpha = 'abcdefghijklmnopqrstuvwxyz'
length = len(s)
s1 = []
s2 = []
s3 = []
for i in range(0,length,2):
    s1.append(s[i])
    a = (alpha.index(s[i]) + int(s[i+1])) % 26
    s2.append(alpha[a])
for j in range(length//2):
    s3 += s1[j]+s2[j]
s4 = ''.join(s3)
print(s4)