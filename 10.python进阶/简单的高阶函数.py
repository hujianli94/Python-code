#!/usr/bin/env python
#-*- coding:utf8 -*-

#函数return返回函数
def func():
    print('in the func')
    return foo()
def foo():
    print('in the foo()')
    return 666

res = func()
print(res)
