import threading
import time
ticket=300
class Person(threading.Thread):
    username=""
    count=0
    def run(self) -> None:
        global ticket
        while True:
            if ticket >0:
                ticket=ticket-1
                self.count=self.count+1
                time.sleep(0.5)
                print(self.username,"成功抢了1张票")
            else:
                print(self.username,"已近抢了",self.count,"张票")
                break
p=Person()
p.username="李"
pp=Person()
pp.username="张"
ppp=Person()
ppp.username="邢"

p.start()
pp.start()
ppp.start()