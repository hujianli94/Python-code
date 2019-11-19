#!/usr/bin/env python
#-*- coding:utf8 -*-
import sys,time

def jindutiao():
    for i in range(40):
        sys.stdout.write("#")   #输出类似print()
        sys.stdout.flush()  #将内存刷新到硬盘
        time.sleep(0.1)

jindutiao()