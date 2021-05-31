'''
排序
'''
'''
当前角标与之后对比
角标每次+1
<角标往前
>角标的往后
'''
list = [100, 70, 80, 60, 85, 40, 5]
count = 0

while count < 6:
    ii=count+1
    while ii< len (list):
        if int(list[count])>int(list[ii]):
            list[count]=list[ii]+list[count]
            list[ii] = list[count]-list[ii]
            list[count] = list[count] - list[ii]
        ii=ii+1
    count = count + 1


print(list)
