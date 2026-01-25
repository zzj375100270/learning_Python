#029讲课后作业1
s = input("请输入一个由字母构成的字符串：")
if s.isalpha() == False:
    print("请输入正确的字符！")
n = len(s)
is_True = False
for each in s:
    if each != s[0]:
        is_True = False
        break
    is_True = True
for i in range(2,n//2+1):
    if n % i == 0 and s[:i]*(n//i) == s:
        is_True = True
print(is_True)