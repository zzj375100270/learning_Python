for i in range(1,10):
    for j in range(9,i-1,-1):
        print(j, "x", i, "=", i * j, end=' ')
    print("\n")