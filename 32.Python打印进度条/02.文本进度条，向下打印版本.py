#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/28 9:24
# filename: 02.文本进度条，向下打印版本.py

import time


def bar(scale):
    print('===========执行开始============')
    for i in range(scale + 1):
        a = '#' * i
        b = '.' * (scale - i)
        c = (i / scale) * 100
        print('\r{:^3.0f}%[{}->{}]'.format(c, a, b), end='')
        time.sleep(0.05)
    print('\n===========执行结束============')


bar(100)
