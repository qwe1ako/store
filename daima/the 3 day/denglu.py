name="root"
password="admin"
count=3
while  count>0 :
    count=count-1
    a=input("请输入密码:")
    if a == password:
        print("密码正确")
        break
    elif a!=password:
        print("密码输入错误还有",count,"次机会")
if count==0:
    print("错误3次，账号已被锁")



