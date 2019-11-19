#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/23 14:37
# filename: 4.等待线程结束.py
"""
join()方法，当前线程t1调用join()方法时，会阻塞当前线程，等到t1线程结束，如果t1线程结束
或者等待超时，则当前线程回到活动状态继续执行。
join(timeout=None)
参数timeout 设置超时时间，单位是秒。如果没有设置timeout时间，则可以一直等待
"""
import threading
import time

# 共享变量0
value = 0


# 线程体函数
def thread_body():
    global value
    # 当前线程对象
    print("ThreadA 开始.....")
    for n in range(2):
        print("ThreadA 执行.......")
        value += 1
        # 线程休眠
        time.sleep(1)
        print("ThreadA 结束.......")


def main():
    print("主线程 开始........")
    t1 = threading.Thread(target=thread_body, name="ThreadA")
    # 启动线程
    t1.start()
    # 主线程被阻塞，等待t1线程结束
    t1.join()
    print("value = {0}".format(value))
    print("主线程  结束.....")


if __name__ == '__main__':
    main()
