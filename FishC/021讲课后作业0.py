# 021讲课后作业0

s = [2,2,4,2,3,6,2]
s.sort()
num = s[len(s)//2]
if s.count(num) > len(s)//2:
    print(f'{num}是主要元素。')
else:
    print('没有主要元素。')