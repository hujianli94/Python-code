#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/17 22:49
# filename: break语句.py
for item in range(10):
    #当循环到3的时候退出整个循环
    if item == 3:
        break
    print("Count is:{0}".format(item))