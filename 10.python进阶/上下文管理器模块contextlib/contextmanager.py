#!/usr/bin/env python
#-*- coding:utf8 -*-
import contextlib

@contextlib.contextmanager
def my_mgr(s, e):
    print(s)
    yield s + ' ' + e
    print(e)

#定义一个用装饰器contextlib.contextmanager 装饰的生成器my_mgr()方法
if __name__ == '__main__':
    with my_mgr('start', 'end') as val:
        print(val)
