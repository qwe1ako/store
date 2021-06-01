import random
a=['bb','jj','hh','yy','nn']
while True :

    if len(a)==0:
        print("删完了")
        break
    print("请选择业务","1.选人2.处罚")
    p=input("请输入编号")
    if p=="1":
        b=random.randint(0,len(a)-1)
        print(a[b],"已移除")
        a.remove(a[b])
        print("现在名单为",a)
    elif p=="2":
        c=random.randint(0,200)
        print(c)
    elif (p)=="Q" or p=="q" :
        break
        print('baibai')
    else:
        print("没有此业务")

