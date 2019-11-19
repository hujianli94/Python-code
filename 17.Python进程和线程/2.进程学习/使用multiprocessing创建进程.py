#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
创建进程
1.os.fork()03.函数               #不支持windows系统
2.multiprocessing模块Process类
3.Process类的子类
4.Pool进程池
'''
from multiprocessing import Process
import time
import os

def child_1(intervel):
    print('子进程（%s）开始执行，它的父进程是(%s) ' % (os.getpid(), os.getppid()))
    t_start = time.time()
    time.sleep(intervel)
    t_end = time.time()
    print("子进程（%s）执行时间为%0.2f 秒" % (os.getppid(), t_end - t_start))

def child_2(intervel):
    print('子进程（%s）开始执行，它的父进程是(%s) '%(os.getpid(), os.getppid()))
    t_start=time.time()
    time.sleep(intervel)
    t_end = time.time()
    print("子进程（%s）执行时间为%0.2f 秒" % (os.getppid(), t_end - t_start))


def main():
    print('主进程开始')
    print("主进程的PID （%s）" % os.getpid())
    p1 = Process(target=child_1, args=(1,))
    p2 = Process(target=child_2, name='mrsoft',args=(2,))
    p1.start()
    p2.start()
    print('p1.is_alive=%s' % p1.is_alive())
    print('p2.is_alive=%s' % p2.is_alive())
    print('p1.name=%s'% p1.name)
    print('p1.id=%s' % p1.pid)
    print('p2.name=%s'% p2.name)
    print('p2.id=%s' % p2.pid)
    p1.join()
    p2.join()

    print("主进程结束")

if __name__ == '__main__':
    main()