#10个数的和、平均数、最大数
max=0
i=0 #次数#
sum=0#和
while i<=9:
    c=int(input("请输入一次数字"))
    i=i+1
    sum=sum+c
    pin=sum/10
    if c>max :
        max=c
print ("最大为",max,"十个数相加为",sum,"是个数的平均数为",pin,)
#调换
'''a=56
b=78
print("a=",(b+a-a))
print("b=",(a+b-b))'''
#随机产生
'''import random
num = int(random.randint(50,150))
print("生成:", num)'''

