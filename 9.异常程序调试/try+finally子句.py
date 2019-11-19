#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/8 21:12
# filename: try+finally子句.py

def use_finally(x, y):
    try:
        a = x / y
    except ZeroDivisionError:
        print("Some bad thing happened: division by zero")
    finally:
        print("No matter what happend, I will show in front of ")


use_finally(2, 0)

"""
Some bad thing happened: division by zero
No matter what happend, I will show in front of 
"""
