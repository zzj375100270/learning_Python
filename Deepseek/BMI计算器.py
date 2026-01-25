# BMI计算器
height = float(input('请输入你的身高m：'))
weight = float(input('请输入你的体重kg：'))
BMI = weight / (height ** 2)
if BMI < 18.5:
    print(f'你的BMI等于{BMI:.1f}，偏瘦')
elif BMI < 24:
    print(f'你的BMI等于{BMI:.1f}，正常')
elif BMI < 28:
    print(f'你的BMI等于{BMI:.1f}，超重')
else:
    print(f'你的BMI等于{BMI:.1f}，肥胖')
