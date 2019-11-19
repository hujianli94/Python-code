#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/8 21:07
# filename: 07.自定义异常.py

class MyError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "this is self define error"


def my_error_test():
    try:
        raise MyError()
    except MyError as e:
        print("Exception info: ", e)


my_error_test()  # Exception info:  this is self define error
