import threading

value = 0
gLock=threading.Lock()

def add_value():
    global value
    gLock.acquire()
    for x in range(1000000):
        value+=1
    gLock.release()
    print("value is %d" % value)

def main():
    th1=threading.Thread(target=add_value)
    th2=threading.Thread(target=add_value)
    th1.start()
    th2.start()


if __name__ == '__main__':
    main()