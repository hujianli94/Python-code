#!/usr/bin/env python
#-*- coding:utf8 -*-
import threading,time

class Consumer(threading.Thread):
    def __init__(self,cond,name):
        #初始化
        super(Consumer,self).__init__()
        self.cond = cond
        self.name = name

    def run(self):
        #确保先运行Seeker中的方法
        time.sleep(1)
        self.cond.acquire()
        print(self.name + ':我这两件商品一起买可否便宜一点?')
        self.cond.notify()
        self.cond.wait()
        time.sleep(1)
        print(self.name + ": 我已经提交订单了，你修改下价格")
        self.cond.notify()
        self.cond.wait()
        time.sleep(1)
        print(self.name + "：收到，我支付成功了")
        self.cond.notify()
        self.cond.release()
        time.sleep(1)
        print( self.name + ":等待收货")

class Producer(threading.Thread):
    def __init__(self, cond, name):
        super(Producer, self).__init__()
        self.cond = cond
        self.name = name

    def run(self):
        self.cond.acquire()
        # 释放对琐的占用，同时线程挂起在这里，直到被 notify 并重新占有琐。
        self.cond.wait()
        time.sleep(1)
        print(self.name + ': 可以的，你提交订单吧')
        self.cond.notify()
        self.cond.wait()
        time.sleep(1)
        print(self.name + ': 好了，已经修改了')
        self.cond.notify()
        self.cond.wait()
        time.sleep(1)
        print(self.name + ': 嗯，收款成功，马上给你发货')
        self.cond.release()
        time.sleep(1)
        print(self.name + ': 发货商品')


cond = threading.Condition()
consumer = Consumer(cond, '买家（小健）')
producer = Producer(cond, '卖家（高圆圆）')
consumer.start()
producer.start()