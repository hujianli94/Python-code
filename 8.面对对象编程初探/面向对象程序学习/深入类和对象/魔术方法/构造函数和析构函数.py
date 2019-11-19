#!/usr/bin/env python
#-*- coding:utf8 -*-
class Test(object):
    def __init__(self):
        print("这个是构造函数....")

    def __del__(self):
        print("这个是析构函数....，结束时自动调用...")

hu = Test()

