
'''
用 第一位 角标比较后面，相同的并计数.
循环15次结束

'''
import random
list = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
count=0
cs=0
i=0
ii=1
z=0
x=0
listt=[]
listtt=[]
while count < 15 :
    cs=0
    countt=0
    while countt < 15:
        if list[count] == list[countt]:
            cs=cs+1
        countt = countt + 1
    if list[count] not in listt:
        listt.append(list[count])
        listtt.append(cs)
    count = count + 1
print(listt)
print(listtt)
while True:
    if x==len(listt):
        break
    l=listt[x]
    m=listtt[x]
    x=x+1
    print(l,"出现了",m)



