# 简易成绩判断
score = float(input('请输入你的分数：'))
if 90 <= score <= 100:
    print('优秀！')
if 60 <= score < 90:
    print('良好！')
if 0 <= score <60:
    print('不及格！')
else:
    print('请输入正确的成绩！')
