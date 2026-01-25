# 九九乘法表

i = 1
while i <= 9:
    j = 9
    while j >= i:
        print(j," * ",i," = ",i*j,end=' ')
        j -= 1
    print()
    i += 1