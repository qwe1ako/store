import random
number= random.randint(0,200)
print(number)
count=7
money=5000
while True:
    money = money-500
    count = count -1
    a = input("输入个数吧:")
    a = int(a)
    if  count == 0:
        print("次数耗尽，剩余钱数",money,)
        break
    if money <= 0:
        print("余额耗尽，可惜！！！")
        break
    if a > number:
        print("===大了些===","剩余",count,"次剩余￥",money,)
    elif a < number :
        print("===小了些===","剩余",count,"次剩余￥",money,)
    elif a < number or a > number:
        money = money - 500
    else:
        money = money + 2000
        if count <= 3:
            money = money + 5000
        print("！！答对了！！", "剩余", count, "次""剩余钱数￥", money, )








