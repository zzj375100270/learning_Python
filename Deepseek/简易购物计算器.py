# 简易购物计算器

price1 = 18.9
price2 = 25.5
price3 = 32.2

num1 = int(input("第一件商品买了几件？"))
num2 = int(input("第二件商品买了几件？"))
num3 = int(input("第三件商品买了几件？"))

price = price1 * num1 + price2 * num2 * price3 * num3
if price > 100:
    price = price * 0.9

print(f"你今天消费的金额是{price:.2f}元！")