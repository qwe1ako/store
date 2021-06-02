students = [
    {'name': '张三', 'age': 23, 'score': 88, 'tel': '23423532', 'gender': '男'},
    {'name': '李四', 'age': 26, 'score': 80, 'tel': '12533453', 'gender': '女'},
    {'name': '王五', 'age': 15, 'score': 58, 'tel': '56453453', 'gender': '男'},
    {'name': '赵六', 'age': 16, 'score': 90, 'tel': '86786785', 'gender': '保密'},
    {'name': '小明', 'age': 18, 'score': 98, 'tel': '23434659', 'gender': '女'},
    {'name': '小红', 'age': 23, 'score': 72, 'tel': '67867868', 'gender': '女'},
]
# 1) 统计不及格学生的个数
# 2) b.打印不及格学生的名字和对应的成绩
# 3) 统计未成年学生的个数
# 4) 打印手机尾号是8的学生的名字
# 5) 打印最高分和对应的学生的名字

count = 0
countt = 0
a = 0
max = 0
xh = 0
tt = "保密"
aa = []
for key in students:
    if key.get("score") < 60:
        count = count + 1
    if key.get("age") < 18:
        countt = countt + 1
        print("不及格人为", key["name"], key.get("score"), "未成年有：", key["name"], key.get("age"))
print("不及格的人数有", count, "人")
print("未成年有：", countt, "人")
for key1 in students:
    a = int(key1.get("tel")) % 10
    if a == 8:
        print("tel尾数为8的是", key1["name"], )
for key3 in students:
    for key2 in students:
        if key2.get("score") > max:
            max = key2.get("score")
    if key3.get("score") == max:
        print("最高成绩是", key3["name"], "分数", max)
# 6) 将列表按学生成绩从大到小排序
# 将学生成绩放到list，对list排序，再放回去
while xh < len(students):
    xhh = xh + 1
    while xhh < len(students):
        if int(students[xh]["score"]) > int((students[xhh]["score"])):
            aa = students[xhh]
            students[xhh] = students[xh]
            students[xh] = aa
        xhh = xhh + 1
    xh = xh + 1
print(students)
#删除性别为“保密”的
for jj, ss in enumerate(students):
    if ss["gender"] == tt:
        del students[jj]
print(students)
