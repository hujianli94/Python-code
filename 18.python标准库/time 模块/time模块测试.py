#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/17 12:42
# filename: time模块测试.py
import time
from loggingClass4 import MyLog


class TimeInfo(object):
    def __init__(self):
        self.log = MyLog()
        self.testTime()
        self.testLocaltime()
        self.testSleep(1)
        self.testStrftime()

    def testTime(self):
        self.log.info("开始测试time.time()函数")
        print('当前时间戳为：time.time() = {!r}'.format(time.time()))
        print('这里返回的是一个浮点数，它是1970纪元后经过的浮点秒数')
        print("\n")

    def testLocaltime(self):
        self.log.info("开始测试time.localtime()函数")
        print("当前本地时间为：time.localtime() = {!r}".format(time.localtime()))
        print("这里返回的是一个struct_time结构的元祖")
        print("\n")

    def testSleep(self, n):
        self.log.info("开始测试time.sleep()函数")
        print("这是计时器：time.sleep(5)")
        print("闭上眼睛1秒就可以了")
        time.sleep(n)
        print("\n")

    def testStrftime(self):
        self.log.info("开始测试time.strftime()函数")
        print("这个函数返回的是一个格式化的时间")
        print("time.strftime(%%Y-%%m-%%d %%X,time.localtime()) = {!r}".format(
            time.strftime("%Y-%m-%d %X", time.localtime())))
        print("\n")


if __name__ == '__main__':
    t1 = TimeInfo()
