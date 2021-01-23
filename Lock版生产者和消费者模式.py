import threading
import random
import time

gMoney=0
gLock=threading.Lock()
gTimes =0


#生产者类
class Producer(threading.Thread):
    def run(self)->None:
        global gMoney
        global gTimes
        while True:
            gLock.acquire() #获得锁
            if gTimes>=10:
                gLock.release()  #释放锁
                break
            money=random.randint(0,100)
            gMoney+=money
            gTimes+=1
            print("%s生产了%d元钱"%(threading.current_thread().name,money))
            gLock.release()


class Consumer(threading.Thread):
    def run(self)->None:
        global gMoney
        while True:
            gLock.acquire()
            money=random.randint(0,100)
            if gMoney>=money:
                gMoney-=money
                print("%s消费了%d元钱"%(threading.current_thread().name,money))
            else:
                if gTimes >= 10:
                    gLock.release()
                    break
                print("%s想消费%d元钱，但是余额只有%d"%(threading.current_thread().name,money,gMoney))
            gLock.release()

def main():
    for x in range(5):
        th1=Producer(name="生产者%d号"%x)
        th1.start()
        time.sleep(1)

    for x in range(5):
        th2=Consumer(name="消费者%d号"%x)
        th2.start()
        time.sleep(1)

if __name__ == "__main__":
    main()

