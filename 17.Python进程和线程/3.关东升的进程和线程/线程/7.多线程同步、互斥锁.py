#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/23 15:42
# filename: 7.多线程同步、互斥锁.py

import threading
import time


class TickDB:
    def __init__(self):
        # 机票的数量
        self.ticket_count = 5

    def get_ticket_count(self):
        '''
        :return: 获得当前机票的数量
        '''
        return self.ticket_count

    def sell_ticket(self, name):
        """
        :return: 销售机票
        """
        # TODO
        # 线程休眠，模拟等待用户付款
        time.sleep(1)
        self.ticket_count -= 1
        if self.ticket_count < 1:
            print("机票已经售完，请换乘其他航空..............")
        else:
            print("第{0}号票，已经售出,【购买者】乘客：{1}，还剩下：{2}张票".format(self.ticket_count, name, self.ticket_count - 1))


# 创建TickDB对象
db = TickDB()
# 创建lock对象
lock = threading.Lock()


# 模拟选票线程体1
def thread_body1(name=None):
    # 声明为全局变量
    global db
    global lock
    while True:
        # 看这里！！开始锁定，加上小锁
        lock.acquire()
        curr_ticket_count = db.get_ticket_count()
        # 查询是否有票
        if curr_ticket_count > 0:
            db.sell_ticket(name)
        else:
            # 看这里，解锁，放开锁定
            lock.release()
            print("【{}】 您查询到的结果：无票".format(name))
            break
        # 解锁
        lock.release()
        time.sleep(1)

# 模拟选票线程体2
def thread_body2(name=None):
    # 声明为全局变量
    global db
    global lock
    while True:
        # 开始锁定，加上小锁
        lock.acquire()
        curr_ticket_count = db.get_ticket_count()
        # 查询是否有票
        if curr_ticket_count > 0:
            db.sell_ticket(name)
        else:
            # 看这里，解锁，放开锁定
            lock.release()
            print("【{}】您查询到的结果：无票".format(name))
            break
        #解锁
        lock.release()
        time.sleep(1)


def main():
    print("***************************************************************")
    print("*************** 欢迎来到XXX航空购票系统 ************************")
    print("***************************************************************")

    print("----------------------------------- t1开始购票--------------------------------------------------")
    # 创建线程对象t1
    t1 = threading.Thread(target=thread_body1, args=("t1",))
    # 启动线程t1
    t1.start()

    print("----------------------------------- t2开始购票--------------------------------------------------")
    # 创建线程对象t2
    t2 = threading.Thread(target=thread_body2, args=("t2",))
    # 启动线程t1
    t2.start()


if __name__ == '__main__':
    main()
