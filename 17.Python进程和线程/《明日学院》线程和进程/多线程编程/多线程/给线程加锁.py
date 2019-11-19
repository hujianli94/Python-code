#!/usr/bin/env python
#-*- coding:utf8 -*-
"""
使用互斥锁
"""
from threading import Thread,Lock
import time

n = 100
def task():
    global n
    mutex.acquire()         #锁定
    time.sleep(0.5)
    n -=1
    print('购买成功，剩余{}电影票'.format(n))
    mutex.release()         #释放锁

if __name__ == '__main__':
    mutex = Lock()          #定义锁
    t_1 = []
    for i in range(10):
        t = Thread(target=task)
        t_1.append(t)
        t.start()
    for t in t_1:
        t.join()