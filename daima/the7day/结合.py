while True:
    print("1.旅游   2.购车")
    what=int(input("您想干什么："))
    if what==1:
        travel={
            "北京":{
                "昌平区":{
                    "bb",
                    "jj",
                    "hh",
                    "yy",

                },
                "海淀区":{
                    "北京大学",
                    "清华大学",
                    "中央党校",
                },
                "朝阳区":{
                    "龙城",
                    "双塔",
                },
            },
            "上海":{
                "静安区":{
                    "静安寺",
                    "马勒别墅",
                },
                "陆家嘴":{
                    "cbd",
                    "东方明珠",
                },
                "浦东区":{
                    "迪士尼",
                },
            },
            "山西":{
                "阳泉":{
                    "翠峰山",
                    "某某山",
                },
                "太原":{
                    "乔家大院",
                    "曹家大院",
                },
                "临汾":{
                    "某酒庄",
                    "采摘园",
                },
            }
        }
        def print_travel(can):
            for o in can:
                print(o,"\t")
        print_travel(travel)
        chose1=input("输入城市：")
        while True:
            if chose1 in travel:
                print_travel(travel[chose1])
                chose2=input("请输入市/区：")
                if chose2 in travel[chose1]:
                    print_travel(travel[chose1][chose2])
                    chose3=input("请输入景区：")
                    if chose3 in travel[chose1][chose2]:
                        print_travel(travel[chose1][chose2])
                        print("选择成功，选择的为",chose3)
                        break
                    elif chose3=="q" :
                        print("再见")
                        break
            else:
                print("没有相关地区")
                break
        break
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
        ["奔驰", 250, "W"],
        ["奥迪", 110, "W"],
        ["兰博基尼", 500, "W"],
        ["volvo", 80, "W"],
        ["雷克萨斯", 90, "W"],
        ["凯迪拉克", 20, "W"]
    ]
    mycart = []
    money = int(input("请输入您带的钱："))
    while True:
        for j, s in enumerate(cart):
            print("剩余车型：", j, s)
        h = input("选择购车编号：")
        if h.isdigit():
            num = int(h)
            if num > len(cart):
                print("您选择的商品不存在")
            if money < cart[num][1]:
                print("可惜，钱不够")
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
    else:
        print("没有该业务")
    break