#!/usr/bin/env python
#-*- coding:utf8 -*-
import threading
import time
class myTread(threading.Thread):
    def run(self):
        global x
        lock.acquire()
        for i in range(2):
            x +=10
        time.sleep(1)
        print(x)
        lock.release()
x = 0
lock = threading.RLock()
def main():
    thrs = []
    for item in range(5):
        thrs.append(myTread())
    for item in thrs:
        item.start()
if __name__ == '__main__':
    main()


"""
自定义一个带锁访问全局变量x的线程类myThread，在main()函数中初始化了5个线程来修改变量x，
但同一时刻只能由一个线程对x操作
"""