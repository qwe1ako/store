e=0
while True:
 a = int(input("输入一个0~100的数:"))
 if 0<=a<=100:
  e=e+a
  print("累计为：",e)
 if a > 100:
   print("输入错误")
   break





