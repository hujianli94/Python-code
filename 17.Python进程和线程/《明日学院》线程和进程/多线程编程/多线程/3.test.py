#!/usr/bin/env python
#-*- coding:utf8 -*-
import threading
import time

'''
def Princ(String):
    print("task",String)
    time.sleep(2)

#执行子进程的时间
start_time = time.time()

#存放线程的实例
t_object = []
for i in range(30):
    t = threading.Thread(target=Princ,args=('t-%s' %(i),))
    t.start()

    #将当前的子线程放到一个列表中
    t_object.append(t)

for t in t_object:
    t.join()

#统计所耗时间
print(time.time() - start_time)

'''


import threading
class MyThreading(threading.Thread):
    def __init__(self):
        super(MyThreading, self).__init__()
    def run(self):
        print('我是子线程： ', threading.current_thread())
t = MyThreading()
t.start()
print('我是主线程： ', threading.current_thread())
