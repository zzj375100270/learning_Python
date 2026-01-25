import random
counts = int(input('请输入抛硬币的次数：'))
i = 0
print("开始抛硬币实验：")
while i < counts:
    num = random.randint(0,1)
    if num % 2 == 1:
        print('正面',end=' ')
    else:
        print('反面',end=' ')
    i = i + 1
   
