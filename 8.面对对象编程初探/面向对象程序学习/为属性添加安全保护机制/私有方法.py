#!/usr/bin/env python
#-*- coding:utf8 -*-
class Private(object):
    def __init__(self):
        pass

    def __foo(self):
        print("@@@@这是一个私有的方法@@@@@.")

    def get_foo(self):
        print("首先，我是一个公有的方法")
        print("开始调用私有方法")
        self.__foo()
        print("公有方法和私有方法结束")

if __name__ == '__main__':
    hu = Private()
    print("开始调用公有方法：")
    hu.get_foo()
    print("开始调用私有方法：")
    print("查看类中的所有方法：")
    print(dir(hu))
    hu._Private__foo()