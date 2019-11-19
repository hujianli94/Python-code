#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/6 15:54
# filename: example01.py
num = 100
print('函数调用前num的值为:{}'.format(num))


def func_glo_l():
    global num
    num = 200
    print("函数体中num的值为{}".format(num))




func_glo_l()
print("函数调用结束后num的值为{}".format(num))

"""
函数调用前num的值为:100
函数体中num的值为200
函数调用结束后num的值为200
"""