#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/8 20:55
# filename: 03.捕获多个异常.py

def mult_exception(x, y):
    try:
        a = x / y
        b = name
    except ZeroDivisionError:
        print("this is ZeroDivisionError")

    except NameError:
        print("This is NameError")


mult_exception(2, 0)  # this is ZeroDivisionError
mult_exception(2, 3)  # This is NameError
