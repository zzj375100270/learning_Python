#032讲课后作业0
old = input("请输入待压缩的字符串：")
word = old[0]
num = 1
new_word = []
for i in range(1,len(old)):
    if old[i] == word:
        num += 1
    else: 
        if num >= 3:
            new_word.append(f'{word}{num}')
        else:
            new_word.append(word*num)
        word = old[i]
        num = 1
if num >= 3:
    new_word.append(f'{word}{num}')
else:
    new_word.append(word*num)
new = ''.join(new_word)
percent = len(new) / len(old)
print(f'压缩后的字符串是：{new}\n压缩率为：{percent:.2%}')