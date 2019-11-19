#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/17 22:51
# filename: continue语句.py
for item in range(10):
    #当循环到3的时候，退出当前循环，进入下一次循环
    if item == 3:
        continue
    print("Count is :{0}".format(item))