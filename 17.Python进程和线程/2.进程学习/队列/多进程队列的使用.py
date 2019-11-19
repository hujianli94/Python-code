#!/usr/bin/env python
#-*- coding:utf8 -*-
from multiprocessing import Queue
#Queue类的常用方法

if __name__ == '__main__':
    q = Queue(3)
    q.put("消息1")
    q.put("消息2")
    print("队列是否已满: %s" % q.full())

    q.put("消息3")
    print("队列是否已满: %s" % q.full())
    try:
        q.put_nowait("消息4")
    except:
        print("消息队列已满，现有消息数量%s" % q.qsize())

    if not q.empty():
        print("-------从队列中取消息------")
        for i in range(q.qsize()):
            print(q.get_nowait())

    if not q.full():
        q.put("消息4")
        print(q.qsize())