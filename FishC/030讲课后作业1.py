#030讲课后作业1
line1 = 'qwertyuiop'
line2 = 'asdfghjkl'
line3 = 'zxcvbnm'
words = ['Twitter','TOTO','FishC','Python','ASL']
output = []
for word in words:
    word1 = word.lower()
    is_True = True
    for i in range(1,len(word)):
        if line1.find(word1[0]) != -1:
            if line1.find(word1[i]) == -1:
                is_True = False
                break
        elif line2.find(word1[0]) != -1:
            if line2.find(word1[i]) == -1:
                is_True = False
                break
        else:
            if line3.find(word1[i]) == -1:
                is_True = False
                break
    if is_True:
        output.append(word)
print("输入：words = ['Twitter','TOTO','FishC','Python','ASL']")
print(f"输出：{output}")