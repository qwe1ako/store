#井深20m，白天爬3，晚上滑2，几天出来
j=20
s=0
day=0
while True:
    if s<j-3:
        s=s+3-2
    else :
       day=day+1
       break
    day=day+1
print("它用了",day,"天")






