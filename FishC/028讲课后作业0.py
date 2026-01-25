#028讲课后作业0
v1 = input('请输入第一个版本号，v1 = ')
v2 = input('请输入第二个版本号，v2 = ')
v1_new = v1.split('.')
v2_new = v2.split('.')
max_len = len(v1_new) if len(v1_new)>=len(v2_new) else len(v2_new)
v1_new.extend(['0']*(max_len-len(v1_new)))
v2_new.extend(['0']*(max_len-len(v2_new)))
v1v2 = True
for i in range(max_len):
    if int(v1_new[i]) > int(v2_new[i]):
        print('v1')
        v1v2 = False
        break
    elif int(v1_new[i]) < int(v2_new[i]):
        print('v2')
        v1v2 = False
        break
if v1v2:
    print('v1 = v2')