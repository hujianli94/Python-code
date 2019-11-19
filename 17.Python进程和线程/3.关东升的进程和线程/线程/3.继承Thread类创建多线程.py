#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/23 14:27
# filename: 3.继承Thread类创建多线程.py
import threading
import time


class MyThread(threading.Thread):
    def __init__(self, name=None):
        super(MyThread, self).__init__(name=name)

    # 线程体函数
    def run(self):
        # 当前线程对象
        t = threading.current_thread()
        for n in range(5):
            # 当前线程名
            print("第{}此执行线程:{}".format(n, t.name))
            # 线程休眠
            time.sleep(1)
        print("线程{}执行完毕！".format(t.name))


def main():
    # 创建线程对象t1
    t1 = MyThread(name="t1-thread")
    # 启动线程t1
    t1.start()

    # 创建线程对象t2
    t2 = MyThread(name="t2-thread")
    # 启动线程t2
    t2.start()


if __name__ == '__main__':
    main()
