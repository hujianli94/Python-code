#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/27 10:17
# filename: 使用队列实现进程间通信.py
from multiprocessing import Process, Queue
import os
import time
import random


def proce_write(q, urls):
    """
    写数据执行的代码
    :param q:
    :param urls:
    :return:
    """
    print("Process【{}】 is writing.....".format(os.getpid()))
    for url in urls:
        q.put(url)
        print("Put 【{}】 to queue.....".format(url))
        time.sleep(random.random())


def proce_read(q):
    """
    读数据的代码
    :param q:
    :return:
    """
    print("Process【{}】 is reading.....".format(os.getpid()))
    while True:
        url = q.get(True)
        print("Get 【{}】 from queue..".format(url))


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程
    q = Queue()
    proce_write1 = Process(target=proce_write, args=(q, ["url1", "url2", "url3"]))
    proce_write2 = Process(target=proce_write, args=(q, ["url4", "url5", "url6"]))
    proce_reader = Process(target=proce_read, args=(q,))

    # 启动子进程proc_writer,写入
    proce_write1.start()
    proce_write2.start()

    # 启动子进程proce_reader 读取
    proce_reader.start()

    # 等待proce_writer结束
    proce_write1.join()
    proce_write2.join()

    # proce_reader进程是死循环，无法等待其结束，需要强制进行终止
    proce_reader.terminate()
