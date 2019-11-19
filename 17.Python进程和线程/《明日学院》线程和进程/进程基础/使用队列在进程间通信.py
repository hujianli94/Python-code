#!/usr/bin/env python
# -*- coding:utf8 -*-

'''
队列在进程中的通信
'''
from multiprocessing import Process, Queue  # 导入进程和队列
import time


def write_task(q):
    if not q.full():
        for i in range(5):
            message = "消息" + str(i)
            q.put(message)
            print("写入：{}".format(message))


def read_task(q):
    time.sleep(1)
    while not q.empty():
        print("读取：{}".format(q.get(True, 2)))


if __name__ == '__main__':
    print("---主进程开始-----")
    q = Queue()
    pw = Process(target=write_task, args=(q,))
    pr = Process(target=read_task, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.join()
    print("---主进程结束----")
