#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
操作系统能够进行运算调度的最小单位，它被包含在进程之中，是进程中的时间运作单位
'''

'''
线程在电脑中是怎么运行的？
线程1         线程2         线程3     线程4

线程的特点：
1.进程是资源分配的最小单位，线程是最小的执行单位
2.一个进程可以有多个线程
3.线程共享进程资源
'''



"""
from multiprocessing import Process,Queue
import os
import time
import random

#写数据进程执行的代码
def write(q):
    print("Process to write :%s " % os.getpid())
    for value in ['A','B','C']:
        print("Put %s to queue..." % value)
        q.put(value)
        time.sleep(random.random())

# 读数据执行的代码
def read(q):
    print("Process to read:%s" % os.getpid())
    while True:
        value = q.get(True)
        print("Get %s from queue." % value)

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()      # 强制终止进程pr
"""






