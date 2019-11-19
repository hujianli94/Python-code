#!/usr/bin/env python
#-*- coding:utf8 -*-
from multiprocessing import Process

g_num = 100

def plus():
    print("-----子进程1开始-----")
    global g_num
    g_num += 50
    print("g_num is %d " % g_num)
    print("------子进程1结束-----")

def minus():
    print("-----子进程2开始-----")
    global g_num
    g_num -= 50
    print("g_num is %d " % g_num)
    print("------子进程2结束-----")




if __name__ == '__main__':
    print("---主进程开始------")
    p1 = Process(target=plus) 
    p2 = Process(target=minus) 
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("----主进程结束------")


