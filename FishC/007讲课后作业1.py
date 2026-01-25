import random
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,\
     21,22,23,24,25,26,27,28,29,30,31,32,33]
num1 = random.sample(x,6)
num2 = random.randint(1,16)
print("开奖号码是：",*num1)
print("特别号码是：",num2)
