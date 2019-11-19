#!/usr/bin/env python
#-*- coding:utf8 -*-
def abc(fun):
    #定义一个装饰器abc
    def warpper(*args,**kwargs):
        #定义包装饰器函数
        print("开始运行....")
        #调用被装饰的函数
        fun(*args,**kwargs)
        print("运行结束!")
    return warpper

@abc
def demo_decoration(x):   #返回包装饰器函数
    a = []
    for i in range(x):
        a.append(i)
    print(a)

@abc
def hello(name):
    print("Hello {}!".format(name))

if __name__ == '__main__':
    demo_decoration(5)
    print()
    hello("hujianli")