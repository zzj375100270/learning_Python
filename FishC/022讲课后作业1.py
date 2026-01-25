#022讲课后作业1
#摩尔投票法1/3

s = [1,2,3,4,1,2,3,4,1,2,3,1,2,1,2,2]
major1 = s[0]
for i in range(1,len(s)):
    if s[i] != major1:
        major2 = s[i]
        break

count1 = 0
count2 = 0

for a in range(len(s)):
    if s[a] == major1:
        count1 += 1
    elif s[a] != major1 and s[a] != major2:
        count1 -= 1
        if count1 == 0:
            major1 = s[a]
            count1 = 1

for b in range(i,len(s)):
    if s[b] == major2:
        count2 += 1
    elif s[b] != major2 and s[b]!= major1:
        count2 -= 1
        if count2 == 0:
            major2 = s[b]
            count2 = 1

if s.count(major1) < s.count(major2):
    major1,major2 = major2,major1
print(f"占比最高的两个元素是{major1}和{major2}。")
if s.count(major2) > len(s)/3:
    print(f"{major1}和{major2}占比都超过了1/3。")
elif s.count(major1) < len(s)/3:
    print(f"{major1}和{major2}占比都没超过1/3。")
else:
    print(f"{major1}占比超过了1/3，{major2}占比没超过1/3。")
