#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
线程中的数据是可以共享的
'''

from threading import Thread

g_num = 100

def plus():
    print("-----子线程1开始-----")
    global g_num
    g_num += 50
    print("g_num is %d " % g_num)
    print("------子线程1结束-----")

def minus():
    print("-----子线程2开始-----")
    global g_num
    g_num -= 50
    print("g_num is %d " % g_num)
    print("------子线程2结束-----")




if __name__ == '__main__':
    print("---子线程开始------")
    p1 = Thread(target=plus)
    p2 = Thread(target=minus)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("----子线程结束------")



