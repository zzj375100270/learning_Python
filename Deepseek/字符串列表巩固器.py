#字符串列表巩固器
# 给定一个混合字符串，如：s = "a1b22c333d4444e"
# 1. 将所有的数字字符挑出来，组成一个新字符串。
# 2. 将所有的字母字符挑出来，组成一个新字符串。
# 3. (挑战) 计算所有数字字符代表的数值之和（例如“22”是2+2，不是22）。
# 这能巩固遍历、分支、字符判断和类型转换。

s = 'a1b22c333d4444e'
alpha_list = [each for each in s if each.isalpha()]
digit_list = [each for each in s if each.isdigit()]
sum_digit = 0
for i in range(len(digit_list)):
    sum_digit += int(digit_list[i])
print(f"新的字母字符串为：{''.join(alpha_list)}")
print(f"新的数字字符串为：{''.join(digit_list)}")
print(f"数字字符串的总和为：{sum_digit}")