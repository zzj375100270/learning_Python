i = 0
x = 0
while i <= 1e6:
    if i % 2 == 0:
        x = x + i
        i = i + 2
print("1000000 以内所有偶数的和是" + str(x))
