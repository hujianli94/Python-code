#!/usr/bin/env python
# -*- coding:utf8 -*-
'''
start()能够创建线程
run()函数中的代码
'''
import threading


def thrfun(x, y):
    for i in range(x, y):
        print(str(i * i) + ";")


ma = threading.Thread(target=thrfun, args=(1, 6))
mb = threading.Thread(target=thrfun, args=(16, 20))
ma.start()
mb.start()
