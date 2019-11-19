#!/usr/bin/env python
#-*- coding:utf8 -*-
# import threading,time
# import queue
#
# q = queue.Queue(maxsize=5)       #设置maxsize=5，防止生产过快
#
# def Producer(name):    #生产者
#     count = 1
#     while True:
#         q.put("面包%s" % count)
#         print("%s生产了面包%s"%(name,count))
#         count +=1
#         time.sleep(1)
#
# def Consumer(name):         #消费者
#     while True:
#         print("[%s] 取到[%s] 并且吃了它..." %(name, q.get()))
#         time.sleep(1)
#
# #生成多个线程
# p = threading.Thread(target=Producer,args=("derek",))
# c = threading.Thread(target=Consumer,args=("chihuo1",))
# c1 = threading.Thread(target=Consumer,args=("chihou2",))
#
# p.start()
# c.start()
# c1.start()



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
            print("生产者{} 将产品{}加入队列".format(self.getName(), i))
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
            print("消费者{} 将产品{}从队列中取出".format(self.getName(), val))
            time.sleep(random.random())

        print("消费者{}完成！".format(self.getName()))

if __name__ == '__main__':
    print("主线程开始".center(50, "-"))
    queue = Queue()
    producer = Producer('Producer', queue)
    consumer = Consumer('Consumer', queue)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
    print("主线程结束".center(50, "-"))