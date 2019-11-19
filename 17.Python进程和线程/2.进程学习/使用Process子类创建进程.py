#!/usr/bin/env python
#-*- coding:utf8 -*-
from multiprocessing import Process
import time
import os

class SubProcess(Process):
    '''
    docstring for SubProcess
    '''
    def __init__(self,interval,name=''):
        super(SubProcess, self).__init__()
        self.interval = interval
        if name:
            self.name = name

    def run(self):
        '''
        进程运行时执行的方法
        :return:
        '''
        print('子进程（%s）开始执行，它的父进程是(%s) ' % (os.getpid(), os.getppid()))
        t_start = time.time()
        time.sleep(self.interval)
        t_end = time.time()
        print("子进程（%s）执行时间为%0.2f 秒" % (os.getppid(), t_end - t_start))

if __name__ == '__main__':
    print("主进程开始")
    print("主进程的PID：%s" % os.getpid())
    p1 = SubProcess(interval=1,name="mrsoft")
    p2 = SubProcess(interval=2)
    p1.start()                  #当调用start方法时会默认执行run方法
    p2.start()
    print('p1.is_alive=%s' % p1.is_alive())
    print('p2.is_alive=%s' % p2.is_alive())
    print('p1.name=%s'% p1.name)
    print('p1.id=%s' % p1.pid)
    print('p2.name=%s'% p2.name)
    print('p2.id=%s' % p2.pid)
    p1.join()
    p2.join()