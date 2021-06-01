print("-------------！！汽车大甩卖商城！！——————————————")
import random

quan = random.randint(1, 6)
a = "奥迪30元代金券"
b = "奔驰20元代金券"
c = "兰博基尼15元代金券"
while True:
    if quan == 1 or quan == 2 or quan == 3:
        aa = 30
        bb = 0
        print("您抽取的优惠券:", a)
        break
    elif quan == 4 or quan == 5 or quan == 6:
        bb = 20
        aa = 0
        print("您抽取的优惠卷为:", b)
        break
count = 1
d = [
    ["奔驰", 20, bb],
    ["奥迪", 30, aa]
]

cart = [
    ["奔驰￥", 250, "W"],
    ["奥迪￥", 110, "W"],
    ["兰博基尼￥", 500, "W"],
    ["volvo￥", 80, "W"],
    ["雷克萨斯￥", 90, "W"],
    ["凯迪拉克￥", 20, "W"]
]
mycart = []
money = int(input("请输入您带的钱："))
while True:
    for j, s in enumerate(cart):
        print("可选车型：", j, s)
    h = input("选择购车型编号：")
    if h.isdigit():
        num = int(h)
        if num > len(cart):
            print("您选择的商品不存在")
        if money < cart[num][1]:
            print("可惜，钱不够")
            break
        money = money - cart[num][1]
        for i, u in enumerate(d):
            if cart[num][0] == u[0]:
                # print(cart[num][0])
                if count == 1 and u[2] != 0:
                    count = count - 1
                    money = money + u[1]
        else:
            mycart.append(cart[num])
            print("----------------------购买成功，剩余余额", money)

    if h == "t" or h == "T":
        print("再见")
        break
l=0
print("消费如下：","一共购买",len(mycart),"辆车")
for jj,ss in enumerate(mycart):
    l=l+ss[1]
print(mycart)
print("您余额为：￥",money,"消费了：",l)

