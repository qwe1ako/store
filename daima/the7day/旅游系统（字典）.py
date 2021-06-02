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

