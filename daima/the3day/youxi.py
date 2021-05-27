number=input("请输入一个分数吧：")
number=int(number)
if number >= 90 and number <= 100:
    print("优秀!excellent")
elif number >= 80 and number < 90:
    print("很好 good ")
elif number >=70 and number <80:
    print("一般般 just so so ")
elif number >=60 and number < 70:
  print("差点！！！")
elif number >= 0 and number <60:
    print ("可惜！！ ")
else:
    print("看仔细输入")