# 编写一个函数，传入一个列表，并统计每个数字出现的次数。返回字典数据：{21:3,56:3,10:3}
# 将a数组枚举遍历
# 判断数字出现的次数
 # 已经在字典中有记录的数据计数加一
 # 没有在字典中存在记录的情况下，将出现的数字添加到字典中，此时计数为1

a=[21,21,21,56,56,56,10,10,10]

def num_count(list) :
    c={}
    for index,value in enumerate(a):
        if value in list[:index]:
            c[value]=c.get(value)+1
        else:
            c[value]=1
    return c
c=num_count(a)
print(c)