def funA(x):
    result = x
    def funB(y):
        nonlocal result
        result *= y
        def funC(z):
            nonlocal result
            result *= z
            return result
        return funC
    return funB
print(f"funA(2)(3)(4)的结果是{funA(2)(3)(4)}")