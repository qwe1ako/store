fruits={
    "苹果": 32.8,
    "香蕉":22,
    "葡萄":15.5
}
info = {
    '小明': {
        'fruits': {'苹果':4, '草莓':13, '香蕉':10},
        'money': 0
    },
    '小刚': {
        'fruits': {'葡萄':19, '橘子':12, '樱桃':30},
        'money': 0
    },
}
# def print_fruits(can):
#     for i in can:
#         print(i,"\t")
# c1=input("输入选择的水果：")
# c2=info
# while True:
#     if c1 in fruits:
#         print(c1,"为",fruits[c1],"元")
#         break
#     else:
#         print("该商品没有上架")
#         break
# while True:
#     if c2 in info:
#         print(info[c2][c2])
# key1是两个人购买的水果名称
# key2是水果店中水果的名称
# 判断
# 判断为真时，去改变money值。 money = 原money + 水果购买量 * 对应水果的单价
for key in info:
    for key1 in info[key]["fruits"]:
        for key2 in fruits:
             if key1==key2:
                 info[key]["money"]=info[key].get("money")+info[key]["fruits"].get(key1)*fruits.get(key2)
for key3 in info:
    for key4 in info :
        i=info[key3].get("money")+info[key4].get("money")
        break
print(info)
print("一共花了￥",i,)

