#040讲课后作业1
import hashlib
code_book = {}
for i in range(1000000):
    code = hashlib.md5(bytes(str(i),"utf-8"))
    code_book[str(i)] = code.hexdigest()
codes = input("请输入md5码：")
for num,code in code_book.items():
    if codes == code_book[num]:
        print(f"明文密码是{num}")