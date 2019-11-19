#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/4/29 12:31
# filename: 自定义异常类3.py
#继承Exception类
class MyError(Exception):
    pass

#需要异常类有一定的提示信息,可以重载__init__和__str__两个方法
class RangeError(Exception):
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return self.value


if __name__ == '__main__':
    raise RuntimeError("Range Error....!")
