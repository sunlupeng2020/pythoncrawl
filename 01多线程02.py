import threading
import time

class CodingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print('%d正在写代码...' % x)
            time.sleep(1)


class DrawingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print('%d正在画图...' % x)
            time.sleep(1)


def multi_thread():
    coding=CodingThread()
    drawing=DrawingThread()
    coding.start()
    drawing.start()


if __name__ == '__main__':
    multi_thread()