#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/17 17:23
# filename: 3.继承Thread类创建多线程.py
import threading
class FkThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.i = 0

    # 重写run()方法作为线程执行体
    def run(self):
        while self.i < 100:
            print(threading.current_thread().getName() + " " + str(self.i))
            self.i +=1


for i in range(100):
    print(threading.current_thread().getName() + " " + str(i))
    if i == 20:
        # 启动第一个线程
        ft1 = FkThread()
        ft1.start()

        # 启动第二个线程
        ft2 = FkThread()
        ft2.start()