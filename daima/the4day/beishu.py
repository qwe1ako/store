5的倍数和
a = [1,5,21,30,15,9,30,24]
b=0
c=0
while b < 8:#运行8次
    if a[b]%5==0:#每个/5
        c=c+a[b]   #能/5的相加
    b=b+1#每次运行加1
print("5的倍数的和=",c)

'''翻转列表
list = [1,2,3,4,5,6,7,8,9]
list.reverse()
print("反转后list=",list)
'''
'''
num=int(input("请输入一个数:"))
while num !=0:

    print(num%10)#num/10后，保留小数点的数
    num=num//10#num/10后，去掉小数点的数
'''




