#029讲课后作业0
text = input("请输入text的内容：")
words = input("请输入words的内容：")
word_list = words.split()
result = []
for word in word_list:
    for i in range(len(text)-len(word)+1):
        if text[i:(i+len(word))] == word:
            result.append([i,i+len(word)-1])
result.sort()
print(result)