#!/usr/bin/env python
#-*- coding:utf8 -*-
import threading
import time

'''
#直接调用
def Princ(String):
    print('task', String)
    time.sleep(5)
# target=目标函数， args=传入的参数
for i in range(3):
    t1 = threading.Thread(target=Princ, args=(i,))
    t1.start()
'''

# t1 = threading.Thread(target=Princ, args=('t1',))
# t1.start()
# t2 = threading.Thread(target=Princ, args=('t1',))
# t2.start()
# t3 = threading.Thread(target=Princ, args=('t1',))
# t3.start()


'''
#通过类调用
import threading
import time
class MyThreading(threading.Thread):
    def __init__(self, conn):
        super(MyThreading, self).__init__()
        self.conn = conn
    def run(self):
        print('run task', self.conn)
        time.sleep(5)
t1 = MyThreading('t1')
t2 = MyThreading('t2')
t1.start()
t2.start()
'''



import threading
import time
#join()方法可以让程序等待每一个线程之后完成再往下执行，称为串行执行
def Princ(String):
    print('task', String)
    time.sleep(1)
for i in range(10):
    t = threading.Thread(target=Princ, args=('t-%s' % (i),))
    t.start()
    # 当前线程执行完毕之后在执行后面的线程
    t.join()
