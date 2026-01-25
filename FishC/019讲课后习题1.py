# 019讲课后习题1

nums = []
while True:
    new = input("请录入一个整数（输入STOP结束）：")
    if new != 'STOP':
        nums.append(int(new))
    else:
        break
target = int(input("请录入目标整数："))

n = len(nums)
for i in range(n):
    for j in range(i,n):
        if nums[i] + nums[j] == target:
            print([i,j])
