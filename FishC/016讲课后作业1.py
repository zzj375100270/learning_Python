import random

counts = int(input("请输入抛硬币的次数："))
i = 0
a = 0    # 正面次数
b = 0    # 反面次数

print("开始抛硬币实验……")

if counts < 100:
    while i < counts:
        num = random.randint(1, 10)

        if num % 2:
            print("正面", end=" ")
            a = a + 1
        else:
            print("反面", end=" ")
            b = b + 1
        i += 1
    print(f"\n一共模拟了{counts}次抛硬币，结果如下：\n正面：{a}次\n反面：{b}次")

elif counts >= 100:
    while i < counts:
        num = random.randint(1, 10)

        if num % 2:
            a = a + 1
        else:
            b = b + 1
        i += 1
    print(f"\n一共模拟了{counts}次抛硬币，结果如下：\n正面：{a}次\n反面：{b}次")