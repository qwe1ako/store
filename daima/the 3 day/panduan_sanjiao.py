a=input("请输入一个数字：")
b=input("请输入第二个数字:")
c=input("请输入第三个数字:")
a=int(a)
b=int(b)
c=int(c)

if a*a+b*b==c*c or a*a+c*c==b*b or c*c+b*b==a*a:
    print("构成了直角三角形")
elif a==b==c :
    print("构成等边三角形")
elif a==b or b==c or c==a:
    print("构成等腰三角形")
elif a+b>c and a+c>b and c+b>a:
    print("构成普通三角形")
elif  a+b<c or a+b<c or a+c<b:
    print("构不成三角形")


