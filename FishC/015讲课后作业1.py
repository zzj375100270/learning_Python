n = int(input("请输入一个正整数："))

while n > 0:
    if n % 2 == 0:
        a = int(n/2)
        print(f"{n}/2 = {a}")
        n = int(n / 2)
    else:
        b = int(n*3+1)
        print(f"{n}*3+1 = {b}")
        n = int(n*3+1)
    if n == 1:
        break

