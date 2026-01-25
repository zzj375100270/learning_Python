# 年龄阶段判断
age = int(input('请输入你的年龄：'))
if age < 0:
    print("年龄错误！")
elif 0 <= age <=12:
    print("你是儿童！")
elif 13 <= age <= 17:
    print("你是青少年！")
elif 18 <= age <= 40:
    print("你是青年！")
elif 41 <= age <= 60:
    print("你是中年！")
else:
    print("你是老年！")
