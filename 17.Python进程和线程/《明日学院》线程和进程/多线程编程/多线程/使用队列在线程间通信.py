#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
生产者和消费者的模式
使用队列模拟生产者和消费者模式
'''

from queue import Queue
from threading import Thread
import time
import random

class Producer(Thread):
    def __init__(self, name, queue):
        Thread.__init__(self, name=name)
        self.data = queue

    def run(self):
        for i in range(5):
            print("生产者{}将产品{}加入队列".format(self.getName(), i))
            self.data.put(i)
            time.sleep(random.random())
        print("生产者{}完成！".format(self.getName()))

class Consumer(Thread):
    def __init__(self, name, queue):
        Thread.__init__(self, name=name)
        self.data = queue

    def run(self):
        for i in range(5):
            val = self.data.get()
            print("消费者{}将产品{}从队列中取出".format(self.getName(), val))
            time.sleep(random.random())
        print("消费者{}完成！".format(self.getName()))



if __name__ == '__main__':
    print('---------主线程开始------------')
    queue = Queue()
    producer = Producer('Producer', queue)
    consumer = Consumer('Consumer', queue)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
    print("----------主线程结束---------------")