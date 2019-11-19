#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/17 10:50
# filename: 多进程01.py
from multiprocessing import Process
import os


def run_task(name):
    print("Child process {} 【{}】 Running ....".format(name, os.getpid()))


if __name__ == '__main__':
    print("Parent process 【{}】".format(os.getpid()))
    for i in range(5):
        p = Process(target=run_task, args=(i,))
        print("Process will be Start.....")
        p.start()
    p.join()        #等待子进程结束
    print("Process end.")