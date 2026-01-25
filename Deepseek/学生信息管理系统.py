# 学生信息管理系统

# 题目：输入学生姓名、语文成绩、数学成绩、英语成绩
# 计算总分和平均分（保留1位小数）
# 根据平均分判断等级：90+优秀，80+良好，70+中等，60+及格，不及格

import sys

name = input("请输入你的姓名：")
chinese = float(input("请输入你的语文成绩："))
math = float(input("请输入你的数学成绩："))
english = float(input("请输入你的英语成绩："))
total = chinese + math + english
everage = total / 3

if (chinese >100 or chinese <0) or (math >100 or math <0) or (english >100 or english <0):
    print("成绩输入错误！")
    sys.exit()

if 90 <= everage <=100:
    level = "优秀"
elif 80 <= everage <90:
    level = "良好"
elif 70 <= everage <80:
    level = "中等"
elif 60 <= everage <70:
    level = "及格"
elif 0 <= everage <60:
    level = "不及格"

print(f"{name}同学，你的总成绩是{total:.1f}，平均分是{everage:.1f}，你的等级是{level}！")