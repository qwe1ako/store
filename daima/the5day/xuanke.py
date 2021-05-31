'''
用三个列表表示三门学科的选课学生姓名(一个学生可以同时选多门课)
语文 = ['小明','小张','小黄','小杨']
数学 = ['小黄','小李','小王','小杨','小周']
英语 = ['小杨','小张','小吴','小冯','小周']
1) 求选课学生总共有多少人
把123，放进a里
'''

# a= ['小明','小张','小黄','小杨']
# b = ['小黄','小李','小王','小杨','小周']
# c = ['小杨','小张','小吴','小冯','小周']
# e=[]
# y=0
# for o in a:
#     e.append(o)
# for i in  b:
#     e.append(i)
# for u in c:
#     e.append(u)
# for j,s in enumerate(e):
#     if s in e[:j]:
#         continue
#     else:
#         y=y+1
#         print("选课人员：",s)
# print("总共有",y,"人")




# 求只选了第一个学科的人的数量和对应的名字
'''
a= ['小明','小张','小黄','小杨']
b = ['小黄','小李','小王','小杨','小周']
c = ['小杨','小张','小吴','小冯','小周']
e=[]
for o in a:
    e.append(o)
number=len(e)
print("选了语文的人为：",e,"人数为：",number,"人")
'''
#3) 求只选了一门学科的学生的数量和对应的名字
#所有人融合 排除重复的
'''
a= ['小明','小张','小黄','小杨']
b = ['小黄','小李','小王','小杨','小周']
c = ['小杨','小张','小吴','小冯','小周']
e=[]
j=0
for o in a:
    e.append(o)
for i in b:
    e.append(i)
for u in c:
    e.append(u)
for u,v in enumerate(e):
    if v in e[:u]:
        continue
    else:
        if e.count(v)==1:
            j=j+1
            print("只选了一门课程的人：",v)
print("一共有",j,'人')
'''

# 4) 求只选了语文和英语的学生的数量和对应的名字
#a和c对比
#重复的拿出来
#拿出来的数据对比b
#没重复的 count+1
a= ['小明','小张','小黄','小杨']
b = ['小黄','小李','小王','小杨','小周',]
c = ['小杨','小张','小吴','小冯','小周',]
y=0

for o in a:#循环a里数据
    for i in c :
        if o==i:#a和c【】的对比
             if o not in b:#o不在b里
                print("只选了语文和数学的人：",o,)
                y=y+1
print("一共",y,"人")













# a= ['小明','小张','小黄','小杨']
# b = ['小黄','小李','小王','小杨','小周']
# c = ['小杨','小张','小吴','小冯','小周']
# i=[]
# u=[]
# j=0
# for y in a:
#     i.append(y)
# for p in c:
#     i.append(p)
# for u,v in enumerate(i):
#     if v in i[:u]:
#         continue
#     else:
#         if i.count(v)==1:
#             j=j+1
#             print(v)
# print("一共有",j,'人')



