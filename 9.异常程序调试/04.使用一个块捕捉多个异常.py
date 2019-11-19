#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/8 20:59
# filename: 04.使用一个块捕捉多个异常.py

def model_exception(x, y):
    try:
        b = name
        a = x / y
    except (ZeroDivisionError, NameError, TypeError):
        print("one of ZeroDivisionError or NameError or TypeE")  # one of ZeroDivisionError or NameError or TypeE


model_exception(2, 0)
