#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/18 22:43
# filename: 自定义异常类4.py
class MyException(Exception):

    def __init__(self, message):
        super(MyException, self).__init__(message)



hu = MyException(message="异常弹出")
print(hu)