#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/8 20:46
# filename: 01.一个简单的异常.py

def exp_exception(x, y):
    try:
        a = x / y
        print("a=", a)
    except Exception:
        print("程序出现异常，异常信息：被除数为0")


exp_exception(2, 0)  # 程序出现异常，异常信息：被除数为0

exp_exception(1, 2)  # a= 0.5
