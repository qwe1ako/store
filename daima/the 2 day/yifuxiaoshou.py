date=('1号','2号','3号','4号','5号','6号','7号')
name=('羽绒服','牛仔裤','风衣','皮草','T恤','衬衫','牛仔裤')
price=(253.6,86.3,96.8,135.9,65.8,49.3,86.3)
repertory=(500,600,335,855,632,562,600)
sell_number=(10,60,43,63,63,120,72)
print('---------------------衣服商城销售报表-----------------')
print('-------------------------------------------------------')
print('日期 名称      价格      库存/件    销售量/天')
print(date[0],'',price[0],'  ',price[0],'    ',repertory[0],'      ',sell_number[0],'')
print(date[1],'',price[1],'  ',price[1],'    ',repertory[1],'      ',sell_number[1],'')
print(date[2],'',price[2],'  ',price[2],'    ',repertory[2],'      ',sell_number[2],'')
print(date[3],'',price[3],'  ',price[3],'    ',repertory[3],'      ',sell_number[3],'')
print(date[4],'',price[4],'  ',price[4],'    ',repertory[4],'      ',sell_number[4],'')
print(date[5],'',price[5],'  ',price[5],'    ',repertory[5],'      ',sell_number[5],'')
print('-----------------------------------------------------------')
'总销售额'
C=359
print('总销售数量:￥',(sell_number[0]+sell_number[1]+sell_number[2]+sell_number[3]+sell_number[4]+sell_number[5]))
print('总销售额:￥',(price[0]+price[1]+price[2]+price[3]+price[4]+price[5]))
print('每种衣服销售占比:￥',(C/(sell_number[0]+sell_number[1]+sell_number[2]+sell_number[3]+sell_number[4]+sell_number[5])),'%')

A=56
B=78
print('A=',(A+B-A))
print('B=',(A+B-B))