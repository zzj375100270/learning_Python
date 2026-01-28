#034讲课后作业0
s = [1,8,7,3,6,5,4,2]
odd = []
even = []
for each in s:
    if each % 2 == 1:
        odd.append(each)
    else:
        even.append(each)
odd.sort()
even.sort()
print(odd + even)