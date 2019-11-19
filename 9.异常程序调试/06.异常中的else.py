#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/8 21:05
# filename: 06.异常中的else.py
'''
如果在try子句执行时没有发生异常，就会执行else语句后的语句（如果
有else）。使用else子句比把所有语句都放在try子句里面更好，这样可以避
免一些意想不到而except又没有捕获的异常
'''


def model_exception(x, y):
    try:
        a = x / y
    except:
        print("Error happened")
    else:
        print("It went as expected")


model_exception(2, 1)  # It went as expected
