#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/8 21:01
# filename: 05.捕捉对象.py

def model_exception(x, y):
    try:
        a = x / y
        b = name

    except (ZeroDivisionError, NameError, TypeError) as e:
        print(e)


model_exception(2, 0)  # division by zero
