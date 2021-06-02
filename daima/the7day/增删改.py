dict = {"k1":"v1","k2":"v2","k3":"v3"}
#1、请循环遍历出所有的key
#2、请循环遍历出所有的value
# 3、请在字典中增加一个键值对,"k4":"v4"
keys=dict.keys()
values=dict.values()
for key in keys:
    print(keys)
    break
for value in values:
    print(values)
    break
dict["k4"]="v4"
del dict["k1"]
dict["k2"]="gai"
print(dict)


