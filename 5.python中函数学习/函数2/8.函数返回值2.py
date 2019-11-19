#!/usr/bin/env python
# -*- coding:utf8 -*-


def no_returm():
    print("no return 函数不写return语句")


def just_return():
    print("just return 函数只写return，不返回具体内容")
    return

def return_val():
    a = 20
    b = 10
    z = a+b
    print("return val函数写return语句，并返回求和结果..")
    return z

print("函数no retrun 调用结果:{}".format(no_returm()))
print("函数just return 调用结果:{}".format(just_return()))
print("函数return val 调用结果:{}".format(return_val()))

"""
no return 函数不写return语句
函数no retrun 调用结果:None
just return 函数只写return，不返回具体内容
函数just return 调用结果:None
return val函数写return语句，并返回求和结果..
函数return val 调用结果:30

"""