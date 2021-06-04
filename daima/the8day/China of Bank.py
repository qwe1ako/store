import random

# 银行的库


names = {
    "account": {"address": "沙河北大桥桥底下", "money": 500, "password": "112233"},
    "account1":{"address":"沙河北大桥桥底下", "money": 500, "password1": "112233"}
}
# 开户行名称
bank_name = "中国工商银行昌平支行"
# 欢迎页面的模板
welcome = '''
    -----------------------------------------
    -     欢迎来到中国工商银行账户管理系统     -
    -----------------------------------------
    -   1.开户                               -
    -   2.存钱                               -
    -   3.取钱                               -
    -   4.转账                               -
    -   5.查询                               -
    -   6.Bye!                               -
    ------------------------------------------
'''


def getRandom():
    li = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f"]
    string = ""
    for i in range(8):
        ch = li[random.randint(0, len(li) - 1)]
        string = string + ch
    return string


# 银行的开户逻辑
def bank_addUser(account, username, password, money, country, province, street, door):
    # 1.判断是否已满
    if len(names) >= 100:
        return 3
    # 2.判断是否存在:依据是用户名
    if username in names:
        return 2
    # 3.开户
    names[username] = {
        "account": account,
        "username": username,
        "password": password,
        "money": money,
        "country": country,
        "province": province,
        "street": street,
        "door": door,
        "bank_name": bank_name
    }
    return 1
# 开户操作
def addUser():
    username = input("请输入您的姓名：")
    password = input("请输入你的密码：")
    money = int(input("请输入您的账户余额："))  # "123"  123
    print("下面请输入您的个人地址信息：")
    country = input("请输入您的国籍：")
    province = input("请输入您的省份：")
    street = input("请输入您的居住街道：")
    door = input("请输入您的门牌号：")
    account = getRandom()
    status = bank_addUser(account, username, password, money, country, province, street, door)
    if status == 1:
        print("恭喜开户成功！以下是您的个人信息：")
        info = '''
            ----------个人信息 【工商银行】--------
            用户名：%s,
            密码：%s,
            账号：%s,
            余额：%s,
            国家：%s,
            省份：%s,
            街道:%s,
            门牌号：%s
            开户行名称：%s
            ------------------------------------
        '''
        print(info % (username, password, account, money, country, province, street, door, bank_name))

    elif status == 2:
        print("对不起，您的账户已存在！请勿重复开户！")
    elif status == 3:
        print("对不起，用户库已满，请携带证件到其他银行办理！")
# 存钱方法
def savemoney():
    account = input("请输入您要存款的账号：")
    password = input("请输入存款账号的密码：")
    money = int(input("请输入您要存的金额："))
    a = bank_savemoney(account, password, money)
    if a == False:
        print("账号或密码输入错误")
    else:
        print("存入成功", "本次存入：￥", money, "\t存钱账号为", account, "账号剩余：￥", names[account].get("money"))
# 存钱逻辑
def bank_savemoney(account, password, money):
    if account in names.keys() and names[account].get("password") == password:
        names[account]["money"] = names[account].get("money") + money
    else:
        return False
# 取钱逻辑
def back_gomoney(account, password, money):
    if account in names.keys():
        if password in names["account"]["password"]:
            if money <= names["account"].get("money"):
                names["account"]["money"] = names["account"].get("money") - money
            else:
                return 3
        else:
            return 2
    else:
        return 1
# 取钱方法
def gomoney():
    account = input("请输入账号：")
    password = input("请输入密码：")
    money = int(input("请输入存款钱数："))
    a = back_gomoney(account, password, money)
    if a == 1:
        print("账号错误")
    if a == 2:
        print("密码错误")
    if a == 3:
        print("余额不足")
    else:
        print("存钱成功，余额为", names["account"]["money"])
#转账逻辑
def back_rotatemoney(account1,account,password,money):
    if account in names.keys():
        if account1 in names.keys():
            if password in names[account]["password"]:
                   if names[account]["money"] < money:
                      return 3
                   else:
                       names[account1]["money"] = names[account].get("money")+money
                       names[account]["money"] = names[account].get("money")-money
                       return 0
            else:
                return 2
        else:
            return 1
#转账方法
def rotatemoney():
    account=input("请输入转出账户：")
    password=input("请输入转出账户密码：")
    account1=input("请输入转入账户：")
    password=input("请输入转入账户密码：")
    money=int(input("请输入金额￥："))
    b=back_rotatemoney(account1,account,password,money,)
    if b==3:
        print("账户余额不足")
    if b==2:
        print("密码不正确")
    if b== 1:
        print("账户不存在")
    else :
        print("转账成功，转出",money,"s剩余：","剩余",names[account].get("money"),"转入账号",account1,names[account1].get("money"))
#查询账户逻辑
def back_inquire(account,password):
    if account in names.keys():
        if password == names[account].get("password"):
                return 1
        else:
            return 2
    else:
        return 3
#查询信息方法
def inquire():
    account=input("请输入账号：")
    password=input("请输入密码：")
    c=back_inquire(account,password)
    if c == 3:
        print("账号输入错误")
    if c == 2:
        print("密码输入错误")
    if c== 1:
        print("以下是账号信息：",)
        info='''
        ===========================
        account:%s
        address:%s
        money:%s
        password:%s
        ===========================
        '''
        print(info %(account,names[account]["address"],names[account]["money"],names[account]["password"]))



# 入口
while True:
    print(welcome)
    chose = input("请输入您的业务编号：")
    if chose == '1':
        addUser()
    elif chose == '2':
        savemoney()
    elif chose == '3':
        gomoney()
    elif chose == '4':
        rotatemoney()
    elif chose == '5':
        inquire()
    elif chose == '6':
        print("再见！")
        break
    else:
        print("输入非法！别瞎弄！")
