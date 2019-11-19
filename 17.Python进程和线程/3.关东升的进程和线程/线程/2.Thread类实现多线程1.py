#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/23 14:18
# filename: 2.Thread类实现多线程1.py
import threading
import time


# 线程体函数
def thread_bady():
    # 当前线程对象
    t = threading.current_thread()

    for n in range(5):
        # 当前线程名
        print("第{}次执行线程:{}".format(n, t.name))
        # 线程休眠，如果不休眠，线程对象t1结束后才会执行线程对象t2线程将
        time.sleep(1)
    print("线程:{}执行完成！".format(t.name))


# 主函数
def main():
    # 创建线程对象t1
    t1 = threading.Thread(target=thread_bady, name="hu_thread")
    # 启动线程t1
    t1.start()

    # 创建线程对象t2
    t2 = threading.Thread(target=thread_bady, name="xiaojian_thread")
    # 启动线程t2
    t2.start()


if __name__ == '__main__':
    main()
