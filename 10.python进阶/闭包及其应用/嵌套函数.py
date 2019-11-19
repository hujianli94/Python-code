#!/usr/bin/env python
#-*- coding:utf8 -*-
x = 14          #定义一个全局变量

def foo():
    x = 3
    def bar():
        print("x is {}".format(x))
    bar()

if __name__ == '__main__':
    foo()
