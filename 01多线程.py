import threading
import time

def coding():
    the_thread = threading.current_thread()
    for x in range(3):
        print('%s正在写代码...' % the_thread.name)
        time.sleep(1)
def drawing():
    the_thread = threading.current_thread()
    for x in range(3):
        print('%s正在画图...' % the_thread.name)
        time.sleep(1)
def multi_thread():
    th1=threading.Thread(target=coding, name='小明')
    th2=threading.Thread(target=drawing, name='小红')

    th1.start()
    th2.start()


if __name__ == '__main__':
    multi_thread()