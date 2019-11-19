#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/17 17:14
# filename: 调用Thread类创建多线程.py
import threading

def action(max):
    for i in range(max):
        print(threading.current_thread().getName() + " " + str(i))

for i in range(100):
    print(threading.current_thread().getName() + " " + str(i))

    if i == 20:
        #创建并启动第一个线程
        t1 = threading.Thread(target=action, args=(10, ))
        t1.start()

        #创建并启动第二个线程
        t2 = threading.Thread(target=action, args=(10,))
        t2.start()
print("主线程执行完成！！")