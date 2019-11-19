#!/usr/bin/env python
#-*- coding:utf8 -*-
import multiprocessing
import time


#设置p.daemon=True后，主进程不等待子进程，直接结束。
def work(i):
    print('work start{0}'.format(time.ctime()))
    time.sleep(1)
    print("work end{0}".format(time.ctime()))

if __name__ == '__main__':
    p = multiprocessing.Process(target=work,args=(2,))
    p.daemon=True
    p.start()
    p.join()            #添加join()之后就等待子进程输出完毕后再输出主进程
    print("-------------end-------------------")


