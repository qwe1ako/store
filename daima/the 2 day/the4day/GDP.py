a=["北京","上海","广东","深圳"]
a.extend(["太原","西安","成都","武汉","南京","贵阳","石家庄","郑州"])
print(a)
b=["北京","上海","广东","深圳"]
b[2]="上海"
b[1]="广东"
print(b)
a=0
b=[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
count=0
sum=0
while count<8:
    sum=sum+b[count]
    count=count+1
    pin=sum/8
print("GDP总和：",sum,"平均GDP",pin)