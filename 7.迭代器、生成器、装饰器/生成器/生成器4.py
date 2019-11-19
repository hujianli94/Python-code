#!/usr/bin/env python
#-*- coding:utf8 -*-

#通过生成器推导式构建

def generator():
    print(123)
    content = yield 1
    print("===========",content)
    print(456)
    yield 2

g = generator()
ret = g.__next__()
print("*****",ret)

ret = g.send("hello")
print("****",ret)


print()


def func1():
    print(11)
    print(333)
    yield 222
    print(666)
    yield 777

g_obj = func1()
print(g_obj.__next__())
print(g_obj.__next__())