#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/17 10:41
# filename: 多进程，进程池的使用.py
from multiprocessing import Pool
import os, time, random


def run_task(name):
    print("Task {0} (pid={1}) is running ....".format(name, os.getpid()))
    time.sleep(random.random() * 3)
    print("Task {} end.".format(name))


if __name__ == '__main__':
    print("Current process {}".format(os.getpid()))
    p = Pool(processes=3)
    for i in range(5):
        p.apply_async(run_task, args=(i,))
    print("Waiting for all subprocess done....")
    p.close()
    p.join()
    print("All subprocess done.!!")
