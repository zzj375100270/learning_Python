# 017讲课后作业1

for i in range(2, 10):
    if i == 2:
        print("2 是一个素数。")
    else:
        j = 2
        while j < i:
            if i % j == 0:
                x = int(i/j)
                print(f"{i} = {j} * {x}")
                break
            j = j + 1
        else: 
            print(f"{i}是一个素数。")