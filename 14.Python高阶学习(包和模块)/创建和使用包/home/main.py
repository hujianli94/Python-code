#!/usr/bin/env python
#-*- coding:utf8 -*-
from size2 import *
from home_dir import size01
import sys

if __name__ == '__main__':
    print('weight= ',getWidth())
    print('heiht= ',getHeigh())

    change(10000,2000)
    print('修改weight后的值= ', getWidth())
    print('修改heiht后的值= ', getHeigh())


    print(size01.height)
    print(size01.width)

    print()
    for info in sys.path:
        print(info)