# 021讲课后作业1

s = [2,2,3,2,4,6,2]
major = s[0]
count = 0

for i in s:
    if count == 0:
        major = i
    elif i == major:
        count += 1
    else:
        count -= 1

if s.count(major) > len(s)/2:
    print(f"{major}是主要元素。")
else:
    print("无主要元素。")