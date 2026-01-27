# 问题：处理学生成绩数据
# 1. 过滤掉不及格的成绩（<60）
# 2. 给每个成绩加上5分（老师调分）
# 3. 将成绩转为等级制（A: >=90, B: >=80, C: >=70, D: >=60）
# 4. 统计每个等级的人数

# 原始数据
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
scores = [85, 45, 92, 78, 60]

print("原始成绩:", dict(zip(students, scores)))

# 第一步：过滤掉不及格的
# 同时处理学生和成绩，所以要zip在一起过滤
student_score_pairs = list(zip(students, scores))
passed_pairs = list(filter(lambda pair: pair[1] >= 60, student_score_pairs))
print("\n及格的学生:", passed_pairs)

# 第二步：给成绩加5分
adjusted_pairs = list(map(lambda pair: (pair[0], pair[1] + 5), passed_pairs))
print("\n调分后的成绩:", adjusted_pairs)

# 第三步：转为等级制
def score_to_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    else:
        return 'D'

grade_pairs = list(map(lambda pair: (pair[0], score_to_grade(pair[1])), adjusted_pairs))
print("\n等级制:", grade_pairs)

# 第四步：统计等级人数
from collections import Counter  # 我们还没有学，先看看效果
grade_counter = Counter(grade for _, grade in grade_pairs)
print("\n等级统计:", dict(grade_counter))