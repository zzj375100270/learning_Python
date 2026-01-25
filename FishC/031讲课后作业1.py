#031讲课后作业1
old = input("请输入一个只包含字母和数字的字符串：")
if not old.isalnum():
    print("输入错误！")
else:
    alpha = []
    nums = []
    new = []
    for each in old:
        if each.isalpha():
            alpha.append(each)
        elif each.isdigit():
            nums.append(each)
    a = len(alpha)
    n = len(nums)
    if abs(a - n) != 1:
        print("字符串中数字和字母的数量不满足重新格式化的条件！")
    else:
        if a > n:
            for i in range(n):
                new.extend([alpha[i],nums[i]])
            new.append(alpha[-1])
        else:
            for i in range(a):
                new.extend([nums[i],alpha[i]])
            new.append(nums[-1])
    print(''.join(new))