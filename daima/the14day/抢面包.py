import threading
import time
bread=10

class Rob(threading.Thread):
    name=""
    count=0
    money=0
    def run(self) -> None:
        global bread
        while True:
            if self.money < 3 or bread == 0:
                print("余额不足,或面包不够")
                break
            elif bread > 0:
                bread = bread -1
                self.count=self.count+1
                self.money=self.money-3
                time.sleep(10)
                print(self.name,"已抢了","1个面包","花了",3,"元")
            else:
                print(self.name,"已抢了",self.count,"个面包")
class Maker(threading.Thread):
    name=""
    countt=0
    def run(self) -> None:
        global bread
        while True:
            if bread < 30:
                bread = bread +1
                self.countt=self.countt+1
                time.sleep(1)
                print(self.name,"造了1个面包",)
            else:
                print(self.name,"一共造了",self.countt)
                break


p=Rob()
p.name="李闻虎"
p.money=30
pp=Rob()
pp.name="李文虎"
pp.money=30
ppp=Rob()
ppp.name="李吻虎"
ppp.money=30
pp.start()
p.start()
ppp.start()

a=Maker()
a.name="李"
aa=Maker()
aa.name="文"
aaa=Maker()
aaa.name='虎'
aaa.start()
aa.start()
a.start()